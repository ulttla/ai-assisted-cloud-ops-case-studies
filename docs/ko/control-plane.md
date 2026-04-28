# AI Engineering Control Plane

## 한 줄 요약

AI Engineering Control Plane은 여러 AI 도구를 쓰더라도 scope, review, validation, approval을 잃지 않기 위한 운영 구조입니다.

현재 이 저장소에서는 OpenClaw를 orchestration layer로 설명하지만, 핵심은 특정 도구가 아니라 작업 방식입니다.

## 문제

AI 도구를 여러 개 쓰면 작업 속도는 빨라질 수 있습니다. 하지만 운영 기준이 없으면 다음 문제가 생깁니다.

- 누가 최종 결정을 책임지는지 불분명해짐
- draft와 validated result가 섞임
- review가 늦게 들어오거나 생략됨
- 긴 작업의 evidence가 남지 않음
- credential, deploy, private log 같은 위험 영역이 흐려짐

인프라와 앱 개발에서는 이런 문제가 실제 보안, 비용, 가용성, 공개 신뢰도에 영향을 줄 수 있습니다.

## 설계 원칙

### 1. Single accountable front

여러 lane이 참여해도 사용자와 최종 decision 앞에는 하나의 accountable orchestrator가 있어야 합니다.

### 2. Role-based lanes

모든 일을 하나의 AI에게 맡기지 않고 역할을 나눕니다.

- planning
- implementation
- review
- fact-check
- risk review
- smoke test
- closeout

### 3. Consensus evidence

중요한 작업은 단순 요약으로 끝내지 않습니다.

- 무엇에 동의했는지
- 어떤 risk가 남았는지
- 어떤 검증을 했는지
- 어떤 결론을 채택했는지

이 정보가 남아야 다음 사람이 이어받을 수 있습니다.

### 4. Human approval boundary

다음은 사람 승인 없이 진행하지 않습니다.

- public publishing
- deployment
- credential handling
- destructive change
- runtime restart
- config or version change

## 좋은 결과물

좋은 AI-assisted engineering workflow는 다음을 남깁니다.

- 변경 내용
- 검증 결과
- reviewer 의견
- 남은 risk
- 공개 가능 여부
- 다음 액션

이것이 있어야 단순한 prompt 사용이 아니라 운영 가능한 engineering system이 됩니다.
