# Substrate-Neutral Conformance Checklist

**Status:** Cross-project verification aid. Not Canon, runtime authority, production authorization, or a substitute for owning-project conformance rules.

Use this checklist when asking whether a new implementation, migration, storage model, programming language, AI model, database, graph, analog medium, neuromorphic substrate, or future technology still realizes the same Velantrim architecture for a declared scope.

## 1. Scope first

- What exact scope is being claimed equivalent?
- Which project owns the relevant semantics?
- Which obligations are applicable in that scope?
- Which obligations are explicitly out of scope?

No implementation may claim ecosystem-wide equivalence from a narrower test.

## 2. Distinction preservation

Verify that materially relevant distinctions remain representable and inspectable. At minimum consider:

- source != representation
- observation != claim
- claim != truth
- source != evidence
- evidence != belief
- belief != knowledge
- retrieval/relevance != epistemic validity
- unknown != false
- unsupported != false
- failure-now != impossible
- conflict detection != conflict resolution
- revision != overwrite
- supersession != deletion
- identity != byte equality
- capability != authority
- receipt != correctness/truth

If a substrate collapses an applicable distinction, mark the mapping `PARTIAL`, `UNSUPPORTED`, `INDETERMINATE`, or `LOSSY`; do not call it fully equivalent.

## 3. Scope, provenance, and authority

Check that the implementation preserves or explicitly translates:

- context/scope;
- time or ordering semantics;
- provenance and known provenance gaps;
- source attribution;
- authority role and domain;
- delegation/admission boundaries;
- lineage across revision, migration, fork, restore, or derivation.

A transfer that preserves content but drops material provenance or authority context is not full semantic preservation.

## 4. Outcome vocabulary

Where applicable, the implementation must distinguish meaningful non-success states rather than flattening them into `false`, `null`, empty output, or timeout.

Reference outcome family:

- `APPLIED`
- `NO_CHANGE`
- `QUARANTINED`
- `REJECTED`
- `PARTIAL`
- `UNKNOWN`
- `UNSUPPORTED`
- `FAILED`

Literal tokens are not mandatory unless an owning specification requires them. The semantic distinctions are.

## 5. Declared loss

For every material mapping, classify preservation using the appropriate owning vocabulary, such as:

- `PRESERVED`
- `PARTIAL`
- `UNSUPPORTED`
- `INDETERMINATE`
- `LOSSY`

Declared loss makes loss visible; it does not prove that the loss is acceptable.

## 6. Temporal and causal discipline

Verify that the implementation does not silently promote implementation order into world order or causality.

Preserve materially relevant differences among:

- occurrence order;
- observation order;
- write/commit order;
- dependency/causal order;
- semantic precedence.

A total execution order must not manufacture causal meaning where only a partial order is known.

## 7. Revision and history

A conforming implementation must preserve the required meaning of change:

- what changed;
- what was superseded;
- what remains unresolved;
- what was deleted or merely made unavailable;
- what lineage connects predecessor and successor states;
- what authority permitted the change.

Replay or append-only storage is not mandatory. Traceable semantic history is the obligation where applicable.

## 8. Cross-domain transfer

When meaning crosses project/domain boundaries, verify:

- provenance survives;
- scope survives;
- authority is not escalated;
- loss is explicit;
- receiving-domain interpretation does not rewrite source-domain truth;
- aggregate-derived-from-subject is not reused as independent evidence about that subject;
- receipt/transport success does not become truth, identity admission, consent, or action authority.

## 9. Project-specific projection

Check the owning project’s neutral projection:

- Crystal: candidate discovery != evidence admission != trusted write.
- Titan: artifact presence != configured != wired != executed != observed runtime behavior; orchestration != epistemic authority.
- Soul: claim != belief != self-model != identity != relationship state != action authority.
- Continuum: process state != one inference instance/context window; unknown continuity state remains explicit.
- Native Kernel: substrate-neutral semantic obligations and conformance.
- Mentaury-Kernel: cross-domain composition, declared loss, provenance, authority, non-escalation.

## 10. Verification evidence

A conformance claim should name:

- implementation/profile name and version;
- claimed scope;
- mapped obligations;
- realization or functional equivalent;
- preservation state per obligation;
- observable test/check or other evidence;
- known losses and uncertainties;
- excluded regions of equivalence;
- reviewer or verification procedure.

Same final answer alone is insufficient evidence of semantic equivalence.

## 11. Final classification

Use a scoped result such as:

- `FULL_CONFORMANCE_FOR_SCOPE`
- `BOUNDED_CONFORMANCE`
- `NON_CONFORMANT_FOR_SCOPE`
- `INDETERMINATE_CONFORMANCE`

These labels do not authorize production, safety, security, legal compliance, runtime activation, Canon promotion, or cross-domain mutation.

## Minimal decision rule

```text
If required distinctions + scope + provenance + authority + uncertainty + revision meaning are preserved
and material loss is explicitly bounded,
then a radically different technology may still be the same architecture for that scope.

If an applicable distinction is silently collapsed,
then identical outputs do not make it the same architecture.
```
