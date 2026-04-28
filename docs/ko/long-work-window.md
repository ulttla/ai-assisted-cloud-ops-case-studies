# Long Work Window

## 개요

Long Work Window는 AI-assisted engineering work를 여러 시간 동안 진행하기 위한 supervised execution block입니다.

목표는 단순히 오래 돌리는 것이 아닙니다. 긴 작업이 scope를 잃지 않고, 중간 상태가 보이고, 검증 가능한 결과를 남기며, 필요할 때 안전하게 중단되거나 재개될 수 있게 만드는 것입니다.

## 왜 필요한가

짧은 AI coding session은 데모하기 쉽습니다. 하지만 실제 작업은 여러 파일, 여러 검증 단계, 배포 여부 판단, 문서화, 다음 작업 handoff까지 이어지는 경우가 많습니다.

Long Work Window는 이런 문제를 다룹니다.

- 작업 목표가 흐려지는 문제
- 첫 작은 수정 후 조기 종료되는 문제
- validation을 잊는 문제
- review 없이 publish나 deploy로 넘어가는 문제
- 긴 작업 후 무엇이 바뀌었는지 설명하기 어려운 문제

## 기본 구조

| 단계 | 설명 |
|---|---|
| Start | scope, primary/secondary/fallback, hard stop, evidence target 고정 |
| Execution | 다음 check-in까지만이 아니라 남은 window 전체 기준으로 작업 |
| Check-in | 30분 단위로 의미 있는 진척, blocker, 다음 작업 공유 |
| Review | 긴 window에서는 별도 review 또는 challenger 관점 투입 |
| Validation | 완료 선언 전 최소 의미 있는 test, build, smoke, inspection 수행 |
| Closeout | 완료, 미완료, 변경 파일, 검증 결과, 남은 위험, 다음 액션 기록 |

## 안전 기준

Long Work Window는 자율 배포 장치가 아닙니다.

다음 작업은 사람 승인 없이 진행하지 않습니다.

- external publishing
- deployment
- credential handling
- destructive cleanup
- runtime restart or config change
- version update

## 좋은 closeout

좋은 closeout은 다음 질문에 답해야 합니다.

- 무엇이 바뀌었는가?
- 어떤 검증을 했는가?
- 어떤 reviewer 또는 challenger 관점이 있었는가?
- 남은 risk는 무엇인가?
- 다음 사람이 바로 이어서 할 수 있는 첫 행동은 무엇인가?

이런 기록이 있어야 긴 AI-assisted work가 단순한 채팅 로그가 아니라 재사용 가능한 engineering evidence가 됩니다.
