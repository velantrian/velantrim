# 🔬 Velantrim Cognitive System Capability Audit v0.1

**Status:** RESEARCH AUDIT · DOCUMENTATION-BASED · NOT IMPLEMENTATION AUTHORITY  
**Date:** 2026-08-23  
**Evaluation target:** [`../vision/VELANTRIM_COGNITIVE_SYSTEM_VISION.md`](../vision/VELANTRIM_COGNITIVE_SYSTEM_VISION.md)  
**Method:** current AI/status documentation + live GitHub lifecycle checkpoints; code is not treated as the primary source for this conceptual audit.  

> This audit asks **what the ecosystem can already provide toward the Vision**, not what each project can claim in isolation.

---

## 🎯 1. Executive conclusion

The ecosystem is **not missing a single magical “brain module.”** Most desired capabilities already exist in bounded form across several projects.

The dominant gap is different:

> **There is not yet one validated end-to-end cognitive loop that composes meaning, memory, retrieval, relations, questioning, reasoning, human context, safe action, and durable continuation as one user-facing process.**

That means the next useful step is primarily **integration testing and capability composition**, not immediate invention of another subsystem.

A practical reading is:

```text
WE HAVE MANY PARTS
      ↓
THE PARTS HAVE STRONG BOUNDARIES
      ↓
SOME PARTS ARE ALREADY PRODUCT/TEST READY
      ↓
WHAT IS NOT YET PROVED
      ↓
CAN THEY COOPERATE AS ONE SIMPLE COGNITIVE LOOP?
```

---

## 🧭 2. Evaluation scale

| Mark | Meaning |
|---|---|
| ✅ | implemented / directly usable within its bounded scope |
| 🟡 | meaningful partial capability exists |
| 🔬 | research/specification only |
| 🔗 | requires bounded composition across projects |
| ❌ | material capability not established |
| 🧹 | likely duplication / simplification opportunity |
| ⚠️ | capability exists but authority or semantic scope must remain constrained |

`implemented != production authorized`  
`testable != proven sufficient`  
`composition != cognition`  
`retrieval != evidence`  
`memory != truth`

---

## 🧩 3. Project roles used in this audit

### 🗿 Titan

Primary role: orchestration, provider/model/tool composition, ordinary-user product path, files/tools E2E, restart continuity, recovery, Reader product path, bounded sandbox contracts.

Current important state:

- V1 product stages completed/closed in the bounded ordinary-user scope;
- bounded pilot evidence exists for the Titan product path;
- sandbox contracts and a backend-neutral protocol exist;
- `NullBackend` / deterministic `FakeBackend` allow lifecycle testing;
- **no runtime-capable generic sandbox backend is authorized by that work**;
- production/runtime authority remains separate.

### 💠 Crystal

Primary role: local-first trusted memory/evidence, provenance, admission, integrity, bounded Canon writes, Reader-side structured extraction/discovery.

Current Reader position includes bounded RC-1…RC-7 and lexical RC-9 capabilities, including structural mapping, multi-pass mechanics, proposition extraction, relation candidates and cross-document links.

Important boundary:

```text
Reader candidate != admitted evidence
similarity != identity
relation candidate != Canon relation
retrieval != evidence
```

Semantic/hybrid Reader runtime and vector/pgvector Reader activation remain unauthorized.

### 🌀 Mentaury Soul

Primary role: bounded cognition semantics — claims, beliefs, epistemic change, self/identity, relations, human-context interpretation and future affect/development research.

Current V1 Research/Core has implemented bounded contracts for:

- claim/provenance representation;
- claim→belief binding;
- epistemic routing;
- Evidence Gate lifecycle;
- anchored typed relations;
- hypothesis discrimination;
- privacy/capability/constraint classification;
- offline epistemic E2E.

Affect/attention/development work remains research-oriented; identity, relationship, retrieval/tool/action runtime remain unauthorized.

### 🧬 Native Kernel

Primary role: technology-neutral semantic laws, non-conflation, explicit provenance/context/authority, uncertainty, accountable revision/loss and conformance/falsification.

Current runtime expansion is frozen; Final Canon and production remain unauthorized. Its value to this Vision is **semantic constraint**, not orchestration or cognition runtime.

### 🌎 Continuum

Primary role: falsifiable process-continuity research — what minimum durable state is sufficient for work to continue across replaceable inference instances.

Current state:

