# NYC Taxi Data Pipeline — GCP ELT

**Version 3.1** : A minimal data pipeline that loads NYC Yellow Taxi data into **Google Cloud Platform** using **Python**, **Docker**, **Terraform**, **GCS**, and **BigQuery**.

# Summary

- [I. Architecture](#i-architecture)
- [II. Quick Start](#ii-quick-start)
- [III. Homework Queries](#iii-homework-queries)
- [IV. References](#iv-references)

## I. Architecture

The platform implements a **containerized batch ELT architecture** using Google Cloud Platform. It is designed for reproducible local execution and cloud-native storage and analytics. For a complete project directory overview, see `structure.txt`.

---

### System Architecture

```text
Local Machine
 └─ Docker (Python + uv batch job)
     ├─ Extract & Load → GCS (raw data lake)
     └─ Transform → BigQuery (data warehouse)
```
---

### Components & Design Notes

- **Docker** provides a reproducible runtime for the batch pipeline
- **Python + uv** handle explicit extract/load logic
- **Terraform** provisions GCS and BigQuery (IaC)
- **GCS** stores raw files (data lake)
- **BigQuery** performs analytical transforms and queries

> Design choice:  
> This project intentionally avoids orchestration frameworks (e.g. Kestra or Airflow) to focus on **core data engineering fundamentals**: cloud infrastructure, batch ingestion, and clear execution flow.


## II. Quick Start

1. GCP Bootstrap (Project, IAM, Billing)
```Bash:
# 1.1 Project & APIs
gcloud projects create nytaxi-yellow-cll
gcloud services enable cloudresourcemanager.googleapis.com iam.googleapis.com serviceusage.googleapis.com storage-api.googleapis.com bigquery.googleapis.com

# 1.2 Service Account + roles
gcloud iam service-accounts create terraform-runner
gcloud projects add-iam-policy-binding nytaxi-yellow-cll \
        --member="serviceAccount:terraform-runner@nytaxi-yellow-cll.iam.gserviceaccount.com" \
        --role="roles/storage.admin"
gcloud projects add-iam-policy-binding nytaxi-yellow-cll \
        --member="serviceAccount:terraform-runner@nytaxi-yellow-cll.iam.gserviceaccount.com" \
        --role="roles/bigquery.admin"

# 1.3 Key & Billing
gcloud iam service-accounts keys create keys/service_account.json \
    --iam-account=terraform-runner@nytaxi-yellow-cll.iam.gserviceaccount.com
gcloud billing projects link nytaxi-yellow-cll --billing-account=xxx
```

2. Provision Infracture (Terraform)
```Bash:
cd terraform
terraform init
terraform plan
terraform apply -auto-approve
```

3. Install Python Dependencies (uv)
```Bash:
cd scripts
uv init --no-workspace
uv add pandas google-cloud-storage pyarrow requests google-cloud-bigquery
```

4. Run Batch ELT (Docker)
```Bash:
docker-compose up --build ingest
docker-compose run --rm transform
```

## III. Homework Queries

```SQL:
-- Q5. Create a new table with "Partition by tpep_dropoff_datetime and Cluster on VendorID"
CREATE OR REPLACE TABLE `nytaxi-yellow-cll.m3_nytaxi_yellow_bq.yellow_tripdata_optimized`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `nytaxi-yellow-cll.m3_nytaxi_yellow_bq.yellow_tripdata_non_partitioned`;

-- Q6. retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive)
SELECT DISTINCT VendorID
FROM `nytaxi-yellow-cll.m3_nytaxi_yellow_bq.yellow_tripdata_optimized`
WHERE tpep_dropoff_datetime >= '2024-03-01'
  AND tpep_dropoff_datetime =< '2024-03-15';
```

## IV. References

- [Homework M3 Repository - cll](https://github.com/clinliang/dez2026-homework/tree/main/m3_proj_tf-bq-dk_nytaxi_yellow)

- [Homework M3 instruction](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/03-data-warehouse/homework.md)

- [Submission URL (<10/02/2025)](https://courses.datatalks.club/de-zoomcamp-2026/homework/hw3)