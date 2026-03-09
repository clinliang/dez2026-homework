#!/usr/bin/env python
# coding: utf-8

import argparse
from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()

parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)

args = parser.parse_args()

spark = SparkSession.builder \
    .appName('pq_to_bq') \
    .getOrCreate()

spark.conf.set('temporaryGcsBucket', 'spark_nytaxi_cll') # new for bq

df = spark.read.parquet(args.input)

df.write.format("bigquery") \
    .option("writeMethod", "direct") \
    .mode("overwrite") \
    .save(args.output)