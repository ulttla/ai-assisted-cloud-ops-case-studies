# Korean Notes Index

이 폴더는 `gun-openclaw-use-cases` 저장소의 한국어 starter 문서 모음입니다.

영어 문서가 canonical source에 가깝고, 한국어 문서는 핵심 개념을 빠르게 읽기 위한 overview 역할을 합니다. 단, AI Lab positioning, Gun-Wiki Brain, Spark Local LLM Lab, AzVision App Development처럼 최근에 정리한 핵심 track은 한국어 문서도 함께 제공합니다.

## 추천 읽기 순서

| 문서 | 설명 |
|---|---|
| [AI Engineering Lab](ai-engineering-lab.md) | 전체 lab 방향과 public-safe 경계 |
| [AI Engineering Control Plane](control-plane.md) | 여러 AI 도구를 하나의 운영 구조로 묶는 방식 |
| [Long Work Window](long-work-window.md) | 여러 시간짜리 AI-assisted work를 check-in, validation, closeout으로 운영하는 방식 |
| [AzVision App Development](azvision-network-path-analysis.md) | Azure network analysis app을 cloud architecture decision support로 확장하는 사례 |
| [Gun-Wiki Brain](gun-wiki-brain.md) | model-neutral project memory와 context engineering 패턴 |
| [Spark Local LLM Lab](spark-local-llm-lab.md) | local LLM, NVIDIA, privacy-sensitive experiment track |
| [Security and Sanitization](security-and-sanitization.md) | 공개 문서에서 private detail을 제거하는 기준 |
| [Public Release Evidence Pattern](../public-release-evidence.md) | 공개 산출물을 검증 증거와 함께 설명하는 기준 |
| [Communicating AI-Assisted Work](communicating-ai-assisted-work.md) | AI-assisted work를 과장 없이 설명하는 기준 |

## 공개 경계

한국어 문서도 영어 문서와 같은 공개 경계를 따릅니다.

- private runtime 설정을 그대로 공개하지 않습니다.
- credential, account, private path, raw log, real cloud export를 포함하지 않습니다.
- AI가 사람 승인 없이 publish, deploy, infrastructure change를 수행해야 한다고 주장하지 않습니다.
- 12시간 LWW claim은 restartable chunk, supervised execution, approval gate와 함께 설명합니다.

## 영어 문서

전체 문서 목록은 [docs/README.md](../README.md)를 기준으로 확인하세요.
