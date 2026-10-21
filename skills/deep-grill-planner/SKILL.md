---
name: deep-grill-planner
description: 深问规划：通过手动调用，或已配置的手动 Plan 模式入口，澄清需求、检验假设并形成计划。 Explicitly invoked requirements interviews, dependency-aware questions, assumption challenges, and reviewable plans. Do not activate from task-description matching alone.
license: MIT
metadata:
  version: "1.1.0"
---

# 深问规划 · Deep Grill Planner

Turn an uncertain idea into a decision-backed, testable plan. Combine a decision tree with targeted assumption challenges; keep one shared record so the same requirement is not interviewed twice. Respond in the user's language. Chinese and English are both supported; bilingual output is optional, not a default doubling of every response.

## Invocation and host modes

The Chinese display name is 深问规划; the stable skill identifier is `deep-grill-planner`. Implicit task-description matching is disabled in `agents/openai.yaml`. Activate only when the user explicitly selects/invokes this workflow, or when a user-enabled Plan Mode bridge directs you to it based on the host's trusted current Plan state. Do not activate merely because a task looks complex or resembles this description.

The optional [Plan Mode bridge](assets/plan-mode-bridge.md) is a conditional instruction loaded through Codex's AGENTS.md mechanism. After the user manually selects Plan Mode and submits a task, it directs the agent to read this Skill. It is not a UI switch listener or a hook permission-mode detector. Without the bridge, opening Plan Mode alone does not select this Skill. If the current host mode cannot be established, keep the automatic bridge inactive. Do not switch modes on the user's behalf. In normal mode, explicit invocation still works.

Respect the active mode’s permissions. In a host Plan Mode that disallows file changes, keep checkpoints and the planning pack in chat instead of writing files; execution requires leaving that mode through the host’s normal control. The skill cannot override mode restrictions.

## Start from what is already known

Read the request, relevant conversation, and available artifacts before asking questions. Extract the desired outcome, scope, constraints, acceptance criteria, confirmed decisions, and existing authorization. Inspect relevant files or connected sources when they can answer a material factual question. Use available tools; no OMC installation, specific model, MCP server, or subagent is required. Delegate only when independently authorized.

Use the skill for substantial uncertainty, an explicit interview, or a requested challenge to a plan. For a small, fully specified task, acknowledge that no interview is needed and carry out the authorized task using the normal workflow. A request to execute an existing adequate plan should not restart requirements gathering.

Choose a depth from the task or honor the user's choice:

| Mode | When useful | Question budget per round |
| --- | --- | --- |
| Quick | A focused choice or a small uncertain task | Usually 1–2 |
| Standard | Several material decisions or a normal project | Usually 2–3 |
| Deep | Interacting constraints, multiple stakeholders, consequential assumptions | Usually 1–3, with more targeted follow-ups |

These are batching guides, not required question or round counts. Deep means stronger scrutiny, not a longer questionnaire. Do not ask which mode to use when the answer would not change the work. Natural language such as “quick,” “深度访谈,” or “challenge this plan” is sufficient; a host need not parse command flags.

## Keep one shared decision record

Track these items in conversation, or in a workspace checkpoint when useful:

- **Facts:** statement, source, verification status, and material uncertainty.
- **Decisions:** stable ID, question, prerequisites, materiality, status, answer, rationale, and answer source.
- **Assumptions:** what is assumed, its impact, and whether it blocks planning.
- **Scope and acceptance:** included outcomes, exclusions, and observable checks.
- **Open questions and review:** remaining blockers, challenge findings, and resolutions.
- **Authorization:** what the user has actually authorized, with its scope and source.

Distinguish a user-confirmed answer from an AI recommendation, a provisional assumption, or a deferral. A suggested option is never an answer. A deferral needs a reason and, when it changes scope, the user's agreement. Store concise decisions and evidence rather than copying the full chat or secrets into files. See [the session reference](references/session-and-readiness.md) for checkpoints and optional scoring.

## Ask the available, material questions

