# Velantrim R — Memory, Experience and Evidence Boundary (2026-10-29)

**Research status: OBSERVED BOUNDED CONTEXT EFFECT / GENERAL ABILITY NOT ESTABLISHED / V3.1 LIVE NOT RUN.**

## What the executed synthetic pilots show

Several small model comparisons found that showing an applicable saved trial record changed the response versus controls without that record. In one V2.1 example, a model chose an action, a deterministic simulated environment assigned its consequence, that event was saved, and a fresh process explicitly shown the event selected another action. This demonstrates a **bounded external-record context effect**, not weight updates, self-learning or subjective experience.

A separate six-response Transfer Applicability Pilot matched its preregistered expected answers, but confounds restrict interpretation: an answer-bearing record ID in A, explicit scope/abstention rules in B, and a missing measured OLD_ONLY baseline before correction in C. Correctly formatted or oracle-matching responses are not proof of independent applicability discovery or belief revision.

## Prepared but NOT executed

- **V3:** Frozen offline candidate; no live model tests.
- **V3.1:** 19 planned diagnostic conditions, 22 frozen prompt variants and 24 offline unit tests reported by Manus, **no live model calls**. The currently shared partial source set allowed 21 tests to pass independently; three retrieval tests need the absent `retrieval_baseline.py`.
- **Long context:** 1K / 8K / 32K / 128K token plans only.
- **External memory:** 10 / 100 / 1,000 / 10,000 record plans only.

The proposed pilot budget of USD 0.10 has **not** been approved; actual provider/model/price are not selected. `BLOCK_NO_CALL` remains in effect.

## Open measurement problems

1. An arbitrary nonempty model-generated explanation may pass V3.1 scoring even when it is not meaningful. Evidence and action consistency are scored; semantic justification is not independently validated.
2. An immutable hash of stored baseline fields does not by itself verify that `baseline_answer` was parsed from the preserved raw response bytes.
3. Correction admission does not by itself authenticate a selected-action simulator event and its observed consequence.
4. Server-side context isolation, long-run repeatability, general applicability transfer, and the retrieval-versus-interpretation failure split remain unresolved.

## Follow-up gate

Maintain frozen versions unchanged. Independently reproduce the complete offline V3.1 package and address the three deficiencies in a separate V3.1.1 amendment. Only then, under an explicitly approved provider/model/budget, run a bounded T0 action → observed simulated consequence → persisted event → restart → new decision experiment with proper no-history, old-only, correction-only, old+correction, and sham controls. Scale prompt length and external record count **separately** only after the small causal pilot is valid.

**Not an assertion of consciousness, model-weight learning, digital personhood, Canon, runtime implementation, or production readiness.**

This public note contains no raw private Notion dialogue or private research artifacts. Primary historical run packages are kept in the owner-controlled experiment archive; evidence status should be verified there rather than inferred from this overview.
