import duckdb
import requests
from pathlib import Path
from tqdm import tqdm

BASE_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download"
INGEST_CONFIG = [
    ("yellow", 2019, 1, 2020, 12),  
    ("green", 2019, 1, 2020, 12),  
    ("fhv", 2019, 1, 2019, 12)      
]

def download_and_convert_files(taxi_type, start_y, start_m, end_y, end_m):
    data_dir = Path("data") / taxi_type
    data_dir.mkdir(exist_ok=True, parents=True)

    start_total = start_y * 12 + (start_m - 1)
    end_total = end_y * 12 + (end_m - 1)
    months = [(i // 12, (i % 12) + 1) for i in range(start_total, end_total + 1)]
    process_files = []

    tqdm.write(f"\n--- 🛠️  Checking/Downloading {taxi_type.upper()} taxi data ({start_y}-{start_m:02d} to {end_y}-{end_m:02d}) ---")

    with duckdb.connect() as con: # auto close connection 
        con.execute("SET memory_limit = '2GB'")

        for year, month in tqdm(months, desc=f"Files for {taxi_type}"): # tqdm progress bar
            parquet_filename = f"{taxi_type}_tripdata_{year}-{month:02d}.parquet"
            parquet_filepath = data_dir / parquet_filename
            process_files.append(parquet_filepath)

            if not parquet_filepath.exists():
                csv_gz_filepath = parquet_filepath.with_suffix('.csv.gz')

                try:                
                    response = requests.get(f"{BASE_URL}/{taxi_type}/{csv_gz_filepath.name}", stream=True)
                    response.raise_for_status()

                    with open(csv_gz_filepath, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)

                    con.execute(f"""
                        COPY (
                            SELECT * 
                            FROM read_csv_auto(
                                '{csv_gz_filepath}',
                                strict_mode=false,
                                sample_size=-1,
                                all_varchar=true,
                                ignore_errors=true
                            )
                        ) TO '{parquet_filepath}' (FORMAT PARQUET)
                    """)
                    # sample_size=-1 infer shema from the whole table
                    # all_varchar=true: convert all columns to varchar str to avoid type inference issues.  
                    # ignore_errors=true: might cause data loss 
                    csv_gz_filepath.unlink() # delete the gz file after conversion

                except Exception as e:
                    tqdm.write(f"Warning: Could not process {taxi_type} {year}-{month:02d}: {e}")   

        return process_files

def update_gitignore():
    gitignore_path = Path(".gitignore")
    content = gitignore_path.read_text() if gitignore_path.exists() else ""
    if 'data/' not in content:
        with open(gitignore_path, 'a') as f:
            f.write('\n# Data directory\ndata/\n' if content else '# Data directory\ndata/\n')

if __name__ == "__main__":
    update_gitignore()
    db_path = "taxi_rides_ny.duckdb"

    print("\n💾 Loading data into DuckDB...")
    
    with duckdb.connect(db_path) as main_con:
        main_con.execute("SET memory_limit = '4GB'")
        main_con.execute("CREATE SCHEMA IF NOT EXISTS prod")

        for taxi_type, start_y, start_m, end_y, end_m in tqdm(INGEST_CONFIG, desc="Overall Progress"):
            target_files = download_and_convert_files(taxi_type, start_y, start_m, end_y, end_m)

            tqdm.write(f"📥 Loading {taxi_type} into 'prod' schema...")
            main_con.execute(f"DROP TABLE IF EXISTS prod.{taxi_type}_tripdata")

            valid_files = [str(f) for f in target_files if f.exists()]

            if valid_files:
                main_con.execute(f"""
                    CREATE TABLE prod.{taxi_type}_tripdata AS 
                    SELECT * FROM read_parquet({valid_files}, union_by_name=true)
                """)
            else:
                tqdm.write(f"  ⚠️ No valid files found for {taxi_type}, skipping table creation.")

    print(f"\n✨ Done! Database is clean and ready at {db_path}")

