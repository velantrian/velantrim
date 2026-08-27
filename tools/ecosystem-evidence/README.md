# Ecosystem Evidence Router / Verifier v0.1.1

This folder is an **orientation and evidence-pointer verification tool**, not an ecosystem status authority.

## Invariants

- project-local manifests own their own vocabulary;
- the index only routes;
- a binding contains check types + JSON Pointers into an existing project-local manifest;
- `FAIL != INCONCLUSIVE != WARN`;
- shallow history cannot prove ancestry/drift;
- missing git cannot be reported as "commit missing";
- path existence or test definitions do not prove runtime enablement, CI success, or authorization.

## Bound projects

- Crystal — `docs/status/implementation-manifest.json`
- Titan — `docs/project_status/FOR_AI.json`
- Mentaury Soul — `docs/ai/project_manifest.json` routing contract
- Native Kernel — `project-state.json`
- Continuum — `project-state.json`

Mentaury-Kernel, AI Skills, Cognitive OS and the umbrella repository remain index-only because the bounded inspection did not establish a suitable project-local machine-state manifest. AI Skills explicitly states that a separate machine-state file is not required at its current repository scope.

## Usage

```bash
python3 verify_ecosystem.py \
  --index ecosystem_status_index.json \
  --claims bindings/crystal.claims.json --repo-root /path/to/crystal \
  --claims bindings/titan.claims.json --repo-root /path/to/titan \
  --unshallow --require-conclusive
```

`--require-conclusive` makes any `INCONCLUSIVE` result non-zero. `--strict` additionally makes `WARN` non-zero.

The verifier never merges, enables runtime, grants capability, changes Canon, or interprets a project-local status as ecosystem-wide authority.
