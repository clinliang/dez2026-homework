#!/usr/bin/env python
# coding: utf-8

#If you don't like using the first flag:

first_chunk = next(df_iter)

first_chunk.head(0).to_sql(
    name="yellow_taxi_data",
    con=engine,
    if_exists="replace"
)

print("Table created")

first_chunk.to_sql(
    name="yellow_taxi_data",
    con=engine,
    if_exists="append"
)

print("Inserted first chunk:", len(first_chunk))

for df_chunk in df_iter:
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append"
    )
    print("Inserted chunk:", len(df_chunk))



""" V1
# libaries
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm


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
def run():
    # parameters - create engine
    pg_user = 'root'
    pg_password = 'root'
    pg_host = 'localhost'
    pg_database = 'ny_taxi'
    pg_port = 5432

    # parameters - url - df_iter
    year = 2021
    month = 1

    # parameters - df_iter
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    url = prefix + f'yellow_tripdata_{year}-{month:02d}.csv.gz'

    # parameters - df_iter
    chunksize = 100000
    target_table = 'yellow_taxi_data'

    engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}')

    # ingestion process
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=100000,
    )

    # for loop to ingest data chunk by chunk
    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.head(0).to_sql(
                name='{target_table}', 
                con=engine, 
                if_exists='replace')
            first = False

        df_chunk.to_sql(
            name='{target_table}', 
            con=engine, 
            if_exists='append')

#  end of main ingestion function
if __name__ == '__main__':
    run()
"""

