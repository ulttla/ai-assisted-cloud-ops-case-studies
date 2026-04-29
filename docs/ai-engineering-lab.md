# AI Engineering Lab

## Purpose

The AI Engineering Lab is my personal R&D space for building AI-assisted applications, orchestration workflows, harness patterns, and supervised long-running engineering automation.

OpenClaw is the current orchestration layer. The lab itself is intentionally tool-agnostic: the useful part is not one specific model or command, but the operating system around scope, review, approval, validation, and evidence.

## What this repository shares

This public repository shares the parts of the lab that can help other people think about AI-assisted engineering workflows:

- how to coordinate multiple tools without losing a single accountable owner;
- how to separate planning, implementation, review, fact-checking, and risk review lanes;
- how to run longer work sessions without turning them into invisible automation;
- how to preserve evidence and closeout notes that make work resumable;
- how to convert private operational work into public-safe case studies.

## Current lab tracks

| Track | Status | Public evidence |
|---|---:|---|
| OpenClaw orchestration | Active | Current control plane for multi-tool workflows |
| Harness engineering | Active | Role-based review lanes, approval gates, and evidence closeouts |
| Long Work Windows | Validated | 5-hour and 12-hour campaigns validated via restartable chunks |
| Infrastructure-aware app work | Active | AzVision app development case study and cloud architecture decision support |
| Public-safe documentation | Active | Sanitized examples, synthetic data, and public boundaries |
| gun-wiki brain | Active | Model-neutral LLM reference notes, inspired by Karpathy-style reading and curation |
| Spark / local LLM experiments | Active | Privacy-sensitive local inference with llama.cpp, Ollama, and NVIDIA GPU experiments |

## Positioning note

The lab is built around AI-assisted app building and cloud architecture decision support, not a full-time software developer workflow. The output reflects a systems architect who uses AI tools inside a disciplined operating model.

## Why long-running AI work matters

Short AI coding sessions are easy to demo. The harder problem is making longer AI-assisted development safe enough to run for hours without losing scope, validation context, or human control.

The lab treats long-running work as an engineering system:

1. define scope and approval boundaries;
2. split long campaigns into restartable chunks;
3. run scheduled check-ins and read-backs;
4. preserve state and evidence;
5. validate before publish or deploy;
6. close with a reusable handoff record.

This is supervised, approval-gated, AI-assisted app development. It is not a claim of full-time developer workflow nor that AI should make external or irreversible changes without a human decision.

## What stays private

The public repo intentionally excludes raw runtime state, local paths, account details, internal channel names, credentials, hosting control-panel notes, and real private cloud exports.

The goal is to share the operating patterns and the lessons, not the private machinery.

## Suggested reading path

1. [AI Engineering Control Plane](ai-assisted-engineering-control-plane.md)
2. [Long Work Window Playbook](long-work-window-playbook.md)
3. [AzVision App Development](azvision-network-path-analysis.md)
4. [Gun-Wiki Brain](gun-wiki-brain.md)
5. [Spark Local LLM Lab](spark-local-llm-lab.md)
6. [Security and Sanitization](security-and-sanitization.md)
7. [Communicating AI-Assisted Work](communicating-ai-assisted-work.md)
