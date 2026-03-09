# NYC Taxi Data Platform — Batch Processing with Spark

**Version 2.1** : 

An end-to-end batch pipeline for processing **NYC Taxi data** using **Apache Spark** . Supports local execution via **Spark Standalone** and cloud execution on **Google Cloud Dataproc** with **Google Cloud Storage** and **BigQuery**.

This project follows the architecture taught in the **Data Engineering Zoomcamp (Batch with Spark)** module.

---

# Summary

- [I. Architecture](#i-architecture)
- [II. Setup & Installation](#ii-setup--installation)
- [III. Execution Guide](#iii-execution-guide)
- [IV. References](#iv-references)


## I. Architecture

The pipeline follows a three-layer batch architecture (Raw → Staging → Report) implemented for both local and cloud environments. For a complete project directory overview, see `structure.txt`.

### System Architecture in local and gcp bq

```text
Raw (Parquet) ──▶ Ingestion (Spark) ──▶ Staging/Transform ──▶ Report (BigQuery/Local)
```

### Two execution environments are supported:
- Local: Spark Standalone Cluster
- Cloud: GCP Dataproc (Managed Spark)


## II. Setup & Installation

### 1. Prerequisites
- Java 11+ (Required for Spark)
- Python 3.x with uv or pip
- GCP Account & gcloud CLI (for cloud execution)

### 2. Install Spark & Dependencies

```Bash:
# Install Java and Python dependencies
sudo apt update && sudo apt install default-jdk -y
uv init && uv add pyspark jupyterlab

# Download and Extract Spark
mkdir -p ~/spark && cd ~/spark
wget https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
tar -xzf spark-3.5.1-bin-hadoop3.tgz
```

### 3. Environment Configuration
Add the following to your ~/.bashrc and run source ~/.bashrc:

```Bash:
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))
export SPARK_HOME=$HOME/spark/spark-3.5.1-bin-hadoop3
export PATH="$PATH:$JAVA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin"
```


## III. Execution Guide

### 1. Download data
```Bash
cd code && ./download_nytaxi_bq.sh 'yellow' 2020 # green, 2021
```

### 2. Local Spark Standalone

```Bash
# Start Master and Worker
start-master.sh   # UI: http://localhost:8080
start-worker.sh spark://127.0.0.1:7077

# Submit Job
spark-submit \
    --master "spark://127.0.0.1:7077" \
    code/06_spark_standalone_script.py \
    --input_green=../data/pq/green/year=2021 \
    --input_yellow=../data/pq/yellow/year=2021 \
    --output=data/report/2021
```

## 3. Google Cloud Dataproc

```Bash
# Create Cluster
gcloud dataproc clusters create nytaxi-cluster \
    --region=europe-west9 \
    --num-workers=2 \
    --master-machine-type=e2-standard-4 \
    --worker-machine-type=e2-standard-4

# Submit PySpark Job
gcloud dataproc jobs submit pyspark \
    gs://your-bucket/code/spark_job.py \
    --cluster=nytaxi-cluster \
    --region=europe-west9 \
    -- \
    --input_green=gs://your-bucket/pq/green/year=2020 \
    --input_yellow=gs://your-bucket/pq/yellow/year=2020 \
    --output="your-project:dataset.table"

# Cleanup
gcloud dataproc clusters delete nytaxi-cluster --region=europe-west9
```

## IV. References

- [M6 Batch with Spark - DTC Data Engineering Zoomcamp 2026](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/06-batch)

- [Homework M6 Repository - cll](https://github.com/clinliang/dez2026-homework/tree/main/m6_proj_spark_nytaxi)

- [NYC Official Data in Parquets](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

- [NYC TLC Data in CSV - 2020 & 2021 only](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/${TAXI_TYPE}/${TAXI_TYPE}_tripdata_${YEAR}-${FMONTH}.csv.gz)