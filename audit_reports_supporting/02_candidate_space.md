# Audit: Candidate Space / Evidence (Velantrim Working Master)

Scope note: my read covers the full document (front-layer relationship map, the research round, the person/user-model boundary, the semantic-clarification-after-adversarial-review section, and the 33-section legacy layer). Section/topic names are used as locators since the export's line numbers are an artifact of extraction, not the document's own addressing.

The document does substantially better on candidate-space discipline than a typical "A≠B slogan wall" — several guardrails carry real positive content (what retrieval *is for*, what rank *actually orders*, a genuine necessary-condition test for compression). But the discipline is uneven: it is well-developed for *expansion* of the candidate space and for *passive* compression of already-settled understanding, and conspicuously thin for *contraction* of the live candidate set — exactly the region where "pruning laundering" (a candidate quietly dropped for resource/staleness/fit reasons later functioning as if refuted) could occur without ever tripping an explicit rule.

---

## Finding 1 — Expansion has a worked mechanism; contraction has none

**SOURCE:** The "dry terrain" example (Thinking↔Relations edge) walks through an actual expansion event: observing dry grass and damaged trees, the fast-grasp connection ("dry vegetation ↔ lack of water") is explicitly said to be only one candidate among rainfall deficit, soil properties, salinity, disease, fire, human activity, seasonality, "or a combination of factors," and thinking's job is to "distinguish competing STRUCTURES of connections and ask which observation would tell one from another." Analogy is separately given a generative role: "ANALOGY → CANDIDATE UNDERSTANDING." By contrast, the "Alternatives and Stopping" material (semantic-clarification section) and the legacy STOP language treat contraction only as a bare list of possible reasons (sufficiency, resource limits, unavailable source, external interruption, authority boundary) with no worked scenario showing what a contraction event actually looks like, what gets recorded, or what would prevent that record from reading as refutation later.

**INFERENCE:** The document gives expansion a rich, concrete generative account (analogy, counterexample-seeking memory queries, structural-alternative generation) but gives contraction only an abstract disclaimer. This is exactly the "expansion gets mechanism, contraction gets a warning label" asymmetry the brief asked me to check for.

**COUNTEREXAMPLE (resource-bounded inquiry):** A safety incident investigation generates five candidate root causes in week one (analogous to the dry-terrain expansion). Over the following weeks, three are silently deprioritized as the investigator's attention narrows under deadline pressure — not because any one of them was discriminated against, but because there was no worked "how do you contract responsibly" procedure to follow, only a reminder that contraction *shouldn't* misrepresent itself. Nothing in the document tells the investigator what a well-formed contraction record looks like, so nothing distinguishes their week-4 report from one where the three causes were actually ruled out.

**VERDICT:** partially survives — the general prohibition exists, but with no positive procedural content, so it survives as an aspiration rather than as an operative discipline.

---

## Finding 2 — "CANDIDATE SELECTION" is a named pipeline step with zero specified criteria

**SOURCE:** Retrieval section: "BROAD ORIENTATION → CANDIDATE SELECTION → TARGETED REREAD/SOURCE REPLAY → UPDATED MODEL... RETRIEVAL ≠ EVIDENCE, RANK ≠ AUTHORITY, NOT RETRIEVED ≠ ABSENT, COVERAGE ≠ COMPREHENSION."

**INFERENCE:** This is actually the reverse failure mode from an empty guardrail — it's an *empty positive step*. "CANDIDATE SELECTION" sits in the pipeline as if it were a specified mechanism, but nothing says what it optimizes for (recall vs. precision vs. hypothesis-type diversity), and none of the four adjacent guardrails constrain it either — they constrain what candidate status *doesn't* license (authority, evidence, absence, comprehension), not what candidate selection must actually do to be adequate. A system could satisfy the formal four-step pipeline with an arbitrarily narrow or biased selection and violate no stated rule. This is the finite-selection-process-mistaken-for-a-world-claim pattern: the pipeline's own name ("candidate space") implies breadth has been achieved, while nothing enforces that.

**COUNTEREXAMPLE (institutional/legal case reasoning):** A discovery process for a lawsuit runs BROAD ORIENTATION → CANDIDATE SELECTION and selects only documents matching the plaintiff's already-stated theory (keyword bias). TARGETED REREAD/SOURCE REPLAY faithfully operates on that narrowed set, and UPDATED MODEL is produced. The pipeline completed all four named steps correctly; the substantive failure (a biased candidate space) is invisible to the process as specified, because "candidate selection" was never given an adequacy criterion.

**VERDICT:** rejected as currently specified — NO NEW PRIMITIVE REQUIRED, but the existing step needs an actual adequacy criterion (even a soft one, e.g., "selection must not be filtered by the leading hypothesis alone") rather than remaining a bare label between two guardrail lists.

---

## Finding 3 — Pairwise support/exclusivity between candidates is named, never specified

**SOURCE:** The relation-type taxonomy (Thinking↔Relations) lists "ПОДДЕРЖКА/ОПРОВЕРЖЕНИЕ — что усиливает или ослабляет конкретную гипотезу?" (support/refutation — what strengthens or weakens a specific hypothesis) as one bullet among thirteen. Separately, "Strength of connection" lists as a factor "what alternative explanations give the same picture" without saying what follows from that.

**INFERENCE:** The document names the *category* of pairwise evidential relations between candidates but never specifies: whether two candidates under the same question are mutually exclusive, compossible, or independently scoped; whether evidence for A is ever treated as counting against B; or what "weakens a hypothesis" cashes out to beyond the already-established "counterexample may outweigh many confirmations" rule (which is about a single hypothesis's own support, not inter-candidate relations). This is squarely "gestured at, not specified."

**COUNTEREXAMPLE (formal mathematics):** A proof search holds two competing lemma candidates, L1 and L2, both consistent with the same set of confirmed sub-results. A new sub-result confirms a consequence of L1. Nothing in the document says whether this should lower confidence in L2 (if L1 and L2 are exclusive under the current axioms) or leave L2 untouched (if they're compatible specializations). The taxonomy names "support/refutation" as a relation type but gives no rule for resolving this case either way.

**VERDICT:** rejected — the gap is real; NO NEW PRIMITIVE REQUIRED, but "support/refutation" needs to be paired with an explicit statement of what exclusivity or independence between two live candidates would even mean before the relation-type label does any work.

---

## Finding 4 — "Competing variants" vs. "different bounded views" is never disambiguated, creating an escape hatch from genuine discrimination

**SOURCE:** Situation Model section: "the model may have several competing variants if evidence doesn't allow choosing one," immediately followed by "the same source may give different correct bounded views under different questions. VIEW A ≠ VIEW B, but neither automatically becomes SOURCE REALITY or UNIVERSAL STATE."

**INFERENCE:** These two sentences sit back-to-back but describe logically different situations — genuinely exclusive candidates awaiting discrimination, versus non-competing views that are each valid under different scopes and require no discrimination at all. The document never states the test for which situation you're in. This matters directly for candidate-space discipline: relabeling an uncomfortable, unresolved conflict between two exclusive candidates as "just two different bounded views" would let a system exit the STOP≠RESOLUTION discipline without ever performing the alignment procedure the Contradictions section (legacy §10) actually specifies (align object/context/time/scope/conditions/role, then classify as contextual difference vs. contradiction). Nothing forces that alignment check to run before a "competing variants" situation gets quietly reclassified as "just different views."

**COUNTEREXAMPLE (institutional/legal case reasoning):** Two witnesses give incompatible accounts of who arrived first at a scene. Both are internally coherent. A system under resource pressure could resolve the discomfort by declaring "witness A's account is View A, witness B's is View B, under different perceptual scopes" — never running the alignment check that would have shown these are actually the *same* object/time/scope and therefore a real contradiction requiring provenance-preserving resolution, not a costless dual-view escape.

**VERDICT:** partially survives — the Contradictions section (§10) does supply the missing alignment procedure elsewhere in the legacy layer, so the tool to prevent this exists in the document; it is simply never cross-referenced from the Situation Model passage where the ambiguity is introduced, leaving the escape hatch open at the point where it's most tempting to use.

---

## Finding 5 — Sufficiency of the candidate space is never given a criterion; the document itself names the blind-spot risk without resolving it

**SOURCE:** "Sufficient or deepen": "the goal is not always maximum depth, but minimally sufficient depth without losing differences capable of changing the conclusion... if the system mistakenly decided NOT to deepen, it will often never know what it missed... the depth decision is tied to blind errors that may leave no trace."

**INFERENCE:** The stated sufficiency criterion — "no undiscovered difference would change the conclusion" — is intensional and self-referentially unusable: by definition the system cannot check whether an uninvestigated candidate would change the conclusion without investigating it. The document is unusually honest here (it names the blind-spot problem explicitly, in its own words, rather than glossing over it), which is a real strength relative to a document that simply asserted "system decides when enough is enough." But the honesty doesn't supply a criterion — it just documents that none exists. "Sufficient for now" has no content beyond "we decided to stop," i.e., it does collapse into convenience, and the document says so about itself.

**COUNTEREXAMPLE (resource-bounded inquiry):** A fraud-detection system reviews a transaction, considers three candidate explanations (error, coincidence, fraud), and stops because none of the three is contradicted and further review would blow the SLA. The "minimally sufficient depth" criterion cannot tell this system whether a fourth candidate (collusion between two accounts, never generated because no analyst thought of it) would have changed the conclusion — the sufficiency test is vacuously satisfied by the *existing* candidate set regardless of what's missing from it.

**VERDICT:** unresolved — correctly identified as unresolved by the document itself; I count this as the document's own admission rather than a hidden gap I'm the first to surface, which is worth noting as intellectual honesty. NO NEW PRIMITIVE REQUIRED — but also no existing distinction currently closes it either.

---

## Finding 6 — The central stress test IS honored, with a real test, but only for settled compression — not for live-candidate contraction

**SOURCE:** Semantic-clarification section: "COMPRESSION ALONE MUST NOT SILENTLY INCREASE EPISTEMIC STRENGTH. Compression by itself does not get the right to turn 'in this episode the prediction failed' into 'the mechanism is refuted altogether,' or 'no exceptions found' into 'there are no exceptions.' If the result becomes epistemically stronger, a separate reason for that strengthening must exist — not merely the disappearance of scope, uncertainty, alternatives, or provenance."

**INFERENCE:** This is genuinely a *test*, not just an aspiration: it states a necessary condition ("a separate reason must exist") that could actually be checked against a specific compression event, and it explicitly names the exact shortcut it forbids (strength increasing merely because qualifiers vanished). This is the strongest, most operational form the "contraction must not increase epistemic strength" principle takes anywhere in the document — full credit for this being a real discipline, not an empty slogan. However, it is framed entirely around *compression of an already-settled record* (an episode, a rule, an exception-search result). It is never explicitly extended to the sibling case the brief is centrally concerned with: an *active candidate* dropping out of current consideration (via STOP, via "not currently the focus," via Essence choosing not to carry it forward) and later being treated as if excluded on the merits. The "Alternatives and Stopping" guardrails (NOT ACTIVE ≠ FALSE, NOT CURRENTLY INVESTIGATED ≠ EXCLUDED) address *status* confusion (active/inactive vs. true/false) but never state the evidentiary-weight version of the same worry — that deprioritization itself should carry zero evidentiary weight against the candidate.

**COUNTEREXAMPLE (medical/diagnostic reasoning):** A differential diagnosis initially includes autoimmune, infectious, and neoplastic causes for a patient's symptoms. Each visit, time pressure causes the clinician to run the workup for whichever cause currently seems most likely and simply not re-raise the others. After several visits, the chart's problem list quietly stops mentioning the neoplastic candidate at all — not because any test excluded it, but because it was never the visit's focus (STOP for resource/attention reasons each time). A later reviewer reading the chart sees no record explaining *why* the candidate disappeared, and treats its absence as if it had been ruled out. The compression test in the document (743) would catch this if it were applied — "the result became stronger (candidate silently dropped) without a separate reason existing" — but nothing wires that test into the STOP/deprioritization pathway; it is stated only for compression of settled records.

**VERDICT:** survives with scope — fully sound and operational for compression of settled understanding; unresolved for the specific candidate-space-contraction case that is this audit's central target.

---

## Finding 7 — The exclusion-scoping rule is a genuine positive account, but the document's own trace mechanism doesn't operationalize it

**SOURCE:** "Alternatives and Stopping": "exclusion of an alternative must be limited to the scope and grounds that actually discriminated it" — this is a real, substantive rule (not an empty A≠B), since it says what licenses exclusion (specific discriminating grounds) and bounds its reach (only that scope). Compare this to the document's actual persistence mechanism for handling loss under compression, "ESSENCE + TRACE" (Understanding↔Expectation edge): the reopen checklist there asks retroactively "what was the essence derived from; what cases supported it; what conditions were then present; what exceptions were known; what was discarded during compression; **what alternatives were then considered**; what has changed since" — note it asks *which* alternatives were considered, but not *why* or *under what scope* each was dropped.

**INFERENCE:** There is a real mismatch between a requirement stated in one place (exclusion must carry its discriminating scope/grounds) and the concrete mechanism built elsewhere to preserve exactly this kind of information (the trace/reopen checklist), which does not actually capture scope-of-exclusion as a first-class item — only "which alternatives existed," not "on what specific grounds, valid over what specific scope, was each one dropped." A reopen event using the document's own checklist would recover the *list* of past alternatives but not the *discriminating basis* the exclusion rule requires be preserved.

**COUNTEREXAMPLE (formal mathematics):** A theorem-proving search discards candidate lemma L2 because it fails under an added regularity assumption R. The exclusion rule says this exclusion is valid only within the scope where R holds. Months later, someone drops assumption R for an adjacent problem and reopens the search using the trace checklist ("what alternatives were then considered") — the checklist recovers "L2 was considered" but not "L2 was excluded specifically because of R," so L2 is not automatically reinstated as live even though its exclusion's scope no longer applies. The specification (761) and the operational mechanism (489–500) are simply not the same list.

**VERDICT:** partially survives — the rule is sound; the mechanism meant to carry it through time under compression doesn't currently carry the specific datum the rule requires.

---

## Finding 8 — Diagnosticity is well-formed where it appears, but never wired into Retrieval or STOP, so a STOP can rest on confirmatory (non-diagnostic) evidence undetected

**SOURCE:** Understanding↔Expectation edge: "MATCHED EXPECTATION ≠ STRONGLY CONFIRMED UNDERSTANDING... an observation that would occur under almost any version gives less new understanding than one that actually separates one hypothesis from another," reinforced by diagnostic question 5 ("what observation would distinguish my understanding from a close alternative?"). Separately, UNKNOWN's differentiated taxonomy (semantic-clarification section) explicitly includes "evidence does not discriminate between live alternatives" as one of its named subtypes — a direct, correct import of the diagnosticity concept into the UNKNOWN material. By contrast, neither the Retrieval section (candidate selection/ranking) nor the "Sufficient or deepen"/STOP material ever mentions diagnosticity as a factor in deciding whether the candidate space is adequate or whether to stop.

**INFERENCE:** The concept is correctly built and correctly kept apart from mere expectation-matching in the place it was introduced (the expectation/observation loop) and correctly reused in the UNKNOWN taxonomy — genuinely consistent, not drifting, across those two locations. But it is never cross-applied to the two places where it would matter most for candidate-space discipline: (1) whether "candidate selection" in Retrieval should favor sources likely to discriminate between live candidates rather than merely sources that confirm the leading one, and (2) whether STOP should require that the evidence which triggered "sufficient" was actually diagnostic among the candidates still live at that point, rather than merely non-contradictory. Without that wiring, a system can satisfy every stated rule (retrieve, compress, stop) using evidence that only ever matched expectation and never discriminated anything, and the document's own vocabulary for catching exactly that failure sits unused two sections away.

**COUNTEREXAMPLE (medical/diagnostic reasoning):** Chest pain with elevated troponin matches the clinician's leading hypothesis (myocardial infarction) and the workup stops. Troponin elevation is also consistent with pulmonary embolism and myocarditis — it is non-diagnostic among the three live candidates. The document's own diagnostic-question 5 ("what observation would distinguish this from a close alternative?") would catch this immediately if it were required at STOP time; nothing in the "Sufficient or deepen" material requires asking it there.

**VERDICT:** partially survives — sound and non-circular where it lives; unresolved as a cross-cutting discipline because it isn't required at the two decision points (candidate selection, STOP) where its absence causes the most damage.

---

## Finding 9 — The candidate-pruning-laundering failure mode is independently reinvented in two disconnected parts of the document, without the insight propagating between them

**SOURCE:** (a) Semantic-clarification section, on compression (743, quoted above in Finding 6). (b) Person/User-model boundary section, open question 5: "How to avoid making personalization a self-confirming loop: the system shows the person only what matches the old model, and then treats their reaction to that narrowed choice as new confirmation of the model?"

**INFERENCE:** These are the *same structural failure* — a candidate (an interpretation, or here a user-preference/option) drops out of active consideration for non-evidential reasons (resource narrowing in one case, personalization narrowing in the other), and the drop's downstream effects get read back as confirming evidence. The document's own relationship-map architecture (explicitly not a pipeline, deliberately allowing each edge to be worked on somewhat independently) lets this pattern be *named* twice without either instance citing the other, and without either instance benefiting from the other's framing — the compression section has the sharper, more operational language ("a separate reason must exist"), but the personalization section, which is arguably the more concrete and higher-stakes instance (it names an actual feedback loop with an external human, not just an internal model), is left as an open question with no answer even alluding to the nearby fix.

**COUNTEREXAMPLE (user interaction / performative feedback):** A recommendation system stops surfacing a genre the user hasn't clicked in months (deprioritized as a "candidate interest" for attention-budget reasons — Finding 6's exact mechanism, applied to a person rather than a hypothesis). Because it's never shown again, the user never clicks it again. The system, applying nothing but its own stated compression rule, would be required to ask "is there a separate reason the model got stronger (interest ruled out) beyond the mere disappearance of the option?" — but because the compression discipline and the personalization open-question were never connected, the system that only reads the personalization section has no such rule to apply at all, and the self-confirming loop the document itself worries about proceeds unchecked.

**VERDICT:** partially survives — the failure mode is correctly identified twice, which is a real strength (it shows the map converges on genuine problems from different edges); but "not yet wired together" is exactly the self-sealing-loop risk the brief asked me to look for, and as written the fix available in one place doesn't reach the place that needs it most.

---

## Closing: what survives cleanly vs. what's genuinely broken

**Survives cleanly (not a real issue on inspection):**
- RANK ≠ AUTHORITY and RETRIEVAL ≠ EVIDENCE are *not* empty guardrails — both are immediately followed by a positive statement of what rank and retrieval actually do (order attention; form a candidate space), which is the right way to write this kind of rule and should be the template for the places that fail to do it.
- The UNKNOWN taxonomy (semantic-clarification section) is genuinely differentiated, not one bucket, and the document supplies a real self-test for keeping it that way ("does the distinction change what to do next — if not, the category may be superfluous"). This is a substantive, non-circular piece of method.
- Diagnosticity vs. matched-expectation is correctly and consistently maintained everywhere it is actually discussed (the expectation/observation loop and the UNKNOWN taxonomy do not drift from each other) — the problem is reach, not internal consistency.
- The compression-strength test (743) is a real necessary-condition test, not an aspiration — it names the specific illegitimate move (strength increasing merely from vanished qualifiers) and demands an independent justification.
- The dry-terrain example shows the document can and does give expansion of the candidate space genuine procedural texture when it wants to.

**Genuinely broken / unresolved:**
- Contraction of the candidate space (as opposed to compression of settled records) has no worked mechanism, no adequacy criterion, and no explicit "removal ≠ evidence against" statement at the evidentiary-weight level (only at the status level).
- "CANDIDATE SELECTION" as a named pipeline step carries no criteria of its own.
- Pairwise support/exclusivity between live candidates is named as a relation-type category and never operationalized.
- "Competing variants" and "different bounded views" are not disambiguated where the ambiguity is introduced, though the tool to fix it (the Contradictions alignment procedure) exists elsewhere unused for this purpose.
- Sufficiency of the candidate space collapses into "convenient to stop," which the document itself admits without resolving.
- The exclusion-scoping requirement (761) is not carried by the concrete trace/reopen mechanism built for exactly this purpose.
- The pruning-laundering failure mode is independently discovered twice (compression; personalization) without cross-reference, so the sharper fix in one place doesn't reach the more consequential instance in the other.
