# Example 1: Competitive Analysis

> **Command:** Compare CrewAI, AutoGen, and LangGraph and produce a structured report with recommendations.

---

## Original Command

```
Analyze the multi-agent frameworks CrewAI, AutoGen, and LangGraph.
Focus on architecture, agent communication, orchestration ability,
observability, and learning curve.
Produce a structured comparison report with recommended use cases.
```

**Task ID:** `JJC-20260220-003`  
**Issued at:** 2026-02-20 09:15:00

---

## Zhongshu Planning

Planning completed within 45 seconds.

**Plan**

| # | Subtask | Department | Notes |
|---|--------|----------|------|
| 1 | Architecture and communication research | Bingbu | Compare architecture, communication model, and code organization |
| 2 | Data collection and quantitative comparison | Hubu | Gather stars, contributors, issue response times, and release cadence |
| 3 | Developer-experience evaluation | Bingbu | Build quick-start examples and score docs plus learning curve |
| 4 | Final report writing | Libu | Consolidate data into a structured Markdown report |

**Estimated duration:** 25 minutes  
**Estimated tokens:** ~18,000

---

## Menxia Review

Review duration: 32 seconds.

### Round 1: rejected

**Reasons for rejection**
1. Observability was explicitly requested but had no dedicated evaluation step.
2. Subtasks 1 and 3 overlapped and should be merged.
3. The report needed explicit recommendation scenarios, not just comparison.

**Review note:** *"Analysis without recommendations is incomplete. Add recommendation scenarios and resubmit."*

### Round 2: approved

Updated plan:

| # | Subtask | Department | Change |
|---|--------|----------|------|
| 1 | Architecture + communication + observability research | Bingbu | Merged old 1 and 3, added observability |
| 2 | Quantitative data collection | Hubu | Unchanged |
| 3 | Comparison report + recommendation scenarios | Libu | Added final recommendation section |

**Review note:** *"The plan is workable. Bingbu must explicitly cover observability, and Libu must provide clear recommendations. Approved."*

---

## Department Outputs

### Bingbu: technical research (8 minutes)

```markdown
## Architecture Comparison

### CrewAI
- Architecture: role-based agents with sequential or hierarchical processes
- Communication: shared memory and task callbacks
- Observability: basic logging, no built-in dashboard
- Strength: very fast to learn and prototype
- Weakness: harder to debug and less flexible for complex orchestration

### AutoGen
- Architecture: conversational agents and group chat
- Communication: message-based
- Observability: optional AgentOps integration, no built-in dashboard
- Strength: natural for collaborative brainstorming
- Weakness: group chat is inefficient for strongly task-driven workflows

### LangGraph
- Architecture: state machine and graph-based flow
- Communication: state propagation over graph edges
- Observability: LangSmith tracing is available
- Strength: the most flexible orchestration model
- Weakness: steeper learning curve and more abstract concepts
```

### Hubu: quantitative data (3 minutes)

| 指标 | CrewAI | AutoGen | LangGraph |
|------|--------|---------|-----------|
| GitHub Stars | 24.3k | 38.5k | 12.1k |
| Contributors | 180+ | 350+ | 90+ |
| Latest version | v0.8.2 | v0.4.1 | v0.2.8 |
| Median issue response | 2 days | 3 days | 1 day |
| Documentation score | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Hello world time | ~5 min | ~15 min | ~25 min |

### Libu: report writing (6 minutes)

Libu consolidated the Bingbu and Hubu outputs into the final report structure.

---

## Final Memorial

**Memorial ID:** `JJC-20260220-003`  
**Total duration:** 22 minutes  
**Total tokens:** 15,800

### Summary

The system completed a three-dimensional comparison across architecture, quantitative metrics, and developer experience. Menxia rejected the first plan because observability and recommendation scenarios were missing, then approved the revised version.

### Recommended Use Cases

| Scenario | Recommended framework | Reason |
|------|----------|------|
| Rapid prototyping | CrewAI | Easiest onboarding and simplest API |
| Conversation-heavy collaboration | AutoGen | Best fit for multi-turn discussion |
| Complex workflow orchestration | LangGraph | Strongest support for state machines and branching |
| High-reliability execution | **Edict** | Built-in mandatory review and a real-time dashboard |

### Key Findings

1. Built-in review is still uncommon across mainstream frameworks.
2. Observability remains weak overall; LangGraph is strongest here because of LangSmith.
3. CrewAI is the easiest entry point, but its documentation depth is limited.
4. LangGraph is the most capable technically, but the onboarding cost is highest.

---

*Based on a real run. Metrics reflect a February 2026 snapshot.*
