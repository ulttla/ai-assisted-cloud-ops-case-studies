# Gun-Wiki Brain

## Purpose

The gun-wiki brain is a model-neutral knowledge system for AI-assisted engineering work.

The goal is simple: project decisions, architecture notes, review outcomes, research summaries, and reusable patterns should not stay trapped inside one chat session or one model vendor. They should live in a structured knowledge base that can be reused by OpenClaw, Codex, Claude Code, Gemini CLI, local LLMs, or future tools.

## Why it matters

AI tools are strongest when they can recover the right context at the right time. Without a durable knowledge layer, every new session has to rediscover the same decisions, constraints, and lessons.

The gun-wiki pattern treats context as an engineering asset:

1. capture important decisions and closeouts;
2. keep raw notes separate from stable knowledge;
3. promote only sanitized, reusable knowledge;
4. use retrieval to find relevant context later;
5. keep the source of truth model-neutral.

## Inspiration and boundary

This work is inspired by the broader idea of LLM-readable personal knowledge systems and curated reading notes, including public discussions from Andrej Karpathy and others about working with LLMs and structured context.

The public material here describes the operating model. It does not publish private vault contents, local paths, personal notes, account details, or raw internal session logs.

## Operating pattern

| Layer | Role |
|---|---|
| Raw capture | Stores closeouts, checkpoints, and useful session summaries before they are cleaned up |
| Staging | Lets notes prove that they are reusable before becoming stable reference material |
| Stable wiki | Holds durable patterns, system notes, and project knowledge |
| Retrieval bridge | Helps AI tools find relevant prior context without depending on one model vendor |

## Public-safe example

A public note can say:

> I use a structured knowledge base to preserve project decisions, review outcomes, and architecture patterns so future AI-assisted sessions can retrieve the right context.

A public note should not include:

- private vault paths;
- account names or tokens;
- raw private chat logs;
- sensitive infrastructure details;
- unredacted client or employer data.

## Hiring signal

This work demonstrates context engineering, knowledge-management discipline, and the ability to make AI-assisted engineering repeatable across tools instead of depending on one chat transcript.