- human reference gate closed;
- Capture Gold / Transfer Oracle human-approved;
- Experiment 0 pre-Pilot harness implemented;
- bounded Pilot preflight/adapter controls merged;
- Pilot remains `NOT_AUTHORIZED` and not run;
- Evidence Lock absent;
- E0-C/E0-T not started;
- production architecture remains unfrozen.

### 🪁 Mentaury Kernel

Primary role: technology-neutral composition invariants across semantic domains.

It preserves provenance, declared semantic loss and non-escalation. It has no runtime, cognition, truth, identity, action or production authority.

### 💻 EITI — implementation reference

EITI is a user-facing personal assistant/product reference with a concrete multi-layer memory system, BM25/FTS retrieval, provider chat, MOSC concept topology, PKG association, RNE goals/facts/questions/gaps, notes/files and local storage.

It is useful as **empirical implementation evidence and a prototype surface**, but its internal labels do not automatically define ecosystem-wide semantics or authority.

### 🚀 Cognitive OS — research architecture

Cognitive OS closely matches the Vision at the conceptual level: Interaction, Cognitive Control, Capability, Assurance and Memory planes; model routing; persistent memory; anti-degradation; modular human-facing and technical intelligence.

It remains a research architecture/design direction, not proof of an integrated runtime.

---

## 📊 4. Capability matrix

| Vision capability | Current level | Main contributors | TEST NOW? | Main gap |
|---|---|---|---|---|
| 🧠 Meaning / context | 🟡🔗 | Titan, Crystal Reader, Soul, Cognitive OS | 🟡 | no single validated context model spanning observation → interpretation → user intent → evidence state |
| 💾 Memory horizons | ✅🟡🔗 | EITI, Crystal, Titan, Soul, Continuum | ✅ | multiple memory notions exist; cross-domain retention/promotion policy is not yet one tested user loop |
| 🔎 Retrieval | ✅🟡 | Titan, Crystal Reader, EITI | ✅ | strong lexical/product retrieval exists; semantic/hybrid authority-safe retrieval is not yet established as one default |
| 🧾 Information extraction | ✅🟡 | Crystal Reader, Titan file path, model providers | ✅ | extraction quality and downstream admission remain deliberately separate |
| 🔗 Meaningful relations | 🟡🔬 | Crystal RC-5/RC-7, Soul ATR, EITI MOSC/PKG | 🟡 | relation types exist in different semantic regimes; no universal relation store should be assumed |
| ❓ Gap/question detection | 🟡🔬 | EITI RNE, Soul HDE/research, model reasoning, Cognitive OS | 🟡 | no validated system-level “what do I not understand?” controller |
| 💭 Reasoning | ✅🟡🔗 | model providers, Titan, Cognitive OS, Soul semantics | ✅ | model reasoning exists; routing/assurance and epistemic admission are separate and need composition tests |
| 👤 Progressive user understanding | 🟡 | EITI, Soul, Titan/Cognitive OS | 🟡 | user model, preference history and identity semantics are not yet one governed runtime path |
| ❤️ Affect / emotional context | 🔬🟡 | Soul research, Cognitive OS, EITI interaction | 🟡 | useful interaction behavior exists, but formal bounded affect-state/runtime semantics are not established |
| 🌱 Learning / development | 🟡🔬 | EITI local learning/association, Soul research, retrieval adaptation | 🟡 | several adaptation mechanisms exist; no unified governed learning lifecycle |
| 🔄 Long-lived work continuity | 🟡🔬 | Titan restart continuity, Continuum, Smart Context research | ✅ for Titan restart; 🔬 for cross-window process continuity | Continuum scientific Pilot/evidence not yet run |
| ⚙️ Tool/action orchestration | ✅🟡 | Titan | ✅ bounded product tools | generic sandbox execution remains protocol/test-double only |
| 🔐 Authority / safe mutation | ✅ | Crystal, Soul, Native Kernel, Mentaury Kernel, Titan boundaries | ✅ | strong architecture; main task is preserve it during composition |
| 🔍 Assurance / verification | ✅🟡 | Titan tests, Crystal gates, Soul Evidence Gate, Native conformance | ✅ | no single assurance controller for every cognitive result, nor should one silently become truth authority |
| 💬 Coherent user-facing experience | 🟡 | Titan, EITI, Cognitive OS | ✅ prototypes exist | ecosystem capabilities are not yet validated as one simple cross-project experience |

