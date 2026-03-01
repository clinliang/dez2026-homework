import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig


@dlt.source
# no auth required for this public endpoint
# the source simply paginates through the API until an empty page is returned
# the configuration mirrors the example from the "@dlt rest api" tutorial
# with a page-number paginator starting at 1

def taxi_pipeline_rest_api_source():
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"
        },
        "resources": [
            {
                "name": "taxi",
                "endpoint": {
                    # the base url already returns the first page, so no extra path
                    "paginator": {
                        "type": "page_number",
                        "base_page": 1,
                        # stop_after_empty_page defaults to True, which matches
                        # the requirement to halt when an empty page is returned
                    }
                }
            }
        ]
    }
    yield from rest_api_resources(config)


pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",
    destination="duckdb",
    refresh="drop_sources",
    progress="log",
)


if __name__ == "__main__":
    # run the pipeline and print a brief summary only (avoids dumping all rows)
    try:
        load_info = pipeline.run(taxi_pipeline_rest_api_source())
        print("pipeline finished, load info:", load_info)
    except Exception as e:
        # show the error and propagate so the exit code remains non-zero
        print("pipeline error:", e)
        raise
