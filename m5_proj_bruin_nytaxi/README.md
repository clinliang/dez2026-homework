# NYC Taxi Data Platform  — Bruin

**Version 2.1** : Build an end-to-end data pipeline using **Bruin**, covering ingestion, staging, and reporting layers on NYC Taxi data.


# Summary

- [I. Architecture](#i-architecture)
- [II. Quick Start](#ii-quick-start)
- [III. Homework Queries](#iii-homework-queries)
- [IV. References](#iv-references)


## I. Architecture

This project follows the Zoomcamp architecture but is implemented with a **Bruin-native** structure. For a complete project directory overview, see `structure.txt`.

### System Architecture

```text
Raw CSV / Source
        ↓
Ingestion (Python)
        ↓
Staging (SQL transformations)
        ↓
Report Layer (Aggregations)
```


## II. Quick Start

```Bash:
# 1. Install dependencies
pip install -r pipeline/assets/ingestion/requirements.txt

# 2. Validate pipeline
bruin validate ./zoomcamp/pipeline

# 3. Run full pipeline
bruin run ./zoomcamp/pipeline

# 4. Run a specific asset
bruin run ./zoomcamp/pipeline/assets/staging/trips.sql
```


## IV. References

- [Homework M5 Repository - cll](https://github.com/clinliang/dez2026-homework/tree/main/m5_proj_bruin_nytaxi)

- [Homework M5 instruction](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/05-data-platforms/homework.md)