---

## 🧠 5. Capability analysis

### 5.1 Meaning and context — 🟡🔗

The ecosystem already contains several distinct components of “understanding”:

```text
raw input
  ↓
Titan / model interaction
  ↓
Crystal Reader structural/proposition extraction
  ↓
Soul claim / belief / relation semantics
  ↓
Cognitive OS interaction + routing concepts
```

But these must not be collapsed into one claim of machine understanding.

What is missing is a **bounded Context Model contract** that can say, for one user turn:

- observed input;
- candidate intent;
- active task/goal;
- relevant entities and relations;
- missing information;
- retrieved context;
- provenance references;
- uncertainty;
- next cognitive need.

This looks more like a **composition/test artifact** than a new intelligence engine.

### 5.2 Memory — ✅🟡🔗

Memory is already one of the strongest areas.

EITI demonstrates practical layers roughly equivalent to active/working/history/digest/profile/KB memory. Crystal provides stronger trusted provenance/admission semantics. Soul distinguishes claim, belief, identity and epistemic lifecycle. Titan has product/session/restart continuity. Continuum tests minimum sufficient process state.

The problem is therefore not “we need memory.”

The open problem is:

> **Which state belongs to which memory horizon, who may promote it, and what should be provided to the next cognitive step?**

Do not create one universal storage backend merely to make the diagram look simpler.

### 5.3 Retrieval and extraction — ✅🟡

This capability can be tested now.

Available building blocks include:

- Titan product file/data/tool path;
- Crystal bounded Reader layers and deterministic lexical discovery;
- EITI BM25/FTS and local memory search;
- model-provider reasoning after retrieval.

Current evidence strongly supports starting with the simple baseline:

```text
intent / query
→ lexical / bounded retrieval
→ candidate context
→ answer / inspection
→ measure usefulness
```

GraphRAG, ANN, vector activation or another retrieval framework should not become mandatory until the controlled test demonstrates a concrete deficit.

### 5.4 Meaningful relations — 🟡🔬

There are already multiple relation systems:

- Crystal Reader relation candidates / cross-document links;
- Soul anchored typed relations;
- EITI MOSC concept topology and PKG association;
- Knowledge Semantics cross-project relation vocabulary.

These are **not interchangeable**.

```text
association != epistemic relation
Reader relation candidate != admitted relation
Soul relation record != Crystal Canon relation
shared vocabulary != shared ownership
```

The next test should therefore evaluate whether relations improve task continuation/retrieval, not attempt to merge all graphs.

### 5.5 Questions and epistemic gaps — 🟡🔬

The desired self-questioning loop is partially represented:

- EITI RNE tracks goals/facts/questions/gaps;
- model reasoning can generate clarification questions;
- Soul HDE can structurally discriminate hypotheses;
- Cognitive OS provides routing/assurance concepts.

What is not established is a bounded controller that decides:

```text
ANSWER NOW
vs
RETRIEVE
vs
VERIFY
vs
ASK USER
vs
CREATE INTERNAL QUESTION
```

This is one of the highest-value integration-test gaps.

### 5.6 Reasoning — ✅🟡🔗

Reasoning capability already exists through provider models and Titan orchestration. The ecosystem should **not build a universal Logic Engine merely because reasoning has many forms**.

The useful missing layer is routing and evaluation:

```text
what kind of reasoning is needed?
→ which capability/model/tool?
→ what evidence/context?
→ what verification?
→ what authority can the result have?
```

Cognitive OS already provides a strong research framing for this.

### 5.7 Progressive user understanding — 🟡

EITI already demonstrates practical accumulation of profile/facts/history and adaptive memory. Soul provides the stricter semantic distinction needed to prevent inferred preferences from silently becoming identity. Titan/Cognitive OS can provide interaction/orchestration surfaces.

The gap is governance and composition, not lack of data structures.

A future test should explicitly distinguish:

```text
observed user statement
inferred preference
working personalization hint
long-lived preference
identity-relevant statement
```

### 5.8 Affect and human context — 🔬🟡

The ecosystem has interaction behavior and dedicated Soul research, but no basis yet for claiming a mature affect runtime.

The first useful target is modest:

> **Can affect/context change communication, attention or retrieval priority without changing truth, evidence, identity or action authority?**

That is testable without attempting to simulate “real feelings.”

### 5.9 Learning and development — 🟡🔬

