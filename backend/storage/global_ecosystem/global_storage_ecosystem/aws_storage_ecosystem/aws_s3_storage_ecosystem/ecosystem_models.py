"""Typed metadata for the Amazon S3 storage category."""
from dataclasses import dataclass

@dataclass(frozen=True)
class StorageCategoryRecord:
    category: str = "S3"
    provider: str = "AWS"
    connection_state: str = "NOT_CONFIGURED"
    storage_operations_enabled: bool = False
