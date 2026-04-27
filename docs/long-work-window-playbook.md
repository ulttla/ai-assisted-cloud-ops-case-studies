# Long Work Window Playbook

## Purpose

A Long Work Window is a structured execution block for deep AI-assisted engineering work. It is designed to keep long-running work moving while preserving progress visibility, validation, and a clean closeout.

## Why it exists

Long AI-assisted sessions can drift if they do not have a clear rhythm. Common failure modes include:

- starting with a vague goal
- ending early after the first small task
- losing track of validation
- forgetting to document decisions
- publishing or deploying without a final approval gate

The Long Work Window model prevents this by making the window own the rhythm while the project owns the goal.

## Operating model

| Phase | Description |
|---|---|
| Start | Fix scope, primary/secondary/fallback queue, expected evidence, and hard stop. |
| Execution | Work against the full remaining window, not only the next check-in slot. |
| Check-ins | Report material progress every 30 minutes without forcing artificial task boundaries. |
| Midpoint challenge | Add a different review or smoke perspective for longer windows. |
| Validation | Run the smallest meaningful test/build/inspection gate before claiming success. |
| Closeout | Record completed work, incomplete work, evidence, risks, and next actions. |

## Example 5-hour structure

```text
T+0:   start, scope, queue, evidence target
T+30:  first check-in, confirm visible delivery
T+60:  primary artifact checkpoint
T+150: midpoint challenger / replan
T+240: validation and public-readiness pass
T+295: 5-minute warning
T+300: closeout with evidence and next action
```

## Closeout minimum

- completed / not completed
- changed files or artifacts
- validation result
- reviewer or challenger findings
- agreement/disagreement and adoption reason
- public release status
- next action

## Public portfolio framing

A Long Work Window is not just “working for five hours.” It is a repeatable operating pattern for turning ambiguous, multi-step AI-assisted work into a delivery package that can be reviewed, resumed, or safely stopped.

## Safe boundaries

Do not use the public playbook to expose internal channel names, approval shortcuts, runtime paths, account identifiers, or exact automation schedules.
