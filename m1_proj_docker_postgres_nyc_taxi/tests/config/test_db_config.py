import os
from app.config.db_config import get_pg_config


def test_db_config_uses_env_vars(monkeypatch):
    monkeypatch.setenv("PGHOST", "test-host")
    monkeypatch.setenv("PGPORT", "6543")

    cfg = get_pg_config()

    assert cfg["host"] == "test-host"
    assert cfg["port"] == 6543


def test_db_config_fallback_to_defaults(monkeypatch):
    monkeypatch.delenv("PGHOST", raising=False)
    monkeypatch.delenv("PGPORT", raising=False)

    cfg = get_pg_config()

    assert cfg["host"] == "pgdatabase"
    assert cfg["port"] == 5432
