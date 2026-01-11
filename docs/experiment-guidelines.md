# Experiment Guidelines

## What is an Experiment?

An experiment exists to answer **one technical question**.

Examples:
- Is dbt suitable for X?
- Can LLM help parse logs?
- API vs CSV ingestion performance?

## Rules

- One question per experiment
- Must produce a conclusion
- Short-lived (days or weeks)
- Merge only into develop

## Naming Convention

experiment/<topic>

Examples:
- experiment/dbt-vs-sql
- experiment/llm-log-parser
- experiment/api-rate-limit
