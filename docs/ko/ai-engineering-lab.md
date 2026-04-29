# AI Engineering Lab

## 목적

AI Engineering Lab은 AI-assisted application development, orchestration workflow, harness engineering, long-running automation을 실험하고 정리하는 개인 R&D 공간입니다.

현재는 OpenClaw를 orchestration layer로 사용하지만, 핵심은 특정 도구 하나가 아니라 작업 운영 방식입니다. 즉, scope를 어떻게 고정하고, review lane을 어떻게 나누고, 어떤 작업에 사람 승인을 유지하고, 어떤 evidence를 남길 것인가가 중심입니다.

## 왜 공개하는가

이 작업은 AI-assisted app building과 cloud architecture decision support에 초점을 둡니다. full-time software developer workflow를 주장하지 않습니다.

이 저장소의 목적은 제 private setup을 그대로 보여주는 것이 아닙니다. 대신 다른 사람에게도 도움이 될 수 있는 pattern과 lesson을 공유하는 것입니다.

공개하는 내용은 다음과 같습니다.

- 여러 AI 도구를 한 workflow 안에서 조율하는 방법
- planning, implementation, review, fact-check, risk review를 분리하는 이유
- 긴 AI-assisted session이 drift하지 않도록 check-in과 closeout을 운영하는 방법
- private operational work를 public-safe case study로 바꾸는 기준

## 현재 lab track

| Track | 상태 | 공개 가능한 evidence |
|---|---:|---|
| OpenClaw orchestration | Active | 현재 multi-tool workflow의 control plane |
| Harness engineering | Active | role-based review lane, approval gate, closeout evidence |
| Long Work Window | Validated | 5시간 및 12시간 campaign을 restartable chunk로 검증 |
| Infrastructure-aware app work | Active | AzVision network path analysis case study, cloud architecture decision support |
| Public-safe documentation | Active | synthetic example, sanitized evidence, 공개 경계 기준 |
| gun-wiki brain | Active | model-neutral LLM reference note, Karpathy 스타일 reading note curation |
| Spark / local LLM 실험 | Active | llama.cpp, Ollama, NVIDIA GPU 기반 privacy-sensitive local inference |

## 중요한 경계

이 작업은 fully unattended AI automation을 주장하지 않습니다.

제가 추구하는 방향은 다음에 가깝습니다.

- supervised execution
- approval-gated publishing and deployment
- evidence-backed closeout
- human ownership of final decisions

AI가 더 많은 일을 도울 수는 있지만, 외부 공개, 배포, credential handling, 파괴적 변경에는 명확한 사람 승인과 검증이 필요합니다.

## 다음 읽을 문서

한국어 문서는 다음 순서가 좋습니다.

1. [AI Engineering Control Plane](control-plane.md)
2. [Long Work Window](long-work-window.md)
3. [Gun-Wiki Brain](gun-wiki-brain.md)
4. [Spark Local LLM Lab](spark-local-llm-lab.md)
5. [Security and Sanitization](security-and-sanitization.md)
6. [AzVision App Development](azvision-network-path-analysis.md)
7. [Communicating AI-Assisted Work](communicating-ai-assisted-work.md)
