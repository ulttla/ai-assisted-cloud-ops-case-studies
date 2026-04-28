# Communicating AI-Assisted Work

## Purpose

AI-assisted engineering is easy to overstate. This note captures public-safe language for explaining supervised AI workflows without implying that models replaced engineering judgment, review, or accountability.

## Good framing

Use language that emphasizes ownership, validation, and boundaries:

- I used AI tools inside a supervised engineering workflow.
- I kept one accountable orchestrator for scope, decisions, and user-facing communication.
- I separated planning, implementation, review, fact-checking, and risk checks into distinct lanes.
- I validated changes before claiming completion.
- I kept human approval for publishing, deployment, credential handling, and destructive actions.
- I converted private operational work into sanitized public examples.

## Avoid overstating autonomy

Avoid phrases that imply reckless unattended production changes:

| Avoid | Prefer |
|---|---|
| Fully autonomous production changes | Supervised, approval-gated execution |
| The AI handled the whole project | AI-assisted workflow with human review and final ownership |
| No human needed | Human-in-the-loop with explicit approval boundaries |
| Agent did everything | Multiple lanes contributed drafts, checks, and review evidence |
| Self-running deployment | Deployment remained approval-gated and validated |

## Explain the value

The strongest signal is not that AI was used. The strongest signal is that the workflow had guardrails:

1. scope was fixed before execution;
2. work was split into restartable chunks;
3. check-ins made progress visible;
4. review lanes challenged or verified the result;
5. tests or smoke checks supported claims;
6. closeout preserved what changed, what passed, what remained risky, and what should happen next.

## Example summary

> I use AI tools as part of a supervised engineering workflow. OpenClaw acts as the current orchestration layer, while specialized lanes handle planning, implementation, review, fact-checking, and risk checks. External or irreversible actions remain human-approved, and each non-trivial work window closes with validation evidence and next steps.

## Public boundary

Do not include raw logs, local runtime paths, private account identifiers, credentials, internal channel names, approval shortcuts, or exact automation schedules when explaining the workflow publicly.
