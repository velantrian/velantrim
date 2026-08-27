#!/usr/bin/env python3
"""verify_ecosystem.py — evidence-pointer verifier for Velantrim project-local manifests.

v0.1.1 hardening:
* the ecosystem index is actually loaded and checked when --index is supplied;
* FAIL, WARN and INCONCLUSIVE remain distinct;
* --require-conclusive makes INCONCLUSIVE non-zero; --strict also makes WARN non-zero;
* git unavailable is INCONCLUSIVE, never "commit not found";
* checkpoint drift is counted only after complete-history ancestry is established;
* claims/index files receive bounded schema validation;
* test-definition counting is named honestly and is not CI proof.

The verifier does not own project status and does not infer authority. A binding
contains only a check type plus JSON Pointer(s) into a project's own manifest.
"""
from __future__ import annotations
import argparse, ast, json, re, subprocess, sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
PASS, FAIL, WARN, INCONCLUSIVE, INFO = "PASS", "FAIL", "WARN", "INCONCLUSIVE", "INFO"
ICON = {PASS: "✅", FAIL: "❌", WARN: "⚠️ ", INCONCLUSIVE: "❔", INFO: "ℹ️ "}
CLAIMS_SCHEMA_VERSIONS = {"0.1", "0.1.1"}
INDEX_SCHEMA_VERSIONS = {"0.1", "0.1.1"}
ALLOWED_CLAIM_TYPES = {"path_exists","symbol_defined","test_definitions_at_least","test_count_at_least","commit_known","commit_is_ancestor_or_equal","checkpoint_drift"}

def json_pointer(doc: Any, pointer: str) -> Any:
    if pointer in ("", "/"): return doc
    if not isinstance(pointer, str) or not pointer.startswith("/"): raise ValueError(f"pointer должен начинаться с '/': {pointer!r}")
    node = doc
    for raw in pointer.split("/")[1:]:
        tok = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(node, list):
            try: idx = int(tok)
            except ValueError as exc: raise TypeError(f"ожидался индекс списка, получено {tok!r}") from exc
            if idx < 0 or idx >= len(node): raise IndexError(f"индекс {idx} вне диапазона для {pointer!r}")
            node = node[idx]
        elif isinstance(node, dict):
            if tok not in node: raise KeyError(f"нет ключа {tok!r} в {pointer!r}")
            node = node[tok]
        else: raise TypeError(f"нельзя индексировать {type(node).__name__} по {tok!r}")
    return node

class GitUnavailable(Exception): pass

def _run_git(root: Path, *args: str) -> tuple[int,str,str]:
    try:
        p = subprocess.run(["git","-C",str(root),*args], capture_output=True, text=True, timeout=120)
    except FileNotFoundError as exc: raise GitUnavailable("git не найден в PATH") from exc
    except subprocess.TimeoutExpired as exc: raise GitUnavailable(f"git {' '.join(args)} превысил таймаут") from exc
    return p.returncode, p.stdout.strip(), p.stderr.strip()

def is_git_repo(root: Path) -> tuple[str,str]:
    try: code,out,err=_run_git(root,"rev-parse","--is-inside-work-tree")
    except GitUnavailable as exc: return INCONCLUSIVE,str(exc)
    return (PASS,"git work tree") if code==0 and out=="true" else (FAIL,err or "не git-репозиторий")

def current_head(root: Path)->tuple[str,str]:
    try: code,out,err=_run_git(root,"rev-parse","HEAD")
    except GitUnavailable as exc: return INCONCLUSIVE,str(exc)
    return (PASS,out) if code==0 and re.fullmatch(r"[0-9a-fA-F]{40}",out) else (INCONCLUSIVE,err or "HEAD не прочитан")

def shallow_state(root: Path)->tuple[str,bool|None,str]:
    try: code,out,err=_run_git(root,"rev-parse","--is-shallow-repository")
    except GitUnavailable as exc: return INCONCLUSIVE,None,str(exc)
    if code!=0: return INCONCLUSIVE,None,err or "не удалось определить shallow-state"
    if out=="true": return PASS,True,"shallow"
    if out=="false": return PASS,False,"complete history"
    return INCONCLUSIVE,None,f"неожиданный ответ: {out!r}"

def commit_presence_local(root: Path,sha:str)->tuple[str,str]:
    try: code,_,err=_run_git(root,"cat-file","-e",f"{sha}^{{commit}}")
    except GitUnavailable as exc: return INCONCLUSIVE,str(exc)
    return (PASS,f"{sha[:12]} есть в локальной истории") if code==0 else (FAIL,err or f"{sha[:12]} отсутствует локально")

