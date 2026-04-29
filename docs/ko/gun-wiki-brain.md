# Gun-Wiki Brain

## 목적

Gun-Wiki Brain은 AI-assisted engineering 작업을 위한 model-neutral knowledge system입니다.

핵심 목표는 프로젝트 결정, 아키텍처 메모, 리뷰 결과, 리서치 요약, 반복 가능한 패턴을 특정 chat session이나 특정 모델에 가두지 않는 것입니다. OpenClaw, Codex, Claude Code, Gemini CLI, local LLM, 또는 앞으로 사용할 다른 도구가 같은 지식 기반을 활용할 수 있게 만드는 방향입니다.

## 왜 중요한가

AI 도구는 필요한 맥락을 제때 찾을 수 있을 때 더 강력합니다. 오래 남는 지식 계층이 없으면 새 session마다 같은 결정, 제약, 시행착오를 다시 찾아야 합니다.

Gun-Wiki 패턴은 context를 engineering asset으로 다룹니다.

1. 중요한 결정과 closeout을 캡처합니다.
2. raw note와 stable knowledge를 분리합니다.
3. 재사용 가치가 확인된 내용만 stable wiki로 올립니다.
4. 나중에 retrieval로 관련 맥락을 찾습니다.
5. 특정 모델 하나에 종속되지 않는 source of truth를 유지합니다.

## 영감과 공개 경계

이 작업은 LLM이 읽기 쉬운 개인 지식 시스템, curated reading note, structured context workflow에서 영감을 받았습니다. Andrej Karpathy가 공개적으로 이야기한 LLM note-taking과 context 활용 아이디어도 이 방향을 생각하는 데 참고가 됐습니다.

이 공개 문서는 운영 모델만 설명합니다. private vault 내용, local path, 개인 메모, account 정보, raw private session log는 공개하지 않습니다.

## 운영 패턴

| 계층 | 역할 |
|---|---|
| Raw capture | closeout, checkpoint, 유용한 session summary를 정리 전 상태로 보관 |
| Staging | note가 재사용 가치가 있는지 확인하는 중간 단계 |
| Stable wiki | 오래 쓸 수 있는 pattern, system note, project knowledge 보관 |
| Retrieval bridge | 특정 모델에 종속되지 않고 과거 맥락을 다시 찾는 경로 |

## 공개 가능한 표현

공개 문서에서는 이렇게 말할 수 있습니다.

> I use a structured knowledge base to preserve project decisions, review outcomes, and architecture patterns so future AI-assisted sessions can retrieve the right context.

공개 문서에 넣으면 안 되는 것:

- private vault path
- account name 또는 token
- raw private chat log
- 민감한 infrastructure detail
- redaction 없는 client 또는 employer data

## 포트폴리오 시그널

이 작업은 context engineering, knowledge-management discipline, 여러 AI 도구를 하나의 지식 기반에 연결하는 운영 설계 능력을 보여줍니다.
