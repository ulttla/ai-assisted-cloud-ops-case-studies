# Public Release Evidence Pattern

## 목적

AI-assisted work는 결과물만 공개할 때보다 검증 근거와 함께 공개할 때 더 신뢰할 수 있습니다. 이 문서는 포트폴리오 페이지, 공개 랩 노트, sanitized case study를 공개하기 전에 어떤 증거를 남기는지 설명합니다.

목표는 private operational log를 공개하는 것이 아닙니다. 목표는 공개 가능한 수준에서 다음 질문에 답하는 것입니다.

- 무엇이 바뀌었는가?
- 무엇을 검증했는가?
- 어떤 claim이 evidence 범위 안에 있는가?
- 무엇은 공개 범위 밖으로 남겼는가?

## Evidence layers

| Layer | 확인 질문 | Public-safe 예시 |
|---|---|---|
| Content boundary | private detail이 제거되었는가? | credential, account ID, private path, raw log, internal channel 제외 |
| Claim boundary | claim이 검증된 범위 안에 있는가? | test count는 특정 작업 slice에만 연결, 장시간 작업은 supervised chunk로 설명 |
| Reader path | 독자가 문서를 따라갈 수 있는가? | README, docs index, examples, portfolio link가 정상 동작 |
| Validation | 기계적 검증 또는 리뷰가 있었는가? | link check, package scan, smoke test, marker scan, browser inspection |
| Human gate | 외부 공개가 의도적으로 승인되었는가? | publish/deploy는 approval-gated 상태 유지 |

## 최소 release checklist

1. **Scope statement** — 이 산출물이 무엇이고 무엇이 아닌지 설명합니다.
2. **Public boundary scan** — secret, private account identifier, raw log, private path, internal channel이 없는지 확인합니다.
3. **Claim scan** — autonomy, security, uptime, production claim이 evidence보다 강하지 않은지 확인합니다.
4. **Reader-path check** — 공개 문서와 페이지 링크가 정상인지 확인합니다.
5. **Smoke or package check** — 반복 가능한 명령 또는 브라우저 확인으로 결과를 검증합니다.
6. **Closeout note** — 완료, 검증, 남은 risk, 다음 action을 남깁니다.

## 예시 closeout evidence

```text
Completed:
- Portfolio AI Lab copy와 public GitHub lab notes를 업데이트했다.
- Public surface에서 internal release note를 제거했다.
- Reader-path check를 반복 가능한 스크립트로 추가했다.

Validation:
- Public package scan passed.
- Local markdown links passed.
- Live smoke passed.
- Reader-path crawl passed.
- Public marker scan found no stale/private deployment markers.

Risk / boundary:
- Hosting workflow details는 private portfolio source repo에만 유지한다.
- External publishing은 approval-gated 상태를 유지한다.
```

## 의미

이 패턴은 AI-assisted output을 engineering evidence로 바꾸는 방식입니다. 빠른 초안 작성보다 중요한 것은 review separation, public-safe boundary, validation, accountable closeout입니다.
