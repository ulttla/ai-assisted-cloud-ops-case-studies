# Spark Local LLM Lab

## 목적

Spark Local LLM Lab은 privacy-sensitive engineering experiment, GPU 기반 model testing, supervised AI workflow integration을 위한 local inference track입니다.

목표는 local model을 쓴다고 모든 민감한 작업이 자동으로 안전하다고 주장하는 것이 아닙니다. 외부 API만 쓰기 애매한 작업에 대해 local review lane을 추가하는 것입니다.

## 왜 중요한가

대부분의 AI-assisted engineering workflow는 hosted model API에 의존합니다. hosted API는 유용하지만, infrastructure work에서는 local inference, GPU 제약, service operation, routing, privacy boundary를 직접 이해하는 것도 중요합니다.

Local LLM lane은 다음에 도움이 됩니다.

- 외부 공유 전 private draft review
- hosted API를 기본값으로 쓰기 어려운 code 또는 document review experiment
- model comparison과 latency testing
- NVIDIA GPU 기반 local inference 운영 경험
- 같은 supervised control plane 안에서 쓰는 second opinion

## 운영 경계

Local model은 review와 experiment lane으로 사용합니다. 최종 권한을 가진 unchecked authority로 쓰지 않습니다.

공개 가능한 표현:

> I configured and operate a local LLM environment on NVIDIA hardware for privacy-sensitive engineering experiments and model evaluation. It is connected to the same supervised workflow as the rest of the AI Engineering Lab.

피해야 할 표현:

- local이므로 모든 sensitive task가 안전하다는 표현
- formal control 없이 production security guarantee처럼 들리는 표현
- private prompt, document, path, runtime state 공개
- credential, account detail, internal network exposure 설명

## 통합 패턴

| 구성 요소 | 역할 |
|---|---|
| Local inference server | model experiment와 review task를 local에서 실행 |
| NVIDIA hardware | GPU 기반 inference 경험 제공 |
| OpenClaw routing | local model을 같은 supervised workflow에 연결 |
| Human approval | 외부 공개, 파괴적 변경, 되돌리기 어려운 작업은 명시 승인 뒤 진행 |
| Evidence trail | 무엇을 검토했고 무엇이 아직 불확실한지 기록 |

## 포트폴리오 시그널

이 track은 local LLM operations, privacy-aware AI workflow design, GPU 기반 infrastructure learning, local model infrastructure를 governed engineering process에 통합하는 능력을 보여줍니다.
