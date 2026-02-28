# NYC Taxi Data Tranformation  — dbt core + DuckDB

**Version 4.1** : Data transformation using **dbt core** on top of **DuckDB** enables a local ELT architecture that ingests NYC Taxi data (Yellow, Green, FHV) and materializes analytics-ready data marts.


# Summary

- [I. Architecture](#i-architecture)
- [II. Quick Start](#ii-quick-start)
- [III. Homework Queries](#iii-homework-queries)
- [IV. References](#iv-references)


## I. Architecture

This project implements a **local analytics engineering** pipeline using Python ingestion, **DuckDB**, **dbt core** (with OOM-safe temp configuration), and bash-based **bucket processing**  to produce analytics-ready datasets. For a complete project directory overview, see `structure.txt`.

### System Architecture

```text
Raw CSV Data
    ↓  (Python ingestion)
DuckDB (raw layer)
    ↓  (dbt staging)
Staging
    ↓  (dbt intermediate) 
Intermediate (bash bucketed execution → int_trips)
    ↓  (dbt marts)
Marts
    ↓
Analytics Queries
```

> Note on Out-of-Memory Mitigation : 
- `int_trips` is processed in 10 buckets via bash to reduce memory usage.
- Intermediate models are materialization as tables, with a custom temp directory configured in dbt to prevent OOM. 


## II. Quick Start

```Bash:
# 1.Setup
uv init && uv add dbt-duckdb && dbt init

# 2.Ingest data
uv run ingest.py

# 3.Prepare dbt
uv run dbt debug
uv run dbt seed
uv run dbt deps

# 4.Build Models
uv run dbt run --select staging
uv run dbt run --select int_trips_unioned
./run_int_trips.sh # bucketed int_trips build
uv run dbt run --select dim_zones dim_vendors
uv run dbt run --select fct_models

# 5.Docs
uv run dbt docs generate
uv run dbt docs serve

# 6.Clean(Optional)
uv run dbt clean
```


## III. Homework Queries

```SQL:
-- Q3. Counting Records in fct_monthly_zone_revenue
$ duckdb taxi_rides_ny.duckdb "select count(*) from prod_marts.monthly_revenue_per_location;"

-- Q4. Best Performing Zone for Green Taxis (2020)
$ duckdb taxi_rides_ny.duckdb "select pickup_zone, monthly_total_amount as revenue_monthly_total_amount \
from prod_marts.monthly_revenue_per_location \
where service_type = 'Green' and \
    revenue_month >= '2020-01-01' and revenue_month < '2021-01-01' \
order by monthly_total_amount desc \
limit 1;"

-- Q5. Green Taxi Trip Counts (October 2019)
$ duckdb taxi_rides_ny.duckdb "select service_type, revenue_month, sum(total_number_trips) as total_monthly_trips \
from prod_marts.monthly_revenue_per_location \
where service_type = 'Green' and \
    revenue_month >= '2019-10-01' and revenue_month < '2019-11-01' \
group by service_type, revenue_month;"

-- Q6. What is the count of records in stg_fhv_tripdata?
$ duckdb taxi_rides_ny.duckdb "select count(*) from prod_staging.stg_fhv_tripdata;"
```


## IV. References

- [M4 dbt Repository - DTC Data Engineering Zoomcamp 2026](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/04-analytics-engineering)

- [Homework M4 Repository - cll](https://github.com/clinliang/dez2026-homework/tree/main/m4_proj_dbt_taxi_rides_ny)

- [Homework M4 instruction](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/04-analytics-engineering/homework.md)