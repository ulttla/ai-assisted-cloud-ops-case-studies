# Security and Sanitization Policy

## Goal

Convert private AI-assisted engineering work into public portfolio material without exposing credentials, personal runtime details, cloud account identifiers, private logs, or operational attack surface.

## Publishable by default

- architecture concepts
- sanitized diagrams
- problem / solution / outcome narratives
- test/build results scoped to a work slice
- lessons learned
- synthetic examples
- public-safe templates

## Do not publish

- API keys, tokens, passwords, session values, or secret categories with raw values
- local file paths or user directory structures
- hosting control-panel details
- internal channel IDs or account IDs
- approval shortcut words or private operational triggers
- real Azure exports, subscription IDs, tenant IDs, resource IDs, or company-specific resource names
- raw automation state files
- private development journal frontmatter
- screenshots containing email addresses, balances, account panels, channels, or runtime paths

## Modify before publishing

| Private detail | Public-safe replacement |
|---|---|
| Specific model/version names | Role-level description such as review lane, fact-check lane, or orchestration LLM |
| Tool names intentionally used as public context | Keep only when they are part of the public artifact's purpose; for this repo, OpenClaw is intentionally named as the current orchestrator while private runtime details stay omitted |
| Local paths | Project-relative paths or omitted entirely |
| Real cloud resource identifiers | Synthetic labels such as `source-vm`, `app-subnet`, `web-nsg` |
| Internal channels | Generic terms such as development channel or portfolio channel |
| Raw logs | Summarized cause / effect / action |
| Private commit history | Clean public repository or curated excerpts |

## Preflight checklist

```text
[ ] No secrets, tokens, passwords, or private config files
[ ] No local absolute paths
[ ] No internal channel IDs, account IDs, or approval shortcuts
[ ] No real Azure tenant/subscription/resource identifiers
[ ] No screenshots with private UI elements
[ ] Public examples use synthetic data only
[ ] Claims are backed by visible artifacts or scoped validation evidence
[ ] Git history is clean or the public repo starts from a fresh history
[ ] README states the repository is a sanitized public lab-notes package
[ ] Public tool names are intentional and do not expose private runtime configuration
[ ] Publish/deploy has explicit human approval
```

## Claim rules

Strong public claims should be:

- **verifiable**: backed by an artifact, test result, screenshot, or documented decision
- **scoped**: tied to a specific work slice, not inflated beyond evidence
- **honest about AI assistance**: distinguish orchestration, review, and implementation support
- **safe**: not dependent on private accounts or private runtime data

## Recommended wording

Use:

> Designed and operated a role-based AI-assisted engineering workflow with structured review, validation, and closeout evidence.

Avoid:

> Fully automated everything with AI agents.

Use:

> Hardened Azure network path analysis and validated the slice with targeted backend tests and frontend build verification.

Avoid:

> Built an enterprise-grade Azure platform.
