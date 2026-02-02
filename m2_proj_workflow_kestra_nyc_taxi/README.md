# NYC Taxi Data Orchestration — Docker + Kestra + Postgres | GCP

**Version 3.1**  
A modular data engineering stack using Kestra, Postgres, Google Cloud Platform (GCP), and pgAdmin to orchestrate the ingestion and storage of NYC Taxi datasets (Yellow / Green).

[**Homework Repository: Module2 Workflow Orchestation with Kestra**](https://github.com/clinliang/dez2026-homework/tree/main/m2_proj_workflow_kestra_nyc_taxi)

---

## Summary

- [I. Infrastructure](#i-infrastructure)  
- [II. Quick Start](#ii-quick-start)
- [III. Homework Results](#iii-homework-results)
- [IV. References](#iv-references)

---

## I. Infrastructure

The platform supports two primary orchestration paths:

- A **local PostgreSQL storage engine** for development
- A **GCP cloud engine** for production-grade scaling

For a full project directory overview, see `structure.txt`.

### System Architecture

```text
            [ BROWSER / UI ]
                  │
        ┌─────────┴─────────┐
        │   Docker Network  │
        │                   │
  ┌─────┴─────┐       ┌─────┴─────┐
  │ [8080/81] │       │ [ Kestra ]│
  └─────┬─────┘       └─────┬─────┘
        │                   │
  ┌─────┴───────────────────┴─────┐
  │                               │
  ▼ LOCAL STORAGE (PG)            ▼ CLOUD STORAGE (GCP)
  ────────────────────            ─────────────────────
  [ db ] (Postgres 18)            [ GCS ] (Bucket)
     │   (Port: 5433)                │
     │                               │
  [ pgAdmin ] [8085]              [ BigQuery ]
     │   (Management)                │  (Database)
     └─────────┬─────────────────────┘
               ▼
        [ kestra_db ]
      (Internal Metadata)
```

### Components & Design Notes

- **kestra**: Standalone engine (v1.1) managing task execution and Gemini AI integration.
- **db / kestra_db**: Separate Postgres 18 instances to isolate orchestration metadata from project data.
- **pgadmin**: Unified web GUI for managing local database instances.

> **Notes for further improvements**
> - For Postgres Workflow: Stream local raw files directly to minimize intermediate "raw" table overhead in Postgres.
> - For GCP Workflow: Use Terraform for infrastructure-as-code (IaC) to manage GCS buckets and BigQuery datasets securely.

---

## II. Quick Start

### 1. Configure Secrets

Create and update your environment files for Docker Compose.

- `.env`: General project configs (e.g., `PROJECT_NAME`)
- `.env_encoded`: Sensitive keys (e.g., `SECRET_GCP_CREDS`, `SECRET_GEMINI_API_KEY`)

```bash
read -s SECRET_GCP_CREDS
# Copy and paste your API KEY, then ENTER to get the KEY
echo -n "$SECRET_GCP_CREDS" | base64 >> .env_encoded
# Encode the key in base64 and append it to .env_encoded
```

### 2. Launch Stack

Pull images and start services.

```bash
docker compose --env-file .env --env-file .env_encoded up -d
```

### 3. Access Interfaces

- **Kestra UI**: http://localhost:8080  
  `(admin@kestra.io / Admin1234)`
- **pgAdmin UI**: http://localhost:8085  
  `(admin@admin.com / root)`

### 4. Run Ingestion Jobs

Create flows in Kestra and run them. Backfill scheduled flows with triggers according to needs.

---

## III. Homework Results

- **Q1 (Yellow 2020-12 File Size)**: 134.5 MiB
- **Q2 (Rendered Variable file)**: green_tripdata_2020-04.csv
- **Q3 (Yellow 2020 Total Rows)**: 24,648,499
- **Q4 (Green 2020 Total Rows)**: 1,734,051
- **Q5 (Yellow March 2021 Rows)**: 1,925,152
- **Q6 (Kestra Schedule Timezone)**: Set timezone: America/New_York in the Schedule trigger

---

## IV. References

- [Homework instruction] (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/02-workflow-orchestration/homework.md)

- [Submission URL (< 03/02/2025)] (https://courses.datatalks.club/de-zoomcamp-2026/homework/hw2)