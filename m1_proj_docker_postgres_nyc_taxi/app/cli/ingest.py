#!/usr/bin/env python
# coding: utf-8

import click

from app.ingest.local_parquet_trips import run as ingest_parquet
from app.ingest.url_csv_trips import run as ingest_trips
from app.ingest.url_csv_zones import run as ingest_zones


@click.group()
def cli():
    """
    Data ingestion command line interface.
    """
    pass

# ----------------------------------------------------------------------
# Local Parquet ingestion
# ----------------------------------------------------------------------
@cli.command("local-parquet-trips")
@click.option(
    "--file",
    "parquet_file",
    required=True,
    help="Path to the local parquet file to ingest",
)
@click.option(
    "--target-table",
    required=True,
    help="Target table name in PostgreSQL",
)
def local_parquet(parquet_file: str, target_table: str):
    """
    Ingest a local parquet file into PostgreSQL.
    """
    ingest_parquet(
        parquet_file=parquet_file,
        target_table=target_table,
    )


# ----------------------------------------------------------------------
# Taxi zones dimension table ingestion
# ----------------------------------------------------------------------
@cli.command("url-csv-zones")
@click.option(
    "--target-table",
    default="dim_taxi_zone",
    show_default=True,
    help="Target table name for taxi zones dimension",
)
def zones(target_table: str):
    """
    Ingest taxi zones lookup table from a public CSV URL.
    """
    ingest_zones(
        target_table=target_table,
    )


# ----------------------------------------------------------------------
# Remote CSV ingestion (monthly data)
# ----------------------------------------------------------------------
@cli.command("url-csv-trips")
@click.option(
    "--year",
    required=True,
    type=int,
    help="Year of the dataset to ingest",
)
@click.option(
    "--month",
    required=True,
    type=int,
    help="Month of the dataset to ingest",
)
@click.option(
    "--target-table",
    required=True,
    help="Target table name in PostgreSQL",
)
def url_csv(year: int, month: int, target_table: str):
    """
    Ingest a monthly CSV dataset from a remote URL into PostgreSQL.
    """
    ingest_trips(
        year=year,
        month=month,
        target_table=target_table,
    )


if __name__ == "__main__":
    cli()