EITI already contains local adaptation/association mechanisms. Soul has research on development and affect/attention. Retrieval policy can also adapt.

The danger is conflating all adaptation with learning.

The minimum test should ask whether the system becomes measurably better at:

- retaining relevant context;
- asking useful questions;
- retrieving prior decisions;
- avoiding repeated explanation;
- correcting a previously wrong working assumption.

No weight training is required for this experiment.

### 5.10 Continuity — 🟡🔬

There are two different meanings and they must remain separate.

**Titan restart continuity:** already product-tested within its bounded V1 path.

**Continuum process continuity:** scientific/research question. Pre-Pilot controls now exist, but Pilot is not authorized or run and no Evidence exists.

Therefore:

```text
restart continuity != process continuity proof
handoff success != identity continuity
context survival != epistemic truth
```

### 5.11 Action and execution — ✅🟡

Titan already has bounded user/product tools. The new sandbox work improves the formal path toward generic isolated execution, but the current backend protocol and test doubles are deliberately non-executing.

So the audit should record:

```text
bounded product/tool execution        ✅
generic sandbox contracts             ✅
backend protocol                      ✅
non-executing Fake/Null backend       ✅
runtime-capable generic sandbox       ❌ / not authorized by this work
```

This distinction matters because the Vision only needs **safe capability selection**, not arbitrary code execution on day one.

---

## 🧪 6. What can be tested now?

### Test A — Simple cognitive loop

**Recommended first test.**

Goal: determine whether existing capabilities already feel like one useful cognitive process.

```text
👤 user gives a real task / idea
        ↓
🧠 identify goal + context + ambiguity
        ↓
🔎 retrieve relevant prior information
        ↓
🔗 connect it to the current topic
        ↓
❓ identify one meaningful gap if present
        ↓
💭 reason using retrieved context
        ↓
💬 answer
        ↓
📝 retain only justified working state
        ↓
next turn / restart
        ↓
🔄 continue without unnecessary re-explanation
```

**Success measures:**

- goal retained;
- relevant prior information recalled;
- irrelevant memory avoided;
- unresolved ambiguity identified;
- no invented user preference/decision;
- answer uses provenance where material;
- next turn continues correctly;
- authority boundaries preserved.

This can be exercised before solving every research question.

### Test B — Memory horizon test

Give the system mixed information:

- throwaway conversational detail;
- current-task constraint;
- temporary hypothesis;
- durable preference;
- externally sourced factual claim;
- explicitly trusted decision.

Measure whether it places/uses them differently rather than treating all six as equivalent memory.

### Test C — Retrieval quality baseline

Use one controlled corpus and compare:

1. lexical/BM25 baseline;
2. existing bounded hybrid mechanisms if already available in the test host;
3. relation-assisted retrieval only where justified.

Do **not** add GraphRAG merely to fill a matrix cell.

### Test D — Question quality

Present an under-specified task and score whether the system:

- asks a genuinely necessary question;
- retrieves before asking when memory already contains the answer;
- does not ask when uncertainty is immaterial;
- distinguishes internal hypothesis checking from user clarification.

### Test E — Restart / handoff

Run the same task before and after a restart/context replacement.

Compare:

- goal retention;
- decisions;
- rejected/deferred paths;
- constraints;
- open questions;
- provenance references;
- next step;
- obsolete-state carryover.

This uses Titan's practical continuity as a baseline and can later feed Continuum experiments without claiming Continuum evidence prematurely.

---

## 🧱 7. The smallest useful integration target

Do **not** start by wiring every project together.

A minimal useful target is:

```text
                  👤 USER
                     │
                     ▼
              🗿 ORCHESTRATION
               What is needed?
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
   💠 MEMORY/READ   🤖 MODEL    🔎 RETRIEVAL
         │           │           │
         └───────────┼───────────┘
                     ▼
               🧩 WORKING CONTEXT
                     │
                     ▼
               ❓ GAP / QUESTION
                     │
                     ▼
                 💭 REASON
                     │
                     ▼
                 💬 ANSWER
                     │
                     ▼
             📝 BOUNDED RETENTION
```

At first:

- Titan can host orchestration/product interaction;
- Crystal can provide bounded read/trusted-memory capability where required;
- the provider model can supply reasoning;
- Soul contracts can constrain claim/belief/perspective handling where that semantic distinction is actually needed;
- Native Kernel/Mentaury Kernel remain invariants/composition constraints, not runtime routers;
- Continuum remains a later experimental consumer of the resulting explicit process state.

