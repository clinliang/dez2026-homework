# Repository Structure

This repository is organized by responsibility, not by tool.

## Core Philosophy
- ingestion is separated from transformation
- dbt handles business logic
- experiments are isolated

## Example Structure

core/           # ingestion, loaders, shared utils
pipelines/      # data pipelines (source-oriented)
models/         # dbt models
exploration/    # research & learning
exercise/       # tutorials & courses
docs/           # governance & documentation