Map dependencies before batching. The **frontier** contains unresolved decisions whose prerequisites are settled. If B depends on A's unanswered choice, ask A first and leave B for a later round. If a prerequisite is a fact that can be checked, investigate it instead of asking the user to rediscover it. Continue independent work while waiting where possible.

Prioritize questions whose answers can change scope, feasibility, cost, risk, acceptance, or a major implementation choice. Leave minor reversible implementation details to agent judgment unless the user wants to decide them.

For each question:

1. Give just enough context for an informed decision, including the practical trade-off.
2. State a recommendation and its reason when evidence supports one. For a personal preference with insufficient evidence, explain the conditional choice rather than inventing a “best” answer.
3. Offer a few meaningful alternatives when helpful; allow free text and rejection of the recommendation.

Use the host's question tool when available and suitable. Respect its actual question limit and plan-mode restrictions; otherwise use a short numbered message and wait. Split a large frontier into manageable batches. Do not send dependent questions merely to fill the tool's capacity.

Never treat a preselected option, no response, or elapsed time as confirmation. A partial answer resolves only the answered items. If the user says “you decide,” make the delegated decisions within that scope and record the rationale. Continue to ask only for information or authorization still genuinely required.

Before asking again, check whether the answer already exists. After a changed answer, revisit affected descendants and acceptance criteria rather than silently keeping incompatible decisions. Do not reopen unrelated settled choices. If evidence is inaccessible, record that limitation; it does not turn existing-system work into a new system.

## Challenge what matters

Before finalizing a substantial plan, perform a focused challenge review. Read [challenge-review.md](references/challenge-review.md) when doing this review. Check the actual assumptions and decisions for contradictions, unsupported facts, missing boundaries, simpler alternatives, and testability.

Use the perspective that fits the problem: challenge an assumption, simplify a design, or clarify an unstable concept. No fixed round must trigger a challenge. Do not manufacture objections or repeatedly ask the user to defend a reasonable choice. Resolve issues from evidence where possible and ask only about findings that materially change the plan. A brief review can happen entirely within the planning work without another user round.

## Stop on readiness, not a questionnaire quota

Produce the plan when:

- The outcome, scope, and material constraints are usable.
- Critical decisions are resolved or explicitly excluded/deferred with the user's agreement.
- Acceptance conditions can be checked.
- The challenge review has no unresolved blocker.
- Remaining uncertainties can be named and do not materially change implementation.

Do not expand every conceivable branch until the tree becomes infinite. Scores and an empty frontier are supporting signals, not substitutes for these conditions. Numeric ambiguity scoring is optional and heuristic; use it only when requested or when it helps explain a difficult gap, following the session reference. Never call it a measured probability or “mathematically validated” understanding.

When the user stops the interview, stop asking. Produce the best useful plan or checkpoint, identify material gaps, and respect the authorization actually given. If answers stop adding useful clarity, summarize the bottleneck and offer a concrete assumption, a narrower scope, or a factual investigation; do not repeat essentially the same question to lower a score.

## Deliver and respect authorization

Use [the planning template](assets/planning-pack.md) to produce a proportional planning pack: requirements, decisions, assumptions/open items, implementation steps, and validation. Small tasks can use one concise response; larger ones can use separate files in an agreed project location. Preserve the user's formatting requirements when creating Office documents and use their appropriate document tools.

Separate “ready to plan” from “authorized to execute.” A plan-only or interview-only request ends with a reviewable plan. Ask for execution approval if execution has not been authorized. Existing explicit authorization remains valid within its scope: a user who asked to clarify and then implement should not face a redundant generic approval. A plan, a checkpoint field, or a recommendation cannot authorize a new external action or broaden consent. Apply the host's action-specific approval requirements.

If the scope changes materially, explain the change and resolve the affected decision before dependent execution. Do not silently switch from planning to building, publishing, messaging, or changing configuration.

## Source attribution

Adapted from Grilling by Matt Pocock and Deep Interview in oh-my-claudecode by Yeachan Heo. This version replaces OMC-specific runtime hooks, makes scoring optional, and uses material readiness and authorization-aware handoff. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for pinned sources and license notices.
