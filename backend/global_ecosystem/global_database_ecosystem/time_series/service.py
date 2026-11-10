"""Time-series and telemetry database descriptors."""
from typing import Any
PLATFORMS = ("timescaledb", "influxdb", "questdb", "tdengine", "victoriametrics")
def describe_time_series_domain() -> dict[str, Any]:
    return {"domain":"time_series","platforms":list(PLATFORMS),"capabilities":["timestamped_ingestion","retention_policies","downsampling","time_partitioning","telemetry_queries"],"integration_status":"catalog_only"}
