"""Typed metadata for the AWS Elastic Disaster Recovery storage category."""
from dataclasses import dataclass

@dataclass(frozen=True)
class StorageCategoryRecord:
    category: str = "ELASTIC_DISASTER_RECOVERY"
    provider: str = "AWS"
    connection_state: str = "NOT_CONFIGURED"
    storage_operations_enabled: bool = False
