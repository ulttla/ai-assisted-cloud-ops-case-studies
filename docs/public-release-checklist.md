# Public AI Engineering Repo Release Checklist

## Purpose

Use this checklist before publishing AI-assisted engineering notes, examples, case studies, or lab documentation.

It is intentionally general. It should work for any public lab-notes repository, not only this repo.

## 1. Content boundary

- [ ] The repo explains patterns, decisions, and sanitized evidence rather than raw private runtime state.
- [ ] Private credentials, tokens, session data, and environment files are absent.
- [ ] Local paths, private account identifiers, internal channel names, and exact automation schedules are absent.
- [ ] Real cloud exports or customer data are replaced with synthetic or sanitized examples.
- [ ] Draft marketing copy, internal approval packets, and deployment notes are outside the public tree.

## 2. Claim safety

- [ ] Test counts and validation results are scoped to the exact slice that produced them.
- [ ] Business metrics are either evidence-ready or softened into public-safe wording.
- [ ] Security or incident content avoids private event details.
- [ ] The text does not imply fully unattended production changes.
- [ ] Human approval boundaries are clearly stated for publishing, deployment, credentials, and destructive actions.

## 3. Reader path

- [ ] README explains what the repo is and what it is not.
- [ ] There is a short reading path for first-time visitors.
- [ ] Internal notes are not mixed with polished public docs.
- [ ] Examples are clearly labeled as synthetic or sanitized.
- [ ] Diagrams and decisions support the main narrative instead of distracting from it.

## 4. Validation

- [ ] Run the repo’s public-readiness scan.
- [ ] Check for broken links in the README and main docs.
- [ ] Confirm generated or copied examples do not include private identifiers.
- [ ] Confirm the public tree looks intentional in the GitHub file browser.
- [ ] Review the latest diff before publishing.

## 5. After publishing

- [ ] Open the public URL in a clean browser session.
- [ ] Confirm the README renders correctly.
- [ ] Confirm linked docs are polished and intentional.
- [ ] Confirm any portfolio site points to the correct public entry point.
- [ ] Record what was published, what was validated, and what remains pending.

## Release posture

A good public release should feel useful to an outside reader even if they never hire you, clone the repo, or know the private context behind it.

The goal is to share insight, not raw machinery.
