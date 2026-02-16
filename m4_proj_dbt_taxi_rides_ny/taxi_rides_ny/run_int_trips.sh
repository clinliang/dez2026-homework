#!/bin/bash

TOTAL_BUCKETS=10

echo "Starting bucketed dbt run..."

for ((i=0; i<$TOTAL_BUCKETS; i++))
do
  echo "--------------------------------------"
  echo "Running bucket: $i"
  echo "--------------------------------------"

  uv run dbt run --select int_trips --vars "{bucket: $i}"

  if [ $? -ne 0 ]; then
    echo "Bucket $i failed. Stopping execution."
    exit 1
  fi
done

echo "All buckets completed successfully."
