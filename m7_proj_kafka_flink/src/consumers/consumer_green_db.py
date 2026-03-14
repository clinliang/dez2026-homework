from kafka import KafkaConsumer
import psycopg2
from datetime import datetime
import math

from models import greentrip_deserializer

# 1. Kafka consumer setup

server = "localhost:9092"
topic_name = "green-trips"

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=[server],
    auto_offset_reset="earliest",   # read from beginning
    enable_auto_commit=False,
    group_id="greentrip-db",
    value_deserializer=greentrip_deserializer
)

# 2. PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgres"
)

# conn.autocommit = True

cur = conn.cursor()

print(f"Listening to topic '{topic_name}' and writing to PostgreSQL...")

# 3. Create table if not exists

cur.execute("""
CREATE TABLE IF NOT EXISTS processed_events (
    PULocationID INTEGER,
    DOLocationID INTEGER,
    trip_distance DOUBLE PRECISION,
    tip_amount DOUBLE PRECISION,
    total_amount DOUBLE PRECISION,
    pickup_datetime TIMESTAMP
)
""")

conn.commit()

# 4. Consume messages and insert into DB

count = 0

for message in consumer:
    greentrip = message.value
    pickup_dt = datetime.fromisoformat(greentrip.lpep_pickup_datetime)

    row = (
        greentrip.PULocationID,
        greentrip.DOLocationID,
        greentrip.trip_distance,
        greentrip.tip_amount,
        greentrip.total_amount,
        pickup_dt
        )

    try:
        cur.execute(
            """
            INSERT INTO processed_events
            (PULocationID, DOLocationID, trip_distance, tip_amount, total_amount, pickup_datetime)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            row
        )

        count += 1
        if count % 100 == 0:
            conn.commit()
            consumer.commit()
            print(f"Inserted {count} records")    

    except Exception as e:
        print(f"Error occurred at offset {message.offset} : {row}")
        print(e)

        conn.rollback()  # rollback the transaction to avoid partial commits
        continue

conn.commit()
consumer.commit()

consumer.close()
print("Consumer closed.")

cur.close()
conn.close()
print("Connection to postgreSQL closed.")


