import inspect
from app.ingest.local_parquet import ingest_local_parquet


def test_ingest_local_parquet_signature():
    sig = inspect.signature(ingest_local_parquet)

    assert "file_path" in sig.parameters
    assert "target_table" in sig.parameters
