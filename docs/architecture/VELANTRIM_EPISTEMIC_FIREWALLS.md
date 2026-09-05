# Velantrim Epistemic Firewalls — Meta-Family Compression

**Status:** Working synthesis. Bounded-sufficient organizational compression, validated by a dedicated stress-test round (MV-3) against the current relationship map. Not Canon, not a new cognitive-state primitive, not a new Engine, and not permission to delete a local guardrail that has its own independent failure mode.

## Why this exists

Across the Velantrim documentation set, many local rules take the shape `X != Y`: source is not evidence, unknown is not false, capability is not permission, and so on. Each rule guards a specific way reasoning silently drifts. As that list grows project by project, a real question follows: can these local firewalls be organized under a smaller number of general families without losing meaning?

A dedicated validation round (MV-3, following whole-map coherence in MV-1 and sufficiency-under-pressure in MV-2) tested exactly that. The goal was **organizational compression**, not formal derivation:

```text
ORGANIZATIONAL COMPRESSION != FORMAL LOGICAL DERIVATION OF EVERY LOCAL FIREWALL
META-FAMILY != PERMISSION TO DELETE A LOCAL DISTINCTION THAT HAS ITS OWN FAILURE MODE
```

The result: eight core meta-families plus one separate research-governance family organize the current set of local firewalls without material semantic loss, in the scope tested so far.

## The nine families

### MF-1 — Epistemic role / strength

**Meta-principle:** No silent epistemic promotion.

Source, representation, claim, evidence, belief, knowledge, confidence, consensus, retrieval result, inferred relation, and observation must not silently acquire a stronger epistemic status without additional grounds.

```text
SOURCE != REPRESENTATION != CLAIM != EVIDENCE != BELIEF != KNOWLEDGE
CONFIDENCE != EVIDENCE
CONSENSUS != TRUTH
RETRIEVAL != EVIDENCE
RELATION LABEL != PROVEN RELATION
INFERRED != OBSERVED
```

### MF-2 — Open-world absence / coverage

**Meta-principle:** Absence in a bounded search or representation is not absence in reality.

Unknown, unsupported, not-retrieved, not-represented, not-surfaced, no-residual-found, and no-known-counterexample must not become a global negative conclusion.

```text
UNKNOWN != FALSE
UNSUPPORTED != FALSE
NOT RETRIEVED != ABSENT
NOT REPRESENTED != ABSENT
NO RESIDUAL FOUND != REPRESENTATIONAL COMPLETENESS
NO KNOWN COUNTEREXAMPLE != APPLICABILITY ESTABLISHED
```

### MF-3 — Scope / applicability / materiality

**Meta-principle:** Local validity, sufficiency, or materiality is not global validity.

A conclusion, Essence, relation, pattern, stop basis, or materiality judgement stays bound to its question, context, scope, time, and conditions. Past fitness for one use does not get promoted to universal applicability.

```text
VALID IN ONE QUESTION / CONTEXT / SCOPE != AUTOMATICALLY VALID IN ANOTHER
BEST AMONG CURRENTLY CONSIDERED != NO BETTER UNCONSIDERED ALTERNATIVE
TASK-BOUNDED STOP != TRUTH / COMPLETENESS
```

### MF-4 — Transformation / provenance / loss

**Meta-principle:** A transformation must preserve or declare its origin, operation, and material loss; the act of transforming must not by itself increase epistemic strength.

Compression, aggregation, inference, derivation, corroboration, summarization/Essence, and revision may change representation, but they do not get to hide origin, uncertainty, lost distinctions, or manufacture a stronger claim merely by having transformed the input.

```text
COMPRESSION != AGGREGATION != INFERENCE != DERIVATION != CORROBORATION
ESSENCE != SOURCE
COMPRESSION ALONE MUST NOT SILENTLY INCREASE EPISTEMIC STRENGTH
```

### MF-5 — Authority / admission / action

**Meta-principle:** No silent authority escalation.

Understanding, recommendation, capability, goal, urgency, transport, integration, fallback, or simulation do not by themselves create permission, admission, or action authority.

```text
KNOWLEDGE != RECOMMENDATION != DECISION != AUTHORIZATION != ACTION
CAPABILITY != PERMISSION
TRANSPORT != ADMISSION
INTEGRATION != AUTHORITY TRANSFER
URGENCY != AUTHORITY
FALLBACK != PERMISSION
GOAL CONFLICT != AUTHORITY EXPANSION
```

### MF-6 — Identity / state / time / execution

**Meta-principle:** The same referent or intention is not the same state, version, episode, execution, or temporal position.

Identity, continuity, state, version, episode, simulation, execution, expectation, observation, and knowledge-time must stay distinguishable.

```text
SAME ENTITY != SAME STATE != SAME VERSION != SAME INTERACTION != SAME EPISODE
CONTINUITY != IDENTITY
SIMULATED != EXECUTED
EXPECTED != OBSERVED
WHEN HAPPENED != WHEN OBSERVED != WHEN LEARNED != WHEN INTERPRETED != WHEN UNDERSTANDING REVISED
WORLD TIME != KNOWLEDGE TIME
```

### MF-7 — Relation semantics / causal attribution