def fetch_commit(root: Path,sha:str)->tuple[str,str]:
    try: code,_,err=_run_git(root,"fetch","--depth","1","origin",sha)
    except GitUnavailable as exc: return INCONCLUSIVE,str(exc)
    return (PASS,f"{sha[:12]} найден точечным fetch") if code==0 else (FAIL,err or f"{sha[:12]} не найден на origin")

def ensure_commit_known(root:Path,sha:str)->tuple[str,str]:
    state,detail=commit_presence_local(root,sha)
    if state in (PASS,INCONCLUSIVE): return state,detail
    state,detail=fetch_commit(root,sha)
    if state in (PASS,INCONCLUSIVE): return state,detail
    return FAIL,f"{sha[:12]} не найден ни локально, ни на origin"

def unshallow(root:Path)->tuple[str,str]:
    state,shallow,detail=shallow_state(root)
    if state!=PASS: return state,detail
    if not shallow: return PASS,"history already complete"
    try: code,_,err=_run_git(root,"fetch","--unshallow","origin")
    except GitUnavailable as exc: return INCONCLUSIVE,str(exc)
    return (PASS,"repository unshallowed") if code==0 else (INCONCLUSIVE,err or "git fetch --unshallow failed")

def ancestor_check(root:Path,older:str,newer:str,allow_unshallow:bool)->tuple[str,str]:
    state,detail=ensure_commit_known(root,older)
    if state!=PASS: return state,detail
    state,shallow,detail=shallow_state(root)
    if state!=PASS: return INCONCLUSIVE,detail
    if shallow:
        if not allow_unshallow: return INCONCLUSIVE,"репозиторий shallow — ancestry ненадёжна; используйте --unshallow"
        state,detail=unshallow(root)
        if state!=PASS: return INCONCLUSIVE,detail
    try: code,_,err=_run_git(root,"merge-base","--is-ancestor",older,newer)
    except GitUnavailable as exc: return INCONCLUSIVE,str(exc)
    if code==0: return PASS,f"{older[:12]} — предок {newer[:12]} (или равен)"
    if code==1: return FAIL,f"{older[:12]} НЕ является предком {newer[:12]}"
    return INCONCLUSIVE,err or f"merge-base вернул код {code}"

def commits_between(root:Path,older:str,newer:str)->tuple[str,int|None,str]:
    try: code,out,err=_run_git(root,"rev-list","--count",f"{older}..{newer}")
    except GitUnavailable as exc: return INCONCLUSIVE,None,str(exc)
    return (PASS,int(out),f"{out} commits") if code==0 and out.isdigit() else (INCONCLUSIVE,None,err or "не удалось посчитать commits")

def origin_repo_slug(root:Path)->tuple[str,str|None,str]:
    try: code,out,err=_run_git(root,"config","--get","remote.origin.url")
    except GitUnavailable as exc: return INCONCLUSIVE,None,str(exc)
    if code!=0 or not out: return INCONCLUSIVE,None,err or "origin URL отсутствует"
    for pattern in (r"^https?://github\.com/([^/]+/[^/]+?)(?:\.git)?$",r"^git@github\.com:([^/]+/[^/]+?)(?:\.git)?$",r"^ssh://git@github\.com/([^/]+/[^/]+?)(?:\.git)?$"):
        m=re.match(pattern,out.strip())
        if m: return PASS,m.group(1).removesuffix(".git"),out.strip()
    return INCONCLUSIVE,None,f"неизвестный формат origin: {out.strip()}"

def _parse(path:Path)->ast.Module|None:
    try: return ast.parse(path.read_text(encoding="utf-8",errors="replace"))
    except (SyntaxError,ValueError,OSError): return None

def symbol_is_defined(path:Path,symbol:str)->tuple[bool,str]:
    tree=_parse(path)
    if tree is None:
        try: text=path.read_text(encoding="utf-8",errors="replace")
        except OSError: return False,"файл не читается"
        return symbol in text,"текстовый fallback; не structural proof"
    for node in ast.walk(tree):
        if isinstance(node,(ast.ClassDef,ast.FunctionDef,ast.AsyncFunctionDef)) and node.name==symbol: return True,f"{type(node).__name__} line {node.lineno}"
        if isinstance(node,ast.Assign):
            for t in node.targets:
                if isinstance(t,ast.Name) and t.id==symbol: return True,f"assignment line {node.lineno}"
        if isinstance(node,ast.AnnAssign) and isinstance(node.target,ast.Name) and node.target.id==symbol: return True,f"annotated assignment line {node.lineno}"
    return False,"не найден"

