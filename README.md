# AI-Assisted Cloud Ops Case Studies

A public-ready portfolio package showing how I use AI-assisted engineering workflows to improve cloud operations, infrastructure reliability, and Azure network analysis.

## One-line pitch

I design AI-assisted engineering workflows that turn long-running infrastructure work into trackable, reviewed, and evidence-backed delivery.

## Why this matters

Many AI workflows optimize only for speed. In infrastructure and cloud operations, speed is not enough: the workflow also needs scope control, human approval, security boundaries, validation evidence, and a clear closeout trail.

This repository documents a sanitized version of the operating model I use for:

- Azure network path analysis and evidence-backed troubleshooting
- role-based AI review lanes for planning, implementation, verification, and risk review
- long-running work windows with progress checkpoints and final validation
- public-safe documentation practices for AI-assisted engineering work

## Case studies

| Case study | What it demonstrates |
|---|---|
| [AzVision Network Path Analysis Hardening](docs/azvision-network-path-analysis.md) | Azure networking domain knowledge, correctness-first engineering, test-backed delivery |
| [AI-Assisted Engineering Control Plane](docs/ai-assisted-engineering-control-plane.md) | Multi-agent workflow design, review governance, human-in-the-loop execution |
| [Long Work Window Playbook](docs/long-work-window-playbook.md) | Structured execution for long-running AI-assisted development work |
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

1. Start with the AzVision case study for the strongest Azure/cloud signal.
2. Read the engineering control-plane writeup to understand the AI-assisted workflow.
3. Review the Long Work Window playbook for the execution discipline behind longer work sessions.
4. Check the examples folder for public-safe packet and closeout templates.

## Next validation targets

- Expand the synthetic Azure sample into a repeatable demo fixture if public code examples are later added.
- Add diagrams rendered from the Mermaid source in `diagrams/`.
- Keep the gunkr.com portfolio draft aligned with this repository until final publish approval.
