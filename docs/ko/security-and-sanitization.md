# Security and Sanitization

## 목적

AI-assisted engineering work를 공개할 때 가장 중요한 기준은 유용한 insight를 공유하되 private operational detail은 노출하지 않는 것입니다.

이 문서는 public lab notes를 만들 때 어떤 정보를 남기고 어떤 정보를 제거해야 하는지 정리합니다.

## 공개해도 되는 것

- architecture pattern
- workflow decision
- sanitized case study
- synthetic example data
- validation result
- public-safe diagram
- 일반화된 lesson learned

## 공개하면 안 되는 것

- credential, token, secret
- private account detail
- local runtime path
- internal channel name or id
- real cloud export
- private incident detail
- hosting control-panel detail
- exact automation schedule
- raw operational log

## Sanitization pattern

| Private detail | Public-safe replacement |
|---|---|
| Real resource name | synthetic resource name |
| Internal account path | generic account description |
| Real export data | synthetic sample |
| Incident timeline | generalized recovery pattern |
| Exact deployment panel steps | public release boundary and validation summary |
| Raw model output | reviewed summary with evidence |

## 공개 문서 작성 기준

좋은 공개 문서는 다음 균형을 지켜야 합니다.

1. 읽는 사람이 배울 수 있을 만큼 구체적이어야 합니다.
2. private system을 추정할 수 있을 만큼 자세하면 안 됩니다.
3. claim은 검증 가능한 범위 안에 있어야 합니다.
4. AI automation을 과장하지 않아야 합니다.
5. 사람 승인과 review boundary를 명확히 해야 합니다.

## 예시

좋은 표현:

> I converted a private network troubleshooting workflow into a synthetic case study that demonstrates path analysis, validation, and evidence presentation without exposing real cloud data.

피해야 할 표현:

> Here is the raw export and internal runtime log from the actual environment.

## 결론

공개 목적은 raw machinery를 보여주는 것이 아니라, 다른 사람이 배울 수 있는 engineering pattern을 안전하게 공유하는 것입니다.
