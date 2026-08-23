# Velantrim Knowledge Semantics v0.1

**Status:** Cross-project semantic vocabulary  
**Authority:** Descriptive only; not a runtime, authority domain, Canon, database, reasoning engine, or admission engine.  
**Scope:** Shared vocabulary for describing knowledge objects across Velantrim projects.

## 1. Purpose

Velantrim Knowledge Semantics defines five orthogonal descriptive dimensions that may be attached to a knowledge object without creating a new subsystem or transferring authority between existing projects.

A knowledge object may express several or all dimensions simultaneously. The dimensions are not pipeline stages and are not separate databases.

> **Knowledge Semantics = shared vocabulary, not a new system.**

## 2. Base Knowledge Object

A knowledge object should be interpretable through the following base concerns where relevant:

- **Identity** — what object, proposition, procedure, model, or normative statement is being discussed.
- **Provenance** — where the information came from and how its lineage can be inspected.
- **Epistemic state** — what the owning domain currently claims about support, uncertainty, contestation, or admission.
- **Scope** — where, for whom, or under what assumptions the object applies.
- **Time** — when the object, source, classification, or applicability is valid.
- **Relations** — typed relationships to other objects.
- **Authority** — which domain, if any, may admit, mutate, execute, or act on the object.

These base concerns are distinct from the five descriptive dimensions below.

## 3. Five Orthogonal Dimensions

### 3.1 Stability / Foundational

Describes how stable, mature, or foundational a proposition is within a declared scope.

Examples include well-established mathematical, physical, chemical, biological, logical, or engineering knowledge.

Rules:

- high stability != eternal truth
- stability != Native Kernel invariant
- stability != epistemic admission
- stability classification must retain scope, provenance, and revision possibility

The term **Invariant Knowledge** is intentionally avoided because `invariant` has a stronger architectural meaning in Native Kernel.

### 3.2 Variance / Contextual

Describes alternatives, disputes, temporal change, competing models, scoped validity, or unresolved positions around a knowledge object.

Useful typed relations may include:

- `SUPPORTS`
- `CHALLENGES`
- `QUALIFIES`
- `SUPERSEDES`
- `CONTRADICTS_CANDIDATE`
- `ALTERNATIVE_MODEL`
- `SAME_TOPIC`

Rules:

- variant != false
- disagreement != resolved contradiction
- relation != truth
- one universal Observed -> Believed -> Validated -> Canonical ladder must not be imposed across Crystal, Titan, and Soul

Each owning domain retains its own epistemic state machine and authority.

### 3.3 Practical / Procedural

Describes how knowledge can be used, performed, built, diagnosed, or verified in practice.

A procedure may contain:

- goal
- prerequisites
- required inputs/materials
- required tools
- environment
- ordered steps
- decision points
- constraints
- safety conditions
- failure modes
- diagnostics
- verification criteria
- expected outputs
- provenance

Rules:

- procedure != fact
- procedure != guarantee
- procedure != permission to execute
- successful precedent != universal rule
- simulation != real-world validation

### 3.4 Perspective Model

Describes how relevance, affordances, constraints, or interpretation may differ for an observer, organism, role, community, or system.

A Perspective Model may contain:

- `subject_or_model_target`
- `object_ref`
- `evidence_basis`
- `observable_relevance`
- `inferred_relevance`
- `uncertainty`
- `limitations`
- `provenance`
- `prohibited_inferences`

Rules:

- perspective model != perspective itself
- model of another perspective != access to subjectivity
- inferred relevance != observed experience
- perspective attribution must remain explicit
- prohibited inferences should be represented where useful

Example: observations may support that a tree provides nesting or perching affordances for a bird; they do not by themselves justify a claim about the bird's subjective aesthetic experience.

### 3.5 Purpose / Normative

Describes why knowledge matters relative to a declared goal, value system, responsibility, or normative frame.

Examples may include guardianship, dignity, regenerative design, bio-centric analysis, safety, sustainability, or a user-declared objective.

Rules:

- purpose != evidence
- purpose != truth
- normative preference != empirical conclusion
- values may influence priorities, questions, trade-offs, and decisions, but may not rewrite evidence

A useful decision separation is:

```text
EVIDENCE -> REASONING -> FACTUAL POSITION
                            |
                  +---------+---------+
                  |                   |
               PURPOSE            CONSTRAINTS
                  |                   |
                  +---------+---------+
                            |
                         DECISION
                            |
                     AUTHORITY CHECK
                            |
                          ACTION
```