def count_test_definitions(path:Path)->int:
    files=sorted(path.rglob("test_*.py")) if path.is_dir() else [path]
    total=0
    for file in files:
        tree=_parse(file)
        if tree is None: continue
        total += sum(1 for node in ast.walk(tree) if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and node.name.startswith("test_"))
    return total

class PathGuardError(Exception): pass

def resolve_inside(root:Path,rel:str)->Path:
    if not isinstance(rel,str) or not rel.strip(): raise PathGuardError("пустой путь")
    candidate=(root/rel).resolve(); rr=root.resolve()
    if candidate!=rr and rr not in candidate.parents: raise PathGuardError(f"путь вне корня репозитория: {rel}")
    return candidate

def load_json(path:Path)->dict:
    value=json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value,dict): raise ValueError(f"{path}: JSON root должен быть object")
    return value

def _require_pointer(claim:dict,key:str)->None:
    value=claim.get(key)
    if not isinstance(value,str) or not value.startswith("/"): raise ValueError(f"{claim.get('id','?')}: {key} должен быть JSON Pointer")

def load_claims_file(path:Path)->dict:
    data=load_json(path); version=str(data.get("claims_schema_version"))
    if version not in CLAIMS_SCHEMA_VERSIONS: raise ValueError(f"{path}: claims_schema_version={version!r}")
    if not isinstance(data.get("project"),str) or not data["project"]: raise ValueError(f"{path}: нужен project")
    if not isinstance(data.get("project_manifest"),str) or not data["project_manifest"]: raise ValueError(f"{path}: нужен project_manifest")
    claims=data.get("claims")
    if not isinstance(claims,list): raise ValueError(f"{path}: claims должен быть list")
    seen=set()
    for claim in claims:
        if not isinstance(claim,dict): raise ValueError(f"{path}: claim должен быть object")
        cid=claim.get("id"); kind=claim.get("type")
        if not isinstance(cid,str) or not cid: raise ValueError(f"{path}: claim без id")
        if cid in seen: raise ValueError(f"{path}: duplicate id {cid}")
        seen.add(cid)
        if kind not in ALLOWED_CLAIM_TYPES: raise ValueError(f"{path}: {cid}: unknown type {kind!r}")
        if kind in {"path_exists","commit_known"}: _require_pointer(claim,"pointer")
        elif kind=="symbol_defined":
            _require_pointer(claim,"path_pointer")
            if "symbol_pointer" in claim: _require_pointer(claim,"symbol_pointer")
            elif not isinstance(claim.get("symbol"),str) or not claim.get("symbol"): raise ValueError(f"{path}: {cid}: нужен symbol или symbol_pointer")
        elif kind in {"test_definitions_at_least","test_count_at_least"}:
            _require_pointer(claim,"path_pointer"); _require_pointer(claim,"min_pointer")
        elif kind=="commit_is_ancestor_or_equal":
            _require_pointer(claim,"older_pointer")
            if "newer_pointer" in claim: _require_pointer(claim,"newer_pointer")
        elif kind=="checkpoint_drift":
            _require_pointer(claim,"older_pointer")
            if "warn_above" in claim and (not isinstance(claim["warn_above"],int) or claim["warn_above"]<0): raise ValueError(f"{path}: {cid}: warn_above invalid")
    return data

def load_index(path:Path)->dict:
    data=load_json(path); version=str(data.get("index_schema_version"))
    if version not in INDEX_SCHEMA_VERSIONS: raise ValueError(f"{path}: index_schema_version={version!r}")
    projects=data.get("projects")
    if not isinstance(projects,list): raise ValueError(f"{path}: projects должен быть list")
    ids=set(); repos=set()
    for item in projects:
        if not isinstance(item,dict): raise ValueError(f"{path}: project entry должен быть object")
        pid=item.get("id"); repo=item.get("repo")
        if not isinstance(pid,str) or not pid: raise ValueError(f"{path}: project без id")
        if not isinstance(repo,str) or "/" not in repo: raise ValueError(f"{path}: {pid}: invalid repo")
        if pid in ids: raise ValueError(f"duplicate project id {pid}")
        if repo.lower() in repos: raise ValueError(f"duplicate repo {repo}")
        ids.add(pid); repos.add(repo.lower())
    return data

@dataclass
class ClaimResult:
    claim_id:str; kind:str; result:str; detail:str=""

