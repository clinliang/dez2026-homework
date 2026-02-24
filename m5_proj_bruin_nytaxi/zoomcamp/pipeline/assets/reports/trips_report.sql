/* @bruin

# Docs:
# - SQL assets: https://getbruin.com/docs/bruin/assets/sql
# - Materialization: https://getbruin.com/docs/bruin/assets/materialization
# - Quality checks: https://getbruin.com/docs/bruin/quality/available_checks

# TODO: Set the asset name (recommended: reports.trips_report).
name: reports.trips_report

# TODO: Set platform type.
# Docs: https://getbruin.com/docs/bruin/assets/sql
# suggested type: duckdb.sql
type: duckdb.sql

# TODO: Declare dependency on the staging asset(s) this report reads from.
depends:
  - staging.trips

# TODO: Choose materialization strategy.
# For reports, `time_interval` is a good choice to rebuild only the relevant time window.
# Important: Use the same `incremental_key` as staging (e.g., pickup_datetime) for consistency.
materialization:
  type: table
  # suggested strategy: time_interval
  strategy: time_interval
  # TODO: set to your report's date column
  incremental_key: trip_date
  # TODO: set to `date` or `timestamp`
  time_granularity: date

# TODO: Define report columns + primary key(s) at your chosen level of aggregation.
columns: 
  - name: trip_date
    type: date
    description: date of the trip (derived from pickup_datetime)
    primary_key: true
  - name: taxi_type
    type: varchar
    description: type of taxi (e.g., yellow, green)
    primary_key: true
  - name: payment_type_name
    type: varchar
    description: payment type (e.g., credit card, cash)
    primary_key: true
  - name: trip_count
    type: BIGINT
    description: total nuber of trips
    checks:
      - name: positive
  - name: total_passengers
    type: BIGINT
    description: total number of passengers
    checks:
      - name: non_negative
  - name: total_distance
    type: DOUBLE
    description: total distance traveled in miles
    checks:
      - name: non_negative
  - name: total_fare
    type: DOUBLE
    description: total fare amount
 #   checks:
 #     - name: non_negative --- IGNORE --- (some trips may have negative fare due to adjustments/refunds)
  - name: total_tips
    type: DOUBLE
    description: total tip amount
    checks:
      - name: non_negative
  - name: avg_fare
    type: DOUBLE
    description: average fare amount per trips
  - name: avg_trip_distance
    type: DOUBLE
    description: average trip distance in miles
  - name: avg_passengers
    type: DOUBLE
    description: average number of passengers per trip
  
custom_checks:
  - name: row_count_postive
    description: ensure the report is not empty
    query: SELECT COUNT(*) > 0 FROM reports.trips_report
    value: 1

@bruin */

-- Purpose of reports:
-- - Aggregate staging data for dashboards and analytics
-- Required Bruin concepts:
-- - Filter using `{{ start_datetime }}` / `{{ end_datetime }}` for incremental runs
-- - GROUP BY your dimension + date columns

SELECT
   -- TODO: replace with your aggregation logic
   CAST(pickup_datetime AS date) AS trip_date,
   taxi_type,
   payment_type_name,

   -- count metrics
   COUNT(*) AS trip_count,
   SUM(COALESCE(passenger_count, 0)) AS total_passengers,

   -- distance metrics
    SUM(COALESCE(trip_distance, 0)) AS total_distance,

  -- revenue metrics
  SUM(COALESCE(tip_amount, 0)) AS total_tips,
  SUM(COALESCE(fare_amount, 0)) AS total_fare,
  SUM(COALESCE(total_amount, 0)) AS total_revenue,

  -- average metrics
  AVG(COALESCE(trip_distance, 0)) AS avg_trip_distance,
  AVG(COALESCE(passenger_count, 0)) AS avg_passengers,
  AVG(COALESCE(trip_distance, 0)) AS avg_trip_distance
  
FROM staging.trips
WHERE pickup_datetime >= '{{ start_datetime }}'
  AND pickup_datetime < '{{ end_datetime }}'
GROUP BY
  CAST(pickup_datetime AS date),
  taxi_type,
  payment_type_name