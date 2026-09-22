# CCL
### Context Curation Ledger

**Open towards Team Collaborations & Contract Opportunities.**

Measures, prunes, and reorders context before it reaches an LLM — and logs the proof. CCL implements the Pruning & Distillation sub-discipline of context engineering: given more relevant retrieved content than fits a model's real token budget, it decides what survives, reorders survivors to counter positional attention decay, and records both the pruned and unpruned outcomes so the improvement is measured, not assumed.

## Why "Ledger"

Most context-engineering advice is qualitative — "keep prompts focused," "avoid dumping everything in." CCL's core value is the opposite: a real, logged account of exactly what was cut, what was kept, how many tokens each choice cost, and how the final answer scored compared to the unpruned baseline. The claim "curation improved this answer" is only an engineering fact, not a guess, because it's written down and comparable.

## Grounded in measured research, not assumption

Built directly on verified findings from Gupte et al. (2025), tested against `llama3.1:8b` specifically — the model this project and its sibling repos run on:

- Near-perfect accuracy (96-99%) under ~4k tokens; a real, measured 10-12% drop in source-attribution accuracy by 12k tokens
- Structured key-value formatting scores meaningfully higher (0.98) than prose (0.76) for getting the actual fact right, on this model specifically
- RoPE's attention decay means content placed in the middle of a context window is read less reliably than content at the start or end

## Status

| Component | Purpose | Status |
|---|---|---|
| `count_tokens()` | Real token measurement, not word-count guessing | ✅ Built, tested |
| `fit_to_budget()` | Prune retrieved chunks to a real, measured ceiling | ✅ Built, tested |
| `position_aware_order()` | Place highest-relevance chunks first/last, not buried mid-context | ✅ Built, tested |
| `comparison_log.py` | The actual proof — pruned and unpruned outcomes, scored and compared | ✅ Built, tested |

## In Production

As of the latest commit, CCL is genuinely wired into procurement-rag's query_vector_store() output via curate_chunks(), and verified working end-to-end inside O2A's live agent test — not just tested in isolation, proven inside the real, running system it was built for.

## Related projects

- [O2A: Observability, Orchestration, Agent](https://github.com/Cre8tiveStuff/O2A-Observability-Orchestration-Agent) — the agent this context ultimately reaches
- [procurement-rag](https://github.com/Cre8tiveStuff/procurement-rag) — the retrieval layer CCL now curates
- [ARC: Agentic Reasoning Chain](https://github.com/Cre8tiveStuff/ARC-Agentic-Reasoning-Chain) — sibling infrastructure governing *when* work happens; CCL governs *what fits* in a single call

---

💬 Building in the open — feedback, questions, and collaboration welcome.