def run_claim(root:Path,manifest:dict,claim:dict,allow_unshallow:bool)->ClaimResult:
    cid=claim["id"]; kind=claim["type"]
    def pv(key="pointer"): return json_pointer(manifest,claim[key])
    try:
        if kind=="path_exists":
            rel=pv(); path=resolve_inside(root,rel); return ClaimResult(cid,kind,PASS if path.exists() else FAIL,str(rel))
        if kind=="symbol_defined":
            rel=pv("path_pointer"); symbol=claim.get("symbol") or pv("symbol_pointer"); path=resolve_inside(root,rel)
            if not path.is_file(): return ClaimResult(cid,kind,FAIL,f"файл отсутствует: {rel}")
            found,how=symbol_is_defined(path,symbol); return ClaimResult(cid,kind,PASS if found else FAIL,f"{rel} :: {symbol} ({how})")
        if kind in {"test_definitions_at_least","test_count_at_least"}:
            rel=pv("path_pointer"); minimum=int(pv("min_pointer")); path=resolve_inside(root,rel)
            if not path.exists(): return ClaimResult(cid,kind,FAIL,f"путь отсутствует: {rel}")
            actual=count_test_definitions(path); result=PASS if actual>=minimum else FAIL
            return ClaimResult(cid,kind,result,f"{actual} {'>=' if result==PASS else '<'} {minimum} test definitions; NOT CI proof")
        if kind=="commit_known":
            state,detail=ensure_commit_known(root,pv()); return ClaimResult(cid,kind,state,detail)
        if kind=="commit_is_ancestor_or_equal":
            older=pv("older_pointer")
            if "newer_pointer" in claim: newer=pv("newer_pointer")
            else:
                state,newer=current_head(root)
                if state!=PASS: return ClaimResult(cid,kind,INCONCLUSIVE,newer)
            state,detail=ancestor_check(root,older,newer,allow_unshallow); return ClaimResult(cid,kind,state,detail)
        if kind=="checkpoint_drift":
            older=pv("older_pointer"); state,newer=current_head(root)
            if state!=PASS: return ClaimResult(cid,kind,INCONCLUSIVE,newer)
            ancestry,detail=ancestor_check(root,older,newer,allow_unshallow)
            if ancestry==FAIL: return ClaimResult(cid,kind,FAIL,f"drift не считается: {detail}")
            if ancestry!=PASS: return ClaimResult(cid,kind,INCONCLUSIVE,f"drift не считается: {detail}")
            state,count,detail=commits_between(root,older,newer)
            if state!=PASS or count is None: return ClaimResult(cid,kind,INCONCLUSIVE,detail)
            budget=int(claim.get("warn_above",50)); return ClaimResult(cid,kind,WARN if count>budget else INFO,f"HEAD на {count} коммитов впереди checkpoint")
        return ClaimResult(cid,kind,INCONCLUSIVE,f"unknown claim type {kind}")
    except (KeyError,IndexError,ValueError,TypeError) as exc: return ClaimResult(cid,kind,FAIL,f"pointer/schema value не резолвится: {exc}")
    except PathGuardError as exc: return ClaimResult(cid,kind,FAIL,str(exc))

def relative_if_inside(path:Path,root:Path)->str|None:
    try: return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError: return None

def validate_binding_against_index(index:dict,index_path:Path,claims_path:Path,binding:dict,repo_root:Path)->list[ClaimResult]:
    project=binding["project"]; matches=[p for p in index["projects"] if p["id"]==project]
    if not matches: return [ClaimResult("index_project_route","index_binding",FAIL,f"{project!r} отсутствует в index")]
    entry=matches[0]; results=[]
    expected=entry.get("project_manifest")
    results.append(ClaimResult("index_manifest_route","index_binding",PASS if expected==binding["project_manifest"] else FAIL,f"index={expected!r}, binding={binding['project_manifest']!r}"))
    expected_claims=entry.get("claims_file"); actual=relative_if_inside(claims_path,index_path.parent)
    results.append(ClaimResult("index_claims_route","index_binding",PASS if expected_claims==actual else FAIL,f"index={expected_claims!r}, actual={actual!r}"))
    state,slug,detail=origin_repo_slug(repo_root)
    if state==PASS and slug is not None: results.append(ClaimResult("index_repo_identity","index_binding",PASS if slug.lower()==entry["repo"].lower() else FAIL,f"index={entry['repo']}, origin={slug}"))
    else: results.append(ClaimResult("index_repo_identity","index_binding",INCONCLUSIVE,detail))
    return results