This is deliberately smaller than “integrate the whole ecosystem.”

---

## 🧹 8. Simplification opportunities

### 8.1 Do not create another central cognitive project

There is no evidence yet that the Vision requires a seventh core runtime.

### 8.2 Do not merge all memory systems

Different memory stores have different semantics and authority. A common **handoff/context contract** is more promising than a common database.

### 8.3 Do not merge every graph

MOSC/PKG associations, Crystal Reader links, Soul typed relations and future knowledge graphs answer different questions.

### 8.4 Prefer a capability router over a project router

The user intent should map to capabilities:

```text
NEED MEMORY
NEED RETRIEVAL
NEED VERIFICATION
NEED REASONING
NEED CLARIFICATION
NEED ACTION
```

Only then should the system resolve which project/provider supplies the capability.

### 8.5 Test simple retrieval before adding advanced retrieval

Existing lexical/BM25 and bounded Reader capabilities are sufficient to establish a baseline. Advanced GraphRAG/vector mechanisms should need measured justification.

---

## ⚠️ 9. Important gaps that remain real

1. **Unified bounded Context Model** — one explicit task/context state usable across capability calls.
2. **Capability-selection policy** — decide memory/retrieval/reason/verify/ask/action from the current need.
3. **Question/gap controller** — avoid both silent guessing and unnecessary clarification.
4. **Cross-domain retention policy** — working → temporary → durable/trusted without authority leakage.
5. **User-model governance** — distinguish inferred personalization from belief/identity.
6. **Affect-state semantics** — if adopted, keep it attributed, uncertain and non-authoritative.
7. **Cross-project composition test harness** — validate the cognitive loop without pretending composition itself is cognition.
8. **Continuum Pilot/Evidence** — still a research gate, not a prerequisite for the first practical cognitive-loop test.
9. **Runtime-capable generic sandbox** — only if real use cases demonstrate a need beyond existing bounded product tools.

---

## 🚫 10. What this audit does NOT recommend building now

Do not automatically implement:

- a new central Kernel;
- a universal Logic Engine;
- one mega-memory database;
- one global knowledge graph;
- GraphRAG everywhere;
- a generic autonomous agent loop;
- a runtime affect engine;
- a full “consciousness architecture”;
- automatic Canon writing;
- automatic identity mutation;
- generic sandbox execution merely because contracts now exist.

Each of these requires a measured problem first.

---

## 🚦 11. Recommended test sequence

```text
T0 — Freeze Vision + audit baseline
        ↓
T1 — Meaning/context + retrieval + answer
        ↓
T2 — Memory horizon / retention test
        ↓
T3 — Gap detection / question-quality test
        ↓
T4 — Restart / successor-context test
        ↓
T5 — Relation-assisted retrieval test
        ↓
T6 — Governed user-model / preference test
        ↓
T7 — Affect-aware interaction test (bounded)
        ↓
T8 — Safe action/tool selection test
        ↓
REASSESS
```

After every test ask:

```text
Did existing mechanisms solve the need?
│
├── YES → keep architecture simple
│
└── NO  → identify exact measured gap
          ↓
       smallest bounded change
```

---

## 🌟 12. Audit conclusion

The current Velantrim ecosystem already contains a surprisingly large fraction of the Vision's raw capabilities.

The strongest existing areas are:

- memory and provenance;
- bounded retrieval/extraction;
- orchestration/product flow;
- epistemic and authority boundaries;
- typed claims/relations/belief lifecycle;
- test/review discipline;
- restart continuity;
- modular cognitive architecture research.

The weakest area is not “intelligence” in the abstract. It is the **validated coordination of these abilities as one simple long-lived user experience**.

Therefore the most valuable next move is:

> **Build/test the smallest cross-capability cognitive loop before adding new architecture.**

North Star:

```text
ПОНЯТЬ
→ ВСПОМНИТЬ
→ НАЙТИ
→ СВЯЗАТЬ
→ СПРОСИТЬ
→ ПОДУМАТЬ
→ ОТВЕТИТЬ
→ СОХРАНИТЬ
→ ПРОДОЛЖИТЬ
```

Then add “НАУЧИТЬСЯ” only as measured, governed improvement over repeated runs — not as an excuse for uncontrolled mutation.
