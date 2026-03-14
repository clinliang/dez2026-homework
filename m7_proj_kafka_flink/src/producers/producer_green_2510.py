import pandas as pd
from kafka import KafkaProducer
from time import time

from models import GreenTrip, greentrip_from_row, greentrip_serializer

# 1. data ingest

# Fetching the raw data first to understand the schema
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-10.parquet"
columns = [
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "passenger_count",
    "trip_distance",
    "tip_amount",
    "total_amount",
]

df = pd.read_parquet(url, columns=columns)

# 2. setup kafka producer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=greentrip_serializer
)

# 3. send records to kafka

topic_name = "green-trips"

t0 = time()

for _, row in df.iterrows():
    greentrip = greentrip_from_row(row)
    producer.send(topic_name, value=greentrip)
producer.flush()

t1 = time()
print(f'took {(t1 - t0):.2f} seconds')