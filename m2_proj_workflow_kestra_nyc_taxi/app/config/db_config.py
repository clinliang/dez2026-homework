import os


def get_pg_config():
    """
    Read PostgreSQL connection configuration from environment variables,
    with safe defaults for Docker-based local development.
    """
    return {
        "host": os.getenv("PGHOST", "pgdatabase"),
        "port": int(os.getenv("PGPORT", 5432)),
        "user": os.getenv("PGUSER", "root"),
        "password": os.getenv("PGPASSWORD", "root"),
        "database": os.getenv("PGDATABASE", "ny_taxi"),
    }
