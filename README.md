# AI Engineering Lab

A public portfolio package for my personal AI Engineering Lab: multi-tool orchestration, harness engineering, supervised long-running development windows, and selected infrastructure/app case studies.

## One-line pitch

I design AI-assisted engineering systems that turn multi-tool coding and infrastructure work into trackable, reviewed, approval-gated, and evidence-backed delivery.

## Why this matters

Many AI coding workflows optimize only for speed. My focus is broader: using an orchestration layer to coordinate multiple AI tools, CLI workflows, browser automation, validation gates, and human approval boundaries so long-running work stays safe and reviewable.

This repository documents a sanitized version of the operating model I use for:

- AI Engineering Lab structure for personal app development and automation
- OpenClaw as the current orchestration/control-plane layer
- Codex, Claude Code, Gemini CLI, browser automation, local scripts, GitHub, and hosting workflows
- role-based harness engineering for planning, implementation, review, fact-check, risk review, and closeout
- supervised long-running AI development windows, currently validated at 5 hours with 7-hour campaign testing and 12-hour canary planned
- Azure network path analysis and evidence-backed troubleshooting as one concrete case study
- public-safe documentation practices for AI-assisted engineering work

## Lab tracks and case studies

| Case study | What it demonstrates |
|---|---|
| [AI Engineering Lab Overview](docs/ai-engineering-lab.md) | Personal R&D system for AI-assisted app development, orchestration, and long-running execution |
| [AI-Assisted Engineering Control Plane](docs/ai-assisted-engineering-control-plane.md) | Multi-tool orchestration, review governance, human-in-the-loop execution |
| [Long Work Window Playbook](docs/long-work-window-playbook.md) | Supervised autonomous development windows with checkpoints, validation, and closeout evidence |
| [AzVision Network Path Analysis Hardening](docs/azvision-network-path-analysis.md) | Azure networking domain knowledge, correctness-first engineering, test-backed delivery |
| [Security and Sanitization Policy](docs/security-and-sanitization.md) | How private operational work is converted into public-safe portfolio material |
| [GitHub Publish Plan](docs/github-publish-plan.md) | Safe sequence for creating the public repository after approval |
| [gunkr.com Deploy Plan](docs/gunkr-deploy-plan.md) | Safe sequence for publishing the portfolio page after approval |

## Evidence snapshots

- Backend targeted tests: 110 passed in the AzVision network-path hardening slice
- Earlier backend regression: 235 passed
- Frontend build: passed
- Review process: builder/reviewer/fact-check/challenger workflow with disagreements resolved before closeout

Numbers are intentionally scoped to the documented work slice rather than generalized beyond what was verified.


## Job-search companion docs

- [Hiring Manager Summary](docs/hiring-manager-summary.md)
- [Interview Guide](docs/interview-guide.md)
- [Resume and LinkedIn Copy Draft](docs/resume-linkedin-copy.md)

## Repository boundaries

This is a sanitized public case-study repository. It does not contain:

- private credentials, tokens, local runtime configuration, or service endpoints
- raw operational logs or personal automation state files
- real Azure export data or customer/company-specific resource identifiers
- hosting control-panel details or internal channel mappings

See [Security and Sanitization Policy](docs/security-and-sanitization.md) for the public release checklist.

## Suggested reading path

1. Start with the AI Engineering Lab overview for the overall positioning.
2. Read the engineering control-plane writeup to understand the multi-tool orchestration and harness model.
3. Review the Long Work Window playbook for the execution discipline behind longer supervised sessions.
4. Read the AzVision case study as a concrete app/infrastructure example.
5. Check the examples folder for public-safe packet and closeout templates.

## Next validation targets

- Expand the synthetic Azure sample into a repeatable demo fixture if public code examples are later added.
- Add diagrams rendered from the Mermaid source in `diagrams/`.
- Keep the gunkr.com AI Engineering Lab section aligned with this repository as the lab evolves.
