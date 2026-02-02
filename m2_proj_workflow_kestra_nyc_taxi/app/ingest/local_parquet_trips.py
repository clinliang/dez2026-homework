#!/usr/bin/env python
# coding: utf-8

### local parquet ingestion

print("=== INGEST_LOCAL_PARQUET.PY LOADED ===")

# libraries
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click
from pathlib import Path

# NEW: access layer
from app.config.db_config import get_pg_config


# parameters - data types (same as CSV version for consistency)
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
    "congestion_surcharge": "float64",
}

# parameters - parse dates
parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
]


### main ingestion function for local parquet files
def run(
    parquet_file: str,
    target_table: str = "yellow_taxi_data",
):
    """
    Ingest local parquet file into PostgreSQL database.

    PostgreSQL connection parameters are resolved via environment variables
    using app.config.db_config.get_pg_config().
    """
    parquet_file = Path(parquet_file)
    if not parquet_file.exists():
        print(f"✗ Error: File not found: {parquet_file}")
        return

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
        print(f"STEP 2: Reading Parquet file - {parquet_file.name}")
        print("=" * 60)

        df_parquet = pd.read_parquet(parquet_file)
        print(f"   Loaded {len(df_parquet):,} rows, {len(df_parquet.columns)} columns")

        # convert to chunked iterator
        df_iter = (
            df_parquet.iloc[i : i + chunksize]
            for i in range(0, len(df_parquet), chunksize)
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
            f"\n✓ STEP 4: Ingestion completed - "
            f"{len(df_parquet):,} rows into '{target_table}' table."
        )

    except Exception as e:
        print(f"✗ Error during ingestion: {e}")
        return

    finally:
        if "engine" in locals():
            engine.dispose()