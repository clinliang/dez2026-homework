# Git Branch Strategy

This repository follows a multi-branch strategy designed for:
- long-term learning
- experimentation
- portfolio-quality delivery

## Branches Overview

| Branch        | Purpose |
|--------------|---------|
| main         | Stable, portfolio-ready code |
| develop      | Active development baseline |
| experiment   | Short-lived PoC and technical validation |
| exploration  | Open-ended research and learning |
| exercise     | Training, tutorials, courses (never merged) |

---

## Branch Semantics

### main
- Always runnable
- Clean structure and documentation
- Only merged from `develop`

### develop
- Stable development branch
- Can receive validated experiments
- Intermediate quality is acceptable

### experiment
- One branch = one question
- Short-lived
- Merge **only into develop**
- Deleted after merge or rejection

### exploration
- Free exploration (AI, tools, ideas)
- Can be messy
- Must be refactored before merging into develop

### exercise
- Courses, tutorials, practice
- Never merged into any branch

---

## Merge Rules

| From        | To        | Allowed |
|-------------|-----------|--------|
| experiment  | develop   | ✅ |
| develop     | main      | ✅ |
| exploration | develop   | ⚠️ after refactor |
| exercise    | any       | ❌ |

---

## Principles

- Branches exist to reduce cognitive load
- main represents what you would show a recruiter
- experiments must have a conclusion