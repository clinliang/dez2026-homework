#!/usr/bin/env python
# coding: utf-8

### yellew data from github

print("=== INGEST_URL_CSV.PY LOADED ===")

# libraries
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

# NEW: access layer
from app.config.db_config import get_pg_config


# parameters - data types
dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

# parameters - parse dates
parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


### main ingestion function
def run(
    target_table: str = "yellow_taxi_data",
    year: int = 2021,
    month: int = 1,
):
    """
    Ingest yellow taxi CSV data from remote URL into PostgreSQL.

    PostgreSQL connection parameters are resolved via environment variables
    using app.config.db_config.get_pg_config().
    """
    # build URL
    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"
    url = prefix + f"yellow_tripdata_{year}-{month:02d}.csv.gz"

    chunksize = 100_000
    pg = get_pg_config()

    try:
        print("\n" + "=" * 60)
        print(f"STEP 1: Connecting to database - {pg['host']}:{pg['port']}")
        print("=" * 60)

        engine = create_engine(
            f"postgresql://{pg['user']}:{pg['password']}@"
            f"{pg['host']}:{pg['port']}/{pg['database']}"
        )

        print("\n" + "=" * 60)
        print(f"STEP 2: Reading CSV data for {year}-{month:02d}")
        print("=" * 60)

        df_iter = pd.read_csv(
            url,
            dtype=dtype,
            parse_dates=parse_dates,
            iterator=True,
            chunksize=chunksize,
        )

        first = True

        print("\n" + "=" * 60)
        print(f"STEP 3: Ingesting data into '{target_table}'")
        print("=" * 60)

        for df_chunk in tqdm(df_iter):
            if first:
                df_chunk.head(0).to_sql(
                    name=target_table,
                    con=engine,
                    if_exists="replace",
                    index=False,
                )
                first = False

            df_chunk.to_sql(
                name=target_table,
                con=engine,
                if_exists="append",
                index=False,
            )

        print(
            f"\n✓ STEP 4: Ingestion completed for {year}-{month:02d} "
            f"into '{target_table}' table."
        )

    except Exception as e:
        print(f"✗ Error during ingestion: {e}")
        return

    finally:
        if "engine" in locals():
            engine.dispose()
