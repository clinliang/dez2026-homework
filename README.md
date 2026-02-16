# Data Engineering Zoomcamp 2026 — Homework & Practice Repository (Linliang CHEN)

This repository contains homework and practice materials for the Data Engineering Zoomcamp 2026, covering core data engineering concepts from local ingestion to workflow orchestration.

➡️ See **`README.md`** inside each project for setup and usage details.


## Repository Structure


**Module 1 Data Ingest Pipeline with Docker + Postgres**

End-to-end NYC Taxi data ingestion pipeline using Docker Compose.

Focus on:
- Containerized setup (Docker)
- Data ingestion from CSV / Parquet (Python)
- Storage in PostgreSQL

📁 **Directory**: [m1_proj_docker_postgres_nyc_taxi/](./m1_proj_docker_postgres_nyc_taxi/)  


---


**Module 2 Data Orchestration with Docker + Kestra + Postgres|GCP**

Orchestrated data engineering stack for NYC Taxi data with workflow management and cloud components.

Focus on:
- Workflow orchestration (Kestra)
- Postgres as analytical storage
- GCP integration
- Production-oriented modular architecture

📁 **Directory**: [m2_proj_workflow_kestra_nyc_taxi/](./m2_proj_workflow_kestra_nyc_taxi/)  


---


**Module 3 ELT with Terraform + Docker + GCS + BigQuery**

Containerized batch ELT architecture for NYC Taxi data focusing on cloud-native storage and data warehousing.

Focus on:
- Infrastructure as Code (Terraform)
- Data Lake storage (Google Cloud Storage)
- Data Warehouse & analytical transforms (BigQuery)
- Production-ready environment with Docker + uv

📁 **Directory**: [m3_proj_tf-bq-dk_nytaxi_yellow/](./m3_proj_tf-bq-dk_nytaxi_yellow/)


---


**Module 4 Data Transform with dbt Core + DuckDB**

Local-first ELT pipeline for NYC Taxi data using dbt Core on DuckDB to build analytics-ready data marts.

Focus on:
- Local ELT pipeline: Python → DuckDB → dbt Core
- dbt lifecycle: compile, run, test, build, docs
- Advanced modeling: Jinja macros, packages, variables and configs
- Scalable execution: OOM-safe and bucket-based batch execution

📁 **Directory**: [m4_proj_dbt_taxi_rides_ny/](./m4_proj_dbt_taxi_rides_ny/)


## Branches
- **main**: Final homework and project submissions.
- **learn**: Local practice and experimental code (not pushed to GitHub).




# NYC Taxi Data Tranformation  — dbt core + DuckDB 

**Version 4.1** : Data transformation using **dbt core** on top of **DuckDB** enables a local ELT architecture that ingests NYC Taxi data (Yellow, Green, FHV) and materializes analytics-ready data marts.


## I. Architecture

This project implements a **local analytics engineering** pipeline using Python ingestion, **DuckDB**, **dbt core** (with OOM-safe temp configuration), and bash-based **bucket processing**  to produce analytics-ready datasets. For a complete project directory overview, see `structure.txt`.