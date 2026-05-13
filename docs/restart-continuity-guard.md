# Restart Continuity Guard

## 60-second summary

A control-plane restart should not silently break the conversation that requested it. The restart continuity guard is a public-safe pattern for treating gateway or assistant restarts as reliability events: checkpoint first, preserve the handoff path, run the restart through the approved path, then verify the same user-facing workflow receives the continuation message.

## Problem

AI operator work often spans chat, tools, scheduled jobs, browser sessions, and repo state. If a service restart loses the active session context, the user may see a healthy process but a broken workflow.

Common failure modes:

- restart command succeeds but no continuation message returns;
- a CLI restart path bypasses the session handoff mechanism;
- delayed restart loses the pending restart notice;
- post-restart smoke checks verify only process health, not user-facing continuity.

## Public-safe pattern

1. Treat restart as approval-gated work.
2. Write a checkpoint before the restart.
3. Prefer a restart path that carries a continuation note or ticket.
4. Block restart paths that bypass chat/session handoff when used from a chat-bound workflow.
5. After restart, verify both process health and user-facing return.
6. Record evidence: what restarted, what message returned, what smoke checks passed, and what caveats remain.

## What this demonstrates

- runtime operations as part of AI engineering, not incidental admin work;
- continuity checks beyond simple service uptime;
- explicit separation between safe inspection and risky lifecycle changes;
- public-safe closeout evidence for operational changes.

## Recommended wording

Use:

> Designed a restart continuity guard so control-plane restarts preserve the active user workflow, require approval, and verify both service health and same-channel continuation before closeout.

Avoid:

> The assistant can restart itself anytime without risk.

## Related

- [Operator Resilience and Update Safety](operator-resilience-and-update-safety.md)
- [Hermes Secondary Operator Lane](hermes-secondary-operator-lane.md)
- [Public Release Evidence Pattern](public-release-evidence.md)
