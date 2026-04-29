# Communicating AI-Assisted Work

## 목적

AI-assisted engineering은 쉽게 과장되어 보일 수 있습니다. 이 문서는 model이 engineering judgment, review, accountability를 대체했다는 인상을 주지 않으면서 supervised AI workflow를 설명하는 public-safe 표현을 정리합니다.

## 좋은 framing

소유권, 검증, 경계를 강조하는 표현을 사용합니다.

- I used AI tools inside a supervised engineering workflow.
- I kept one accountable orchestrator for scope, decisions, and user-facing communication.
- I separated planning, implementation, review, fact-checking, and risk checks into distinct lanes.
- I validated changes before claiming completion.
- I kept human approval for publishing, deployment, credential handling, and destructive actions.
- I converted private operational work into sanitized public examples.

## 자율성 과장 피하기

Unattended production change처럼 들리는 표현은 피합니다.

| 피할 표현 | 더 나은 표현 |
|---|---|
| Fully autonomous production changes | Supervised, approval-gated execution |
| The AI handled the whole project | AI-assisted workflow with human review and final ownership |
| No human needed | Human-in-the-loop with explicit approval boundaries |
| Agent did everything | Multiple lanes contributed drafts, checks, and review evidence |
| Self-running deployment | Deployment remained approval-gated and validated |

## 가치 설명하기

강한 시그널은 AI를 썼다는 사실 자체가 아닙니다. 더 강한 시그널은 workflow에 guardrail이 있었다는 점입니다.

1. execution 전에 scope를 고정했습니다.
2. 긴 작업을 restartable chunk로 나눴습니다.
3. check-in으로 진행 상황을 보이게 했습니다.
4. review lane이 결과를 challenge하거나 verify했습니다.
5. test 또는 smoke check로 claim을 뒷받침했습니다.
6. closeout에 변경 내용, 통과한 검증, 남은 risk, 다음 액션을 남겼습니다.

## 예시 문장

> I use AI tools as part of a supervised engineering workflow. OpenClaw acts as the current orchestration layer, while specialized lanes handle planning, implementation, review, fact-checking, and risk checks. External or irreversible actions remain human-approved, and each non-trivial work window closes with validation evidence and next steps.

## 공개 경계

Workflow를 공개적으로 설명할 때 raw log, local runtime path, private account identifier, credential, internal channel name, approval shortcut, exact automation schedule은 포함하지 않습니다.
