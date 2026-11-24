"""Catalog-only global database category module; not a live connector."""

TIME_SERIES_DATABASES = {
    "category": "TIME_SERIES_DATABASES",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "providers": [
        "InfluxDB",
        "TimescaleDB",
        "QuestDB",
        "VictoriaMetrics",
        "Prometheus",
        "OpenTSDB",
        "Apache IoTDB",
        "TDengine",
        "Apache Druid",
        "Apache Pinot",
        "ClickHouse",
        "GreptimeDB",
        "M3DB",
        "Graphite",
        "CrateDB"
    ],
}
