import os
from google.cloud import bigquery

def run_transform():
    # BigQuery Client (Uses the env var for credentials)
    client = bigquery.Client()

    project_id = "nytaxi-yellow-cll"
    dataset_id = "m3_nytaxi_yellow_bq"
    
    native_table = f"{project_id}.{dataset_id}.yellow_tripdata_non_partitioned"
    external_table = f"{project_id}.{dataset_id}.external_yellow_tripdata"

    sql = f"""
        CREATE OR REPLACE TABLE `{native_table}` AS
        SELECT * FROM `{external_table}`;
    """

    print(f"🔄 Creating Native Table: {native_table}...")
    query_job = client.query(sql)
    query_job.result() 
    print("✅ BigQuery transformation complete!")

if __name__ == "__main__":
    run_transform()