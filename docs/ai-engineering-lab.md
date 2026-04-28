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
| Long Work Windows | Expanding | 5-hour windows validated; 7-hour campaign testing; 12-hour canary planned |
| Infrastructure-aware app work | Active | AzVision network path analysis case study |
| Public-safe documentation | Active | Sanitized examples, synthetic data, and public boundaries |

## Why long-running AI work matters

Short AI coding sessions are easy to demo. The harder problem is making longer AI-assisted development safe enough to run for hours without losing scope, validation context, or human control.

The lab treats long-running work as an engineering system:

1. define scope and approval boundaries;
2. split long campaigns into restartable chunks;
3. run scheduled check-ins and read-backs;
4. preserve state and evidence;
5. validate before publish or deploy;
6. close with a reusable handoff record.

This is supervised, approval-gated, long-running AI development. It is not a claim that AI should make external or irreversible changes without a human decision.

## What stays private

The public repo intentionally excludes raw runtime state, local paths, account details, internal channel names, credentials, hosting control-panel notes, and real private cloud exports.

The goal is to share the operating patterns and the lessons, not the private machinery.

## Suggested reading path

1. [AI Engineering Control Plane](ai-assisted-engineering-control-plane.md)
2. [Long Work Window Playbook](long-work-window-playbook.md)
3. [AzVision Network Path Analysis](azvision-network-path-analysis.md)
4. [Security and Sanitization](security-and-sanitization.md)
