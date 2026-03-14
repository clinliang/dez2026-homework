# Data Engineering Zoomcamp 2026 — Homework & Practice Repository (Linliang CHEN)

This repository contains homework and practice materials for the Data Engineering Zoomcamp 2026, covering core data engineering concepts from local ingestion to workflow orchestration.

➡️ See all modules' content in [Data Engineering Zoocamp Github Repository](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main)

➡️ See **`README.md`** inside each project for setup and usage details.


## Repository list

- [Module 1 Data Ingest Pipeline with Docker + Postgres](#module-1-data-ingest-pipeline-with-docker--postgres)
- [Module 2 Data Orchestration with Docker + Kestra + Postgres|GCP](#module-2-data-orchestration-with-docker--kestra--postgresgcp)
- [Module 3 ELT with Terraform + Docker + GCS + BigQuery](#module-3-elt-with-terraform--docker--gcs--bigquery)
- [Module 4 Data Transform with dbt Core + DuckDB](#module-4-data-transform-with-dbt-core--duckdb)
- [Module 5 Use Bruin as Data Platform](#module-5-use-bruin-as-data-platform)
- [Workshop 1 AI-Assisted Data Pipeline with dlt + DuckDB](#workshop-1-ai-assisted-data-pipeline-with-dlt--duckdb)
- [Module 6 Batch Processing with Spark Standalone or DataProc](#module-6-batch-processing-with-spark-standalone-or-dataproc)
- [Module 7 Stream Processing with Kafka and Flink](#module-7-stream-processing-with-kafka-and-flink)



## Repository resume

### Module 1 Data Ingest Pipeline with Docker + Postgres

End-to-end NYC Taxi data ingestion pipeline using Docker Compose.

Focus on:
- Containerized setup (Docker)
- Data ingestion from CSV / Parquet (Python)
- Storage in PostgreSQL

📁 **Directory**: [m1_proj_docker_postgres_nyc_taxi/](./m1_proj_docker_postgres_nyc_taxi/)  


---


### Module 2 Data Orchestration with Docker + Kestra + Postgres|GCP

Orchestrated data engineering stack for NYC Taxi data with workflow management and cloud components.

Focus on:
- Workflow orchestration (Kestra)
- Postgres as analytical storage
- GCP integration
- Production-oriented modular architecture

📁 **Directory**: [m2_proj_workflow_kestra_nyc_taxi/](./m2_proj_workflow_kestra_nyc_taxi/)  


---


### Module 3 ELT with Terraform + Docker + GCS + BigQuery

Containerized batch ELT architecture for NYC Taxi data focusing on cloud-native storage and data warehousing.

Focus on:
- Infrastructure as Code (Terraform)
- Data Lake storage (Google Cloud Storage)
- Data Warehouse & analytical transforms (BigQuery)
- Production-ready environment with Docker + uv

📁 **Directory**: [m3_proj_tf-bq-dk_nytaxi_yellow/](./m3_proj_tf-bq-dk_nytaxi_yellow/)


---


### Module 4 Data Transform with dbt Core + DuckDB

Local-first ELT pipeline for NYC Taxi data using dbt Core on DuckDB to build analytics-ready data marts.

Focus on:
- Local ELT pipeline: Python → DuckDB → dbt Core
- dbt lifecycle: compile, run, test, build, docs
- Advanced modeling: Jinja macros, packages, variables and configs
- Scalable execution: OOM-safe and bucket-based batch execution

📁 **Directory**: [m4_proj_dbt_taxi_rides_ny/](./m4_proj_dbt_taxi_rides_ny/)


---

### Module 5 Use Bruin as Data Platform

Production-style batch data pipeline using Bruin to orchestrate SQL-based transformations with incremental strategies.

Focus on:
- Batch orchestration with Bruin
- Data quality checks & asset dependencies
- Modular SQL asset structure (staging → marts → reports)
- Production-ready execution with time-window parameters

📁 **Directory**: [m5_proj_bruin_nytaxi/](./m5_proj_bruin_nytaxi/)


---

### Workshop 1 AI-Assisted Data Pipeline with dlt + DuckDB

Production-ready batch data pipeline built with dlt and DuckDB, enhanced by MCP for AI-assisted development and ad hoc analysis.

Focus on:
- AI-assisted pipeline setup and ad hoc SQL exploration via Copilot (MCP)
- Incremental loading strategy with dlt
- Structured transformation layers (ingestion → staging)
- Local analytical warehouse powered by DuckDB

📁 **Directory**: [ws1_proj_dlt_mcp_nytaxi/](./ws1_proj_dlt_mcp_nytaxi/)


---


### Module 6 Batch Processing with Spark Standalone or DataProc

End-to-end Spark pipeline for NYC Taxi data, scaling from local clusters to GCP Dataproc.

Focus on:
- Environments: Spark Standalone (Local) and GCP Dataproc (Cloud)
- Architecture: Three-layer batch flow (Raw → Staging → Report)
- Ecosystem: Integration with Google Cloud Storage and BigQuery

📁 **Directory**: [m6_proj_spark_ny/](./m6_proj_spark_nytaxi/)

---

### Module 7 Stream Processing with Kafka and Flink

End-to-end streaming pipeline for NYC Taxi trip data, processing real-time events from ingestion to analytics.

Focus on:
- Environment: Local infrastructure orchestrated with Docker Compose
- Architecture: Real-time streaming pipeline simulation (Producer → Kafka → Flink → PostgreSQL)
- Ecosystem: Kafka for event streaming, PyFlink for stream processing, PostgreSQL for analytics storage

📁 **Directory**: [m7_proj_kafka_flink/](./m7_proj_kafka_flink/)


## Branches
- **main**: Final homework and project submissions.
- **learn**: Local practice and experimental code (not pushed to GitHub).