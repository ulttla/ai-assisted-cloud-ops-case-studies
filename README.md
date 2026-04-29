# OpenClaw Use Cases: AI Engineering Lab Notes

This repository is a public, sanitized snapshot of how I run an AI Engineering Lab with OpenClaw as the current orchestration layer.

It is not a raw dump of my private setup. It is a cleaned set of notes, patterns, decisions, and case studies for people interested in supervised multi-tool AI engineering: harness design, long-running work windows, evidence-based closeouts, and infrastructure-aware validation.

## What this repo is

- A practical lab-notes repository for AI-assisted engineering workflows.
- A public-safe explanation of how I coordinate multiple coding and review tools through one accountable orchestration layer.
- A set of patterns for keeping long-running AI work observable, reviewable, and approval-gated.
- A small collection of sanitized case studies and synthetic examples.

## What this repo is not

- It is not a turnkey clone of my private runtime.
- It is not a credentialed setup guide.
- It is not a claim that AI should publish, deploy, or change infrastructure without human approval.
- It does not include private logs, local runtime state, account details, real cloud exports, or hosting control-panel details.

## Core idea

Many AI coding workflows optimize for speed. My focus is operating discipline: how to make longer AI-assisted work stay scoped, reviewed, validated, and safe enough to turn into reusable engineering evidence.

The operating model is:

1. one accountable orchestrator;
2. multiple specialist lanes for planning, implementation, review, fact-checking, risk review, and smoke checks;
3. human approval for external, destructive, or irreversible actions;
4. state and closeout records that make long sessions resumable;
5. public-safe documentation that shares the insight without exposing private infrastructure.

## Language

- [Korean overview / 한국어 개요](README.ko.md)

## Reading path

| Start here | Why it matters |
|---|---|
| [AI Engineering Lab](docs/ai-engineering-lab.md) | Overall positioning and lab tracks |
| [AI Engineering Control Plane](docs/ai-assisted-engineering-control-plane.md) | How multiple tools stay under one accountable workflow |
| [Long Work Window Playbook](docs/long-work-window-playbook.md) | The supervised multi-hour execution pattern |
| [AzVision App Development](docs/azvision-network-path-analysis.md) | A concrete infrastructure/app case study |
| [Gun-Wiki Brain](docs/gun-wiki-brain.md) | Model-neutral project memory and context engineering pattern |
| [Spark Local LLM Lab](docs/spark-local-llm-lab.md) | Local LLM / NVIDIA privacy-sensitive experimentation track |
| [Security and Sanitization](docs/security-and-sanitization.md) | What is intentionally excluded from the public version |
| [Communicating AI-Assisted Work](docs/communicating-ai-assisted-work.md) | Public-safe language for explaining supervised AI work |
| [Portfolio Claim Guidelines](docs/portfolio-claim-guidelines.md) | Safer wording patterns for public metrics and business outcomes |
| [Public Release Checklist](docs/public-release-checklist.md) | A general checklist for publishing AI engineering notes safely |

## Design decisions

- [ADR 0001: Single orchestrator, multiple specialist lanes](docs/adr/0001-single-orchestrator.md)
- [ADR 0002: Consensus evidence before closeout](docs/adr/0002-consensus-before-closeout.md)
- [ADR 0003: Sanitized case-study repository instead of raw setup dump](docs/adr/0003-sanitized-case-study-repo.md)

## Diagrams

- [Agent team flow](diagrams/agent-team-flow.md)
- [AzVision path analysis flow](diagrams/azvision-path-analysis-flow.md)

## Examples

The `examples/` folder contains public-safe templates and synthetic data:

- harness packet template;
- Long Work Window closeout template;
- sanitized path evidence;
- synthetic Azure path sample.

These examples are intentionally small. They show the shape of the evidence without exposing private systems.

## Evidence snapshots

- AzVision app development path-analysis version: 110 targeted backend tests passed.
- Earlier backend regression: 235 tests passed.
- Frontend build: passed.
- Review pattern: builder, reviewer, fact-check, and challenger lanes with disagreements resolved before closeout.
- Long Work Window campaign model: validated up to 12 hours through restartable chunks, not a single unattended session.

The numbers are scoped to documented work slices. They are not generalized beyond what was actually validated.

## Public boundary

This repository is meant to share engineering patterns, not private operations. If a detail would expose credentials, private paths, account identifiers, real cloud exports, internal channel names, deployment control panels, or exact runtime state, it belongs outside the public tree.

## Portfolio link

More context: [gunkr.com](https://gunkr.com/)