## 4. Classification Is Itself a Claim

Assigning a dimension or classification is not a privileged meta-truth.

For example, saying that an object is `high-stability` or that a particular perspective is relevant is itself a claim that may require:

- object reference
- dimension
- classification/value
- scope
- rationale
- provenance
- uncertainty/confidence where applicable
- asserting actor/domain
- assertion time
- status/revision history

Therefore:

- classification != truth
- classification may be contested
- classification may be revised without erasing its history

## 5. Cross-Project Relationship

The five dimensions are cross-cutting vocabulary. They do **not** create ownership of a dimension by a project.

Existing domains retain their documented responsibilities:

- **Crystal** — evidence, provenance, admission, trusted memory, bounded canonical writes.
- **Titan** — execution, tools, providers, orchestration, product composition, practical use and research infrastructure.
- **Native Kernel** — technology-neutral semantic invariants and conformance obligations.
- **Mentaury Soul** — cognition, claims/beliefs, self/identity, relationships, commitments, character, and normative interpretation within its authority.
- **Continuum** — research into functional process continuity across inference/context/runtime replacement.
- **Mentaury Kernel** — cross-domain composition specification, provenance preservation, declared loss, compatibility, and non-escalation.
- **Knowledge Atlas / System OS** — navigation and ecosystem-level orientation; not runtime authority.

A project may produce, store, consume, or interpret knowledge carrying any of the five dimensions when that operation is inside its existing authority.

## 6. Non-Conflation Rules

The following rules are normative for this vocabulary:

```text
dimension != epistemic status
classification != truth
classification itself == contestable claim
stable != Native Kernel invariant
stable != eternal truth
variant != false
practical != permission to execute
perspective model != subjectivity
perspective relevance != observed experience
purpose != evidence
purpose != truth
normative preference != empirical conclusion
retrieval != evidence
relation != authority
reasoning result != admission
knowledge semantics != authority domain
shared vocabulary != shared ownership
integration != authority transfer
```

Existing project-specific non-conflation rules remain authoritative in their owning domains.

## 7. Infrastructure Is Not the Knowledge Architecture

Mechanisms such as BM25/BM25F, embeddings, RRF, GraphRAG, causal graphs, vector stores, retrieval routers, Facts Packs, consolidation workers, or multi-scale/fractal representations are supporting mechanisms.

They may discover, retrieve, rank, connect, summarize, or maintain candidates, but they do not become truth or authority merely by doing so.

```text
KNOWLEDGE OBJECTS
       |
  +----+----+----------------+
  |         |                |
 BM25   embeddings          graph
  |         |                |
  +---------+----------------+
            |
         RETRIEVAL
            |
        CANDIDATES
            |
      domain-specific
      evidence/admission/
      cognition/execution
```

## 8. Example: Tree

One object can carry all five dimensions at once:

- **Stability:** biological organism, photosynthesis, vascular structure, with explicit scientific scope.
- **Variance:** taxonomy, local conservation status, climate-specific growth, competing ecological models.
- **Practical:** cultivation, forestry, construction use, disease treatment, verification and safety procedures.
- **Perspective:** human, bird, insect, forester, ecosystem, or cultural perspective models with explicit attribution and uncertainty.
- **Purpose:** biodiversity protection, harvesting, restoration, cultural preservation, or another declared goal/value frame.

The dimensions therefore describe coordinates of one knowledge object; they are not sequential stages.

## 9. Versioning and Change

This document is intentionally small and cross-project.

Changes should preserve these constraints:

1. Do not create a new runtime or authority domain from this vocabulary without a separate explicit architecture decision.
2. Do not silently redefine existing project authority.
3. Do not use `Stable` as a synonym for Native Kernel `Invariant`.
4. Do not allow Purpose to alter factual evidence.
5. Do not represent a Perspective Model as direct access to another subject's experience.
6. Do not allow Practical knowledge to imply execution authority.
7. Treat classification changes as versioned claims rather than destructive overwrites.

## 10. Summary

Velantrim Knowledge Semantics is a shared vocabulary of five orthogonal dimensions over existing authority domains:

```text
Knowledge Object
├── Stability / Foundational
├── Variance / Contextual
├── Practical / Procedural
├── Perspective Model
└── Purpose / Normative
```

It adds a common language for describing what knowledge means, how stable or contested it is, how it can be used, how relevance changes across perspectives, and why it matters — while preserving the existing boundaries between evidence, cognition, execution, semantic law, continuity, composition, and authority.