"""Streaming ingestion and CDC metadata descriptors."""
from typing import Any
PLATFORMS = ("apache_kafka", "redpanda", "apache_pulsar", "debezium", "cloud_pubsub", "kinesis")
def describe_streaming_domain() -> dict[str, Any]:
    return {"domain":"streaming_and_cdc","platforms":list(PLATFORMS),"capabilities":["event_streams","change_data_capture","schema_registry","replay","dead_letter_queues"],"integration_status":"catalog_only"}
