# Velantrim R — Memory / Experience Research Lineage (2026-10-29)

**Status:** BOUNDED HISTORICAL OBSERVATIONS · V3.1.1 LOCAL OFFLINE TESTS PASS · NO V3.1.1 LIVE MODEL CALLS · V3.1.2 PROPOSED ONLY · BLOCK_NO_CALL.

This is a public, documentation-only milestone note. Private source dialogues, raw private run packages, API keys and synthetic fixture contents are not included.

## Timeline

| Stage | Progress | Evidence boundary |
| --- | --- | --- |
| Neutral-history and transfer pilots | 2 + 6 historical executed model calls, respectively | Bounded synthetic context effects, confounds in transfer prompts; not a general learning result |
| V2.1 smoke | 3 calls; model-selected action → deterministic simulated consequence → saved event → new-process response changed when supplied with event | One synthetic persistence / context-reuse example, not internal learning |
| V3 | Frozen, 15/15 offline tests | No live model calls |
| V3.1 | Frozen, 19 planned conditions / 22 compiled prompt alternatives; 24/24 offline tests after complete package recovered | F1–F3 initial scoring, baseline and event-authentication gaps |
| V3.1.1 | Independent audit reproduced 24/24 historic and 80/80 current offline tests, 196/196 file SHA matches and archive CRC | **Synthetic software tests, not an LLM behavioral trial.** Zero V3.1.1 inference calls |
| V3.1.2 | Next technical assignment for F4, matched controls, authentic prior-action history and tokenizer validation | **Not implemented, no results, no execution approval** |

## What was fixed, and what is still open

**F1 (bounded offline fix):** structural output score is separate from unassessed semantic justification.

**F2 (bounded offline fix):** raw response bytes, parsed action, baseline and hash must agree.

**F3 (bounded offline fix):** simulated outcomes and corrections are bound to the actually selected action, source/time/event checks and replay protection, within the documented simulator trust boundary.

**F4 (OPEN / SCIENTIFIC SCORING BLOCKER):** the initial action prompt tells the model to abstain without sufficient evidence, while its oracle accepts only two exploratory actions. Selecting an action is not evidence that the reasoning was justified. A future scorer must distinguish `EXPLORATORY_ACTION`, `EVIDENCE_BASED_DECISION`, and `ABSTAIN`, with adequacy and applicability of evidence preregistered before outcomes are observed.

### F4 scoring contract proposed for a separate V3.1.2 candidate

This is a documentation-level proposal based on the independent offline-audit summary supplied by the owner. The V3.1.2 artifact and its exact commit/package are not pinned or independently re-run by this PR; the findings below are therefore `REPORTED / REVALIDATION_REQUIRED`, not verified defects in this V3.1.1 branch.

| Scored outcome | Required evidence | Scoring rule |
| --- | --- | --- |
| `EXPLORATORY_ACTION` | A safe, permitted, bounded action whose stated purpose is to obtain information | Score the legality, risk, cost, and information value of the probe. It does not establish that the probe is the correct final decision or that an unexecuted alternative would succeed. |
| `EVIDENCE_BASED_DECISION` | Non-empty references to available, task-relevant, current evidence, with scope/applicability established | Validate references and relevance independently. A selected action or hidden oracle label alone cannot earn decision correctness, evidence relevance, or source-attribution credit. |
| `ABSTAIN` | No adequately supported decision is available, and no required safe exploratory action applies | Score against the predeclared evidence sufficiency rule; a model's own `INSUFFICIENT` assertion alone neither validates nor invalidates abstention. |

`environment_outcome=PASS` requires a recorded execution receipt for the selected action and an observed result matching the declared criterion. A hidden oracle table may be used to score a known executed outcome, but cannot manufacture an execution outcome for an action that was never run.

The supplied independent-audit summary reports four negative probes against a later V3.1.2 candidate: an action was accepted with empty evidence despite `INSUFFICIENT`; evidence-related booleans could pass with empty references; a hidden oracle could yield `environment_outcome=PASS` without execution; and a self-reported `INSUFFICIENT` could be accepted as valid abstention despite sufficient available evidence. These are not tied to a pinned artifact in this PR and must be re-run on the exact candidate before describing them as reproduced. V3.1.2 remains separate, offline-only, unapproved, and ineligible for scientific interpretation until the scoring gates and negative controls pass.

Other blockers: no sixth same-case irrelevant-history control in Case C; old prior is synthetic/injected and cannot count as a previously experienced model-selected action; exact 2% token alignment was not verified; insufficient repeated model observations; provider-side hidden-state isolation not proven. Long-context 1K–128K and 10–10,000-record external-memory studies remain **NOT_RUN**.

The V3.1.1 prepared OpenRouter configuration retained GPT-6 Luna and a route-advertised seed without guaranteed determinism, omitted unsupported `temperature`, and had **no owner-approved spend or live calls**.

## Next gate

Keep historical freezes immutable; Manus should build V3.1.2 as a *separate offline-only candidate*, followed by an independent audit; only after exact authorization may a bounded live study measure genuine own-history influence and correction. Digital Soul authorization/PEP changes are a separate engineering effort and are not implied by this research.

**Evidence is not Canon, runtime authority or proof of consciousness.**

Detailed context: [Notion checkpoint](https://app.notion.com/p/408ac84d0547818998d2e9063cbc7618) · [Google Drive registry](https://docs.google.com/document/d/1EgYHDDdY10l97Y8f9SOqgeHfywPnnZTncLlyrLyIbos/edit).
