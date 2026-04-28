# OpenClaw Use Cases: AI Engineering Lab Notes

이 저장소는 제가 OpenClaw를 현재 orchestration layer로 사용해 운영하는 AI Engineering Lab의 공개용 노트입니다.

개인 런타임 설정을 그대로 공개하는 저장소가 아니라, supervised multi-tool AI engineering을 실제 작업에 적용하면서 얻은 패턴, 의사결정, 사례, 안전 기준을 public-safe 형태로 정리한 자료입니다.

## 이 저장소가 다루는 것

- 여러 AI 도구를 하나의 책임 있는 workflow 안에서 조율하는 방법
- planning, implementation, review, fact-check, risk review를 분리하는 harness engineering 패턴
- 여러 시간 동안 이어지는 AI-assisted work를 check-in, validation, closeout으로 관리하는 방식
- private operational work를 공개 가능한 case study와 example로 바꾸는 기준

## 이 저장소가 아닌 것

- 제 private runtime을 그대로 복제할 수 있는 설정 덤프가 아닙니다.
- credential, account, local path, private log, real cloud export는 포함하지 않습니다.
- AI가 사람 승인 없이 publish, deploy, infrastructure change를 수행해야 한다는 주장도 아닙니다.

## 핵심 생각

AI coding workflow는 속도만으로 평가하면 위험해질 수 있습니다. 제가 관심 있는 부분은 더 긴 작업을 어떻게 scope 안에 묶고, review하고, validate하고, 나중에 다시 이어갈 수 있는 evidence로 남길 수 있는가입니다.

제 기준의 operating model은 다음과 같습니다.

1. 하나의 accountable orchestrator가 scope와 최종 결정을 책임집니다.
2. 여러 specialist lane이 planning, build, review, fact-check, risk check를 나눠 맡습니다.
3. 외부 공개, 배포, 파괴적 변경, credential handling은 사람 승인을 유지합니다.
4. 긴 작업은 state와 closeout 기록으로 재개 가능하게 만듭니다.
5. 공개 문서는 private detail을 제거하고 pattern과 lesson만 남깁니다.

## 읽는 순서

| 문서 | 설명 |
|---|---|
| [AI Engineering Lab](docs/ko/ai-engineering-lab.md) | 전체 lab 방향과 왜 이 구조를 만들었는지 |
| [Long Work Window](docs/ko/long-work-window.md) | 여러 시간짜리 AI-assisted work를 관리하는 방식 |
| [AI Engineering Control Plane](docs/ko/control-plane.md) | 여러 AI 도구를 하나의 운영 구조로 묶는 방식 |
| [Security and Sanitization](docs/ko/security-and-sanitization.md) | 공개 문서에서 private detail을 제거하는 기준 |
| [English README](README.md) | 전체 공개 저장소의 기본 landing page |

영어 원문 문서는 `docs/` 폴더에 있습니다. 한국어 문서는 먼저 overview 중심으로 시작했고, 아직 영어 문서 전체를 모두 번역한 것은 아닙니다. AzVision case study, public release checklist, ADR 같은 세부 문서는 현재 영어 원문을 기준으로 읽는 것이 가장 정확합니다. 한국어 문서는 필요에 따라 점진적으로 늘릴 계획입니다.
