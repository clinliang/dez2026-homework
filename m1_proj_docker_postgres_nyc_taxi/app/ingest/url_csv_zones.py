#!/usr/bin/env python
# coding: utf-8

### taxi zones data from github

print("=== INGEST_URL_CSV_ZONES.PY LOADED ===")

# libraries
import pandas as pd
from sqlalchemy import create_engine
import click

# NEW: import access layer
from app.config.db_config import get_pg_config


# parameters - data types (schema reference = taxi_zone_lookup.csv)
dtype = {
    "LocationID": "Int64",
    "Borough": "string",
    "Zone": "string",
    "service_zone": "string",
}


### main ingestion function
def run(
    target_table: str = "taxi_zone_lookup",
    url: str = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv",
):
    """
    Ingest taxi zone lookup CSV into PostgreSQL.

    PostgreSQL connection parameters are resolved via environment variables
    using app.config.db_config.get_pg_config().
    """
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
        print("STEP 2: Reading taxi zone lookup CSV")
        print("=" * 60)

        df = pd.read_csv(
            url,
            dtype=dtype,
        )

        print("\n" + "=" * 60)
        print(f"STEP 3: Writing data to table '{target_table}'")
        print("=" * 60)

        df.to_sql(
            name=target_table,
            con=engine,
            if_exists="replace",
            index=False,
        )

        print(f"\n✓ STEP 4: Ingestion completed into '{target_table}' table.")

    except Exception as e:
        print(f"✗ Error during ingestion: {e}")
        return

    finally:
        if "engine" in locals():
            engine.dispose()
