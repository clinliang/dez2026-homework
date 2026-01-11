#!/usr/bin/env python
# coding: utf-8


# libaries
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click


# parameters - data types - df_iter
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

# parameters - parse dates - df_iter
parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


### main ingestion function
def run(
    pg_user: str = 'root',
    pg_pass: str = 'root',
    pg_host: str = 'localhost',
    pg_db: str = 'ny_taxi',
    pg_port: int = 5432,
    target_table: str = 'yellow_taxi_data',  # Added parameter
    year: int = 2021,
    month: int = 1,
):
    # parameters - df_iter
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    url = prefix + f'yellow_tripdata_{year}-{month:02d}.csv.gz'

    # parameters - df_iter
    chunksize = 100000

    try:
        engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

        # ingestion process
        df_iter = pd.read_csv(
            url,
            dtype=dtype,
            parse_dates=parse_dates,
            iterator=True,
            chunksize=chunksize,
        )
        
        first = True

        # for loop to ingest data chunk by chunk
        for df_chunk in tqdm(df_iter):
            if first:
                df_chunk.head(0).to_sql(
                    name=target_table, 
                    con=engine, 
                    if_exists='replace',
                    index=False
                    )
                first = False

            df_chunk.to_sql(
                name=target_table, 
                con=engine, 
                if_exists='append',
                index=False
                )

        print(f"\nIngestion completed for {year}-{month:02d} into '{target_table}' table.")

    except Exception as e:
        print(f"✗ Error during ingestion: {e}")
        return
        
    finally:
        if 'engine' in locals():
            engine.dispose()

@click.command()
@click.option('--pg-user', default='root', show_default=True, help='Postgres user')
@click.option('--pg-pass', default='root', show_default=True, help='Postgres password')
@click.option('--pg-host', default='localhost', show_default=True, help='Postgres host')
@click.option('--pg-db', default='ny_taxi', show_default=True, help='Postgres database')
@click.option('--pg-port', default=5432, show_default=True, type=int, help='Postgres port')
@click.option('--target_table', default='yellow_taxi_data', show_default=True, help='Target table name')  # Added CLI option
@click.option('--year', default=2021, show_default=True, type=int, help='Year of data')
@click.option('--month', default=1, show_default=True, type=int, help='Month of data (1-12)')
def cli(pg_user, pg_pass, pg_host, pg_db, pg_port, target_table, year, month):
    run(
        pg_user=pg_user,
        pg_pass=pg_pass,
        pg_host=pg_host,
        pg_db=pg_db,
        pg_port=pg_port,
        target_table=target_table,  # Pass it through
        year=year,
        month=month,
    )


#  end of main ingestion function
if __name__ == '__main__':
    cli()