**Meta-principle:** Relation type, proof status, and causal attribution must not silently collapse.

Sub-family A (relation semantics): similarity, analogy, correlation, mechanism, causation, identity, condition, dependency, and other relation types are not interchangeable, and chaining a relation across steps does not guarantee its meaning survives.

Sub-family B (intervention attribution): a change observed after one's own action does not acquire the status of independent world evidence; self-caused, world-caused, measurement-caused, and mixed/unknown stay distinguishable.

```text
SIMILARITY != MECHANISM
CORRELATION != CAUSATION
ANALOGY != IDENTITY
OBSERVED AFTER MY ACTION != INDEPENDENT WORLD EVIDENCE
SELF-CAUSED != WORLD-CAUSED
MEASUREMENT EFFECT != WORLD CHANGE
```

### MF-8 — Operational selection / revision / finality

**Meta-principle:** Activation, selection, stopping, or revision state does not by itself set truth, exclusion, or finality.

Inactivity, deactivation, omission from current focus, stopping, or a new revision do not mean falsity, epistemic exclusion, final resolution, or that history disappeared.

```text
NOT ACTIVE != FALSE
NOT CURRENTLY INVESTIGATED != EXCLUDED
OPERATIONAL DEACTIVATION != EPISTEMIC EXCLUSION
REMOVAL FROM CONSIDERATION != EVIDENCE AGAINST
STOP != RESOLUTION
SAME STOP != SAME EPISTEMIC STATE
CURRENT UNDERSTANDING CHANGED != HISTORY DISAPPEARED
STABLE != IMMUTABLE
```

### RG-1 — Research / donor / implementation governance

This family is deliberately kept **separate from the eight cognitive-state families above** — it governs how donor phenomena and implementations are allowed to influence the architecture, not a state of cognition itself.

**Meta-principle:** An external phenomenon, analogue, or implementation is not a required cognitive law.

```text
DONOR != ARCHITECTURE
BIOLOGICAL PHENOMENON != DIGITAL REQUIREMENT
WORKING AI ANALOGUE != PROOF OF COGNITIVE NECESSITY
TECHNOLOGY != ARCHITECTURE
GOOD ANALOGY != NEW PRIMITIVE
PROBLEM != NEW MODULE
FIXTURE FAILURE != PRESELECTED SOLUTION
```

## Compression failure test

Before accepting the nine families as the organizing set, adjacent merges were attempted and rejected:

- **MF-1 + MF-5 fails.** Epistemic strength and action authority are independent axes: evidence can be strong without permission to act on it, and permission can exist alongside incomplete knowledge.
- **MF-2 + MF-3 fails.** "Not found / not represented" is a coverage problem; "true here, but not there" is an applicability/scope problem. They fail for different reasons.
- **MF-7 into MF-1 fails.** Relation and causal-attribution semantics carry a distinct intervention question — a post-action observation can be well observed and still not count as independent world evidence.
- **MF-8 into MF-2 fails.** Stop, deactivation, and revision are operational/temporal states, not merely an absence of data.
- **RG-1 into core cognition fails.** Folding research governance into cognitive state makes research governance look like a cognitive mechanism, which reintroduces the donor/implementation drift this family exists to block.

`NO SILENT EPISTEMIC PROMOTION` (MF-1) and `NO SILENT AUTHORITY ESCALATION` (MF-5) held up as the two strongest independent meta-boundaries under this test, but neither absorbs the rest.

## What this establishes, and what it does not

```text
META-COMPRESSION COMPLETE FOR CURRENT SCOPE != ARCHITECTURE COMPLETE
```

This organizational layer:

- **does** give the ecosystem's many local `X != Y` rules a shared, checkable home rather than an ever-growing flat list;
- **does not** formally derive every local firewall from the nine families;
- **does not** license deleting a local guardrail that is an executable, reviewable example of a specific failure mode — local guardrails remain useful precisely because they are concrete;
- **does not** claim the nine families are the final or only possible organization; a new primitive is only justified after a localized failure that the existing vocabulary cannot honestly express.

## Relationship to existing documents

This is an **organizing layer over already-documented firewalls**, not a replacement for them:

- The [Substrate-Neutral Architecture](VELANTRIM_SUBSTRATE_NEUTRAL_ARCHITECTURE.md)'s seven cross-project laws and the [Substrate-Neutral Conformance Checklist](SUBSTRATE_NEUTRAL_CONFORMANCE_CHECKLIST.md)'s distinction-preservation list are concrete instances that these families organize, mainly under MF-1, MF-3, and MF-6.
- The [Knowledge Semantics](../knowledge/VELANTRIM_KNOWLEDGE_SEMANTICS.md) non-conflation rules (its section 6) overlap most with MF-1, MF-2, and MF-5; that document's five knowledge dimensions are a separate, narrower vocabulary and are not superseded by this one.
- Owning projects (Crystal, Titan, Mentaury Soul, Continuum, Native Kernel, Mentaury-Kernel) keep authority over their own domain-specific firewalls; this document does not transfer or centralize that authority.

```text
SHARED META-ORGANIZATION != SHARED AUTHORITY
NINE FAMILIES != CLOSED TAXONOMY
```
