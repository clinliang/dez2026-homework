# NYC Taxi Streaming Data Platform — Kafka + Flink

**Version 2.1** : 

An end-to-end **stream processing** pipeline for **NYC Taxi trip data** using:
- Apache **Kafka** for real-time event streaming
- Apache **Flink (PyFlink)** for stream processing
- **PostgreSQL** for analytical storage
- **Docker Compose** for local infrastructure orchestration

This project follows the architecture taught in the **Data Engineering Zoomcamp – Streaming** module.

---

# Summary

- [I. Architecture](#i-architecture)
- [II. Quick Start](#ii-quick-start)
- [III. Commands and Queries for Questions](#iii-commands-and-queries-for-questions)
- [IV. References](#v-references)


## I. Architecture

This project implements a real-time streaming analytics pipeline.
For a complete project directory overview, see `structure.txt`.

### System Architecture in local and gcp bq

```text
Taxi Events ──▶ Kafka Producer ──▶ Kafka Topic ──▶ Flink Streaming Jobs ──▶ Postgres Analytical Tables
```

### Pipeline Components

| Layer             | Tool            | Purpose                |
| ----------------- | --------------- | ---------------------- |
| Event ingestion   | Kafka Producer  | Send taxi trip events  |
| Message queue     | Kafka           | Stream transport       |
| Stream processing | Flink (PyFlink) | Real-time aggregation  |
| Storage           | PostgreSQL      | Store analytics tables |
| Infrastructure    | Docker Compose  | Local orchestration    |


## II. Quick Start

### 1. Prerequisites
Install:
- Docker
- Docker Compose
- Python 3.11+
- uv or pip

### 2. Prepare Infrastructure and Events Data

```Bash:
# 2.1 Start infrastructure
docker compose up -d
# This will start: Redpanda(Kafka), Flink JobManager, Flink TaskManager, PostgreSQL

# 2.2 Create topic
docker exec -it m7_proj_kafka_flink-redpanda-1 rpk topic create green-trips

# 2.3 Produce events Data (Command for Question 2)
uv run python -m producers.producer_green_2510
# Send green taxi Octobre 2025 trip events to Kafka.
```

### 3. Prepare Sink Tables in PostgreSQL

```SQL:
CREATE TABLE pickup_demand_5min (
    window_start TIMESTAMP,
    window_end TIMESTAMP,
    pickup_location_id INTEGER,
    trip_count BIGINT,
    PRIMARY KEY (window_start, pickup_location_id)
);

CREATE TABLE session_pickups (
    session_start TIMESTAMP,
    session_end TIMESTAMP,
    pickup_location_id INTEGER,
    trip_count BIGINT,
    PRIMARY KEY (session_start, pickup_location_id)
);

CREATE TABLE hourly_revenue (
    window_start TIMESTAMP(3) PRIMARY KEY,
    window_end TIMESTAMP(3),
    total_tip_amount DOUBLE PRECISION
);
```

### 4. Consume with Kafka and Process with Flink

```Bash:
# 3.1 Consume data
cd src
uv run python -m consumers.consumer_green_db

# 3.2 Start Flink Streaming Job 1 - Pickup demande by 5 minutes
docker compose exec jobmanager ./bin/flink run \
	-py /opt/src/job/pickup_demand_5mn_job.py \
    --pyFiles /opt/src -d
# Run SQL to get the answer, then cancel the job

# 3.3 Start Job 2 - Pickups by session (5 minutes gap)
docker compose exec jobmanager ./bin/flink run \
	-py /opt/src/job/session_pickups_job.py \
    --pyFiles /opt/src -d
# Run SQL, get the answer, then Cancel the job.

# 3.4 Start Job 3 - hourly revenue
docker compose exec jobmanager ./bin/flink run \
	-py /opt/src/job/hourly_revenue_job.py \
    --pyFiles /opt/src -d
# Run SQL, get the answer, then Cancel the job.
```


## III. Commands and Queries for Questions

### Q1 
docker exec -it m7_proj_kafka_flink-redpanda-1 rpk version

### Q2
see **Quick Start -> 2.3 Produce Events Data**

### Q3-Q6

```SQL
--Q3
SELECT COUNT(1) FROM processed_events WHERE trip_distance > 5;

--Q4
SELECT pickup_location_id, trip_count FROM pickup_demand_5min ORDER BY trip_count DESC LIMIT 3;

--Q5
SELECT * FROM session_pickups ORDER BY trip_count DESC LIMIT 1;

--Q6
SELECT window_start, total_tip_amount FROM hourly_revenue ORDER BY total_tip_amount DESC LIMIT 1;
```


## IV. References

- [M7 Streaming - DTC Data Engineering Zoomcamp 2026](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/07-streaming)

- [Homework M7 Repository - cll](https://github.com/clinliang/dez2026-homework/tree/main/m7_proj_kafka_flink)

- [Homework M7 Questions](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/07-streaming/homework.md)
