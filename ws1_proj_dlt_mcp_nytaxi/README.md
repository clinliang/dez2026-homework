# NYC Taxi Data Platform  — dlt + MCP

**Version 2.1** : End-to-end data pipeline using **dlt** + **DuckDB**, built with **VS Code** + **MCP** (Copilot). Covers ingestion, transformation, and analysis for NYC Taxi data.

# Summary

- [I. Architecture](#i-architecture)
- [II. Quick Start](#ii-quick-start)
- [III. References](#iii-references)


## I. Architecture

This project follows the Zoomcamp pattern with an integration of AI-assisted workflow via MCP. For a complete project directory overview, see `structure.txt`.


### System Architecture

```text
Raw CSV / API
      ↓
Ingestion Layer (Python + dlt)
      ↓
Staging Layer (SQL transformations in DuckDB)
      ↓
AI-Assisted Ad Hoc Analysis (Copilot Chat in VS Code)
```

### Core Components
- dlt → Data ingestion & pipeline management
- DuckDB → Local analytical warehouse
- MCP (VS Code) → AI-assisted development
- uv → Python dependency management


### Note
- No predefined reporting layer
- Focus on flexible, exploratory analytics
- AI agent generates SQL dynamically
- Developer remains in full control of logic and validation



## II. Quick Start

```Bash:
# 1. Environment Setup
uv init --python 3.12
uv add "dlt[duckdb,workspace]" pandas

# 2. Configure MCP (VS Code)
mkdir -p .vscode && touch .vscode/mcp.json # Paste MCP configuration into mcp.json

# 3. Initialize dlt Pipeline
uv run dlt init dlthub:taxi_pipeline duckdb # with 'copilot'

# 4. Develop Pipeline by using VS Code Chat (Copilot + MCP)

# 5. Run the pipeline and debug with the agent
uv run python taxi_pipeline.py

# 6. Inspect Pipeline
uv run dlt pipeline taxi_pipeline show
```


## III. References

- [dlt Repository - DTC Data Engineering Zoomcamp 2026](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2026/workshops/dlt)

- [Homework dlt Repository - cll](https://github.com/clinliang/dez2026-homework/tree/main/m6_proj_dlt_mcp_nytaxi)

- [Homework dlt instruction](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/workshops/dlt/dlt_homework.md)