@dataclass
class ProjectReport:
    project:str; manifest_path:str; manifest_readable:bool; results:list[ClaimResult]=field(default_factory=list); error:str|None=None
    def verdict(self)->str:
        if not self.manifest_readable or (self.error and not self.results): return "FAILED"
        if any(r.result==FAIL for r in self.results): return "FAILED"
        if any(r.result==INCONCLUSIVE for r in self.results): return "PARTIALLY_VERIFIED"
        if any(r.result==WARN for r in self.results): return "VERIFIED_WITH_WARNINGS"
        return "VERIFIED"

def run_project(claims_path:Path,repo_root:Path,allow_unshallow:bool,index:dict|None,index_path:Path|None)->ProjectReport:
    binding=load_claims_file(claims_path); report=ProjectReport(binding["project"],binding["project_manifest"],False)
    repo_state,repo_detail=is_git_repo(repo_root)
    if repo_state!=PASS: report.error=repo_detail
    if index is not None and index_path is not None: report.results.extend(validate_binding_against_index(index,index_path,claims_path,binding,repo_root))
    try: manifest_abs=resolve_inside(repo_root,binding["project_manifest"])
    except PathGuardError as exc: report.error=str(exc); return report
    if not manifest_abs.is_file(): report.error=f"манифест проекта не найден: {binding['project_manifest']}"; return report
    try: manifest=load_json(manifest_abs)
    except (json.JSONDecodeError,ValueError) as exc: report.error=f"манифест проекта не парсится: {exc}"; return report
    report.manifest_readable=True
    for claim in binding["claims"]:
        needs_git=claim["type"] in {"commit_known","commit_is_ancestor_or_equal","checkpoint_drift"}
        if needs_git and repo_state!=PASS: report.results.append(ClaimResult(claim["id"],claim["type"],INCONCLUSIVE,repo_detail))
        else: report.results.append(run_claim(repo_root,manifest,claim,allow_unshallow))
    return report

def print_report(report:ProjectReport)->None:
    print(f"\n{'='*68}\nproject  : {report.project}\nmanifest : {report.manifest_path}{'' if report.manifest_readable else ' [UNREADABLE]'}\nverdict  : {report.verdict()}")
    if report.error: print(f"  {ICON[WARN]} preflight: {report.error}")
    for r in report.results:
        print(f"  {ICON[r.result]} [{r.kind}] {r.claim_id}")
        if r.detail: print(f"       {r.detail}")

def main(argv:list[str]|None=None)->int:
    p=argparse.ArgumentParser(description=__doc__.split("\n\n")[0]); p.add_argument("--index",type=Path); p.add_argument("--claims",action="append",default=[],type=Path); p.add_argument("--repo-root",action="append",default=[],type=Path); p.add_argument("--unshallow",action="store_true"); p.add_argument("--require-conclusive",action="store_true"); p.add_argument("--strict",action="store_true"); p.add_argument("--json",action="store_true"); args=p.parse_args(argv)
    if not args.claims: p.error("нужен хотя бы один --claims")
    if len(args.claims)!=len(args.repo_root): p.error("число --repo-root должно совпадать с --claims")
    index=None; index_path=None
    if args.index:
        index_path=args.index.resolve()
        try: index=load_index(index_path)
        except (OSError,json.JSONDecodeError,ValueError) as exc: print(f"index не проходит схему: {exc}",file=sys.stderr); return 2
    try: reports=[run_project(c.resolve(),r.resolve(),args.unshallow,index,index_path) for c,r in zip(args.claims,args.repo_root)]
    except (OSError,json.JSONDecodeError,ValueError) as exc: print(f"binding не проходит схему: {exc}",file=sys.stderr); return 2
    if args.json:
        print(json.dumps({"reports":[{"project":x.project,"verdict":x.verdict(),"manifest_path":x.manifest_path,"error":x.error,"results":[r.__dict__ for r in x.results]} for x in reports]},ensure_ascii=False,indent=2))
    else:
        for x in reports: print_report(x)
    has_fail=any((not x.manifest_readable) or any(r.result==FAIL for r in x.results) for x in reports)
    has_inc=any(any(r.result==INCONCLUSIVE for r in x.results) for x in reports); has_warn=any(any(r.result==WARN for r in x.results) for x in reports)
    if has_fail: return 1
    if args.strict and (has_warn or has_inc): return 1
    if args.require_conclusive and has_inc: return 1
    return 0

if __name__=="__main__": sys.exit(main())
