"""@bruin

name: ingestion.trips
type: python
image: python:3.11
connection: duckdb-default

materialization:
  type: table
  strategy: append

columns:
  - name: vendor_id
    type: integer
    description: Taxi vendor identifier

  - name: pickup_datetime
    type: timestamp
    description: Trip pickup timestamp

  - name: dropoff_datetime
    type: timestamp
    description: Trip dropoff timestamp

  - name: passenger_count
    type: integer
    description: Number of passengers

  - name: trip_distance
    type: double
    description: Trip distance in miles

  - name: ratecode_id
    type: integer
    description: Rate code identifier

  - name: store_and_fwd_flag
    type: string
    description: Whether trip record was stored before sending

  - name: pickup_location_id
    type: integer
    description: TLC pickup location id

  - name: dropoff_location_id
    type: integer
    description: TLC dropoff location id

  - name: payment_type
    type: integer
    description: Payment method code

  - name: fare_amount
    type: double
    description: Base fare amount

  - name: extra
    type: double
    description: Extra charges

  - name: mta_tax
    type: double
    description: MTA tax amount

  - name: tip_amount
    type: double
    description: Tip amount

  - name: tolls_amount
    type: double
    description: Tolls amount

  - name: improvement_surcharge
    type: double
    description: Improvement surcharge

  - name: total_amount
    type: double
    description: Total trip amount

  - name: congestion_surcharge
    type: double
    description: Congestion surcharge

  - name: airport_fee
    type: double
    description: Airport fee

  - name: taxi_type
    type: string
    description: Taxi type (yellow or green)

  - name: extracted_at
    type: timestamp
    description: Ingestion timestamp

@bruin"""

import os
import json
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/"


def month_range(start_date: str, end_date: str):
    """Generate list of (year, month) between two dates"""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    current = start.replace(day=1)
    while current <= end:
        yield current.year, current.month
        current += relativedelta(months=1)


def build_url(taxi_type: str, year: int, month: int):
    return f"{BASE_URL}{taxi_type}_tripdata_{year}-{month:02d}.parquet"


def materialize():

    start_date = os.getenv("BRUIN_START_DATE")
    end_date = os.getenv("BRUIN_END_DATE")

    vars_json = os.getenv("BRUIN_VARS", "{}")
    vars_dict = json.loads(vars_json)
    taxi_types = vars_dict.get("taxi_types", ["yellow"])

    all_dfs = []

    for taxi_type in taxi_types:
        for year, month in month_range(start_date, end_date):
            url = build_url(taxi_type, year, month)

            try:
                df = pd.read_parquet(url)

                # normalize column names
                df.columns = [c.lower() for c in df.columns]

                # rename common TLC differences
                df = df.rename(columns={
                    "vendorid": "vendor_id",
                    "tpep_pickup_datetime": "pickup_datetime",
                    "tpep_dropoff_datetime": "dropoff_datetime",
                    "lpep_pickup_datetime": "pickup_datetime",
                    "lpep_dropoff_datetime": "dropoff_datetime",
                    "pulocationid": "pickup_location_id",
                    "dolocationid": "dropoff_location_id",
                    "ratecodeid": "ratecode_id"
                })

                df["taxi_type"] = taxi_type
                df["extracted_at"] = datetime.utcnow()

                all_dfs.append(df)

                print(f"Loaded {taxi_type} {year}-{month:02d}")

            except Exception as e:
                print(f"Skipping {url}: {e}")

    if not all_dfs:
        return pd.DataFrame()

    final_df = pd.concat(all_dfs, ignore_index=True)

    return final_df