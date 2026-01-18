# NYC Taxi Ingest — Docker + Postgres

**Version 5.1: Modularizes the setup with a unified CLI, externalized environment configs, and isolates the Python environment in `/opt/venv` to prevent volume conflicts.**

Small Docker Compose setup to ingest NYC taxi data (local Parquet or URL CSV) into a local Postgres database.

# Github : 

# Summary
I. Quick Start
II. Homework Bash Commands(questions 1 & 3)
III. Homework SQL Queries(question 3-6)
IV. Data sources
V. References



## I. Quick Start
> Note: This setup is optimized for local development and homework execution.
> For a full project directory overview, see `structure.txt`.

1. Download the parquet file and place it in `./data/` (e.g., `green_tripdata_2025-11.parquet`)
2. Start the full stack: `docker-compose up -d`
3. Access to the database:
	- From host : `pgcli -h localhost -p 5433 -U root ny_taxi`
	- From container : `docker exec -it ny_taxi_pgdatabase psql -U root -d ny_taxi`(from container)
4. Access pgAdmin: http://localhost:8085 (login: admin@admin.com / password: root)
5. Run ingestion jobs using the "taxi-ingest" service and CLI entrypoint: 
`docker-compose run --rm taxi-ingest python -m app.cli.ingest [COMMAND] [OPTIONS]`




## II. Homework Bash Commands (Questions 1 & 3)

### Question 1. Docker image innpsection (pip version of the image python:3.13)
```Bash:
$ PS1="(m1_proj)$"
(m1_proj)$ docker run -it --rm -v $(pwd)/test:/app/test --entrypoint=bash python:3.13.11-slim
root@6591db134bf0:/# pip --version
```

### Question 3. Counting short trips (<=1 mile, Nov 2025)
```Bash:
#Base Command: 
docker-compose run --rm taxi-ingest python -m app.cli.ingest [COMMAND] [OPTIONS]
#Command & Options by Task :
	- `url-csv-zones --target-table dim_taxi_zone`
	- `url-csv-trips --target-table yellow_taxi_2021_1 --year 2021 --month 1`
	- `local-parquet-trips --target-table green_taxi_data_2025_11 --file /app/data/green_tripdata_2025-11.parquet`
```

docker-compose run --rm taxi-ingest python -m app.cli.ingest url-csv-zones --target-table dim_taxi_zone

docker-compose run --rm taxi-ingest python -m app.cli.ingest local-parquet-trips --target-table green_taxi_data_2025_11 --file /app/data/green_tripdata_2025-11.parquet


docker-compose run --rm taxi-ingest python -m app.cli.ingest url-csv-trips --target-table yellow_taxi_2021_1 --year 2021 --month 1


## III. Homework SQL Queries (Questions 3-6)

### Question 3. Trips with distance <= 1 mile (Nov. 2025)
Result: 8,007

```SQL:
SELECT 
	COUNT(*) AS nb_trips_25nov_less_or_equal_1mile
FROM green_taxi_trips_2025_11
WHERE trip_distance <= 1
	AND lpep_pickup_datetime >= '2025-11-01' 
	AND lpep_pickup_datetime < '2025-12-01';
```

### Question 4. Pickup day with the longest trip (<100 miles)
Result: 2025-11-14

```SQL:
SELECT DISTINCT 
	CAST(lpep_pickup_datetime AS DATE) AS pickup_date_the_farest_trip
FROM green_taxi_trips_2025_11
WHERE trip_distance = (
	SELECT MAX(trip_distance) 
	FROM green_taxi_trips_2025_11
	WHERE trip_distance < 100
  );
```

### Question 5. Pickup zone with largest total_amount (Nov 18, 2025)
Result: East Harlem North

```SQL
WITH amount_by_zone AS (
	SELECT "PULocationID", SUM(total_amount) AS zone_amount
	FROM green_taxi_trips_2025_11
	WHERE CAST("lpep_pickup_datetime" AS DATE) = '2025-11-18'
	GROUP BY "PULocationID"
	),
SELECT z."Zone"
FROM amount_by_zone a
JOIN dim_taxi_zone z ON z."LocationID" = b."PULocationID"
ORDER BY a.zone_amount DESC
LIMIT 1;	
```

### Question 6. Drop-off zone with highest tip (pickup:East Harlem North)
Result: Yorkville West

```SQL:
SELECT z1."Zone", MAX("tip_amount") AS max_tip
FROM green_taxi_trips_2025_11 t
LEFT JOIN dim_taxi_zone z1 ON t."DOLocationID" = z1."LocationID"
JOIN dim_taxi_zone z2 ON t."PULocationID" = z2."LocationID"
WHERE z2."Zone" = 'East Harlem North'
GROUP BY z1."Zone"
ORDER BY max_tip DESC
LIMIT 1
```



## IV. Data sources

### Green trips (2025-11, Parquet):
https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
From https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

### Taxi zone lookup (CSV)
https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
OR https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv

### Yellow trips (2021-01, CSV)
https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz



## V. References

# Homework instruction:
https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/01-docker-terraform/homework.md

# Submission URL (<27/01/2025):
https://courses.datatalks.club/de-zoomcamp-2026/homework/hw1