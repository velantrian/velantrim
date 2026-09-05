# velantrim

## 👤 What Velantrim is for

Velantrim is a cognitive-system research ecosystem aimed at helping AI **avoid starting from zero every time a conversation, task, or model changes**. Instead of treating one long transcript as memory, the system aims to preserve organized context: what happened, what it means, where information came from, what remains relevant, what changed, and which source should be reopened when more detail is needed.

The human-facing goal is simple: **less repeated explanation, less unnecessary rereading of long histories, faster context reconstruction, and more continuous work across chats, tasks, and replaceable AI models.**

```text
MESSAGES / DOCUMENTS / DECISIONS / EVENTS
                  ↓
        ORGANIZED CONTEXT + ESSENCE
                  ↓
        RELEVANT MEMORY / SOURCE
                  ↓
           AI CONTINUES WORK
```

A useful retrieval principle is:

`ESSENCE → DISCOVERY → SOURCE REOPEN`

Boundaries: **more data != better understanding**; **summary != source**; **retrieval != evidence**. This describes the human-facing system goal, not a claim that every end-to-end mechanism is already implemented or authorized in runtime.

## Ecosystem documentation

- [Velantrim Substrate-Neutral Architecture](docs/architecture/VELANTRIM_SUBSTRATE_NEUTRAL_ARCHITECTURE.md) — cross-project orientation for preserving semantic distinctions and obligations across replaceable implementation technologies. Not a runtime, Canon, or authority domain.
- [Substrate-Neutral Conformance Checklist](docs/architecture/SUBSTRATE_NEUTRAL_CONFORMANCE_CHECKLIST.md) — scoped verification aid for deciding whether a different implementation still preserves the same applicable semantic architecture. Not production or runtime authorization.
- [Velantrim Epistemic Firewalls — Meta-Family Compression](docs/architecture/VELANTRIM_EPISTEMIC_FIREWALLS.md) — eight core meta-families plus one research-governance family organizing the ecosystem's local `X != Y` non-conflation rules, validated as bounded-sufficient organizational compression. Does not license deleting local guardrails or claim architectural completeness.
- [Velantrim Cognitive System Vision v0.1](docs/vision/VELANTRIM_COGNITIVE_SYSTEM_VISION.md) — desired human-facing cognitive capabilities and North Star. Vision only; not architecture, runtime, or authority.
- [Velantrim Cognitive System Capability Audit v0.1](docs/research/COGNITIVE_SYSTEM_CAPABILITY_AUDIT.md) — documentation-based audit of how current projects can satisfy the Vision individually and collectively, with test-now guidance and simplification boundaries. Research audit only; not implementation authority.
- [Velantrim Knowledge Semantics v0.1](docs/knowledge/VELANTRIM_KNOWLEDGE_SEMANTICS.md) — cross-project vocabulary for Stability, Variance, Practicality, Perspective, and Purpose. Descriptive only; not a runtime or authority domain.
