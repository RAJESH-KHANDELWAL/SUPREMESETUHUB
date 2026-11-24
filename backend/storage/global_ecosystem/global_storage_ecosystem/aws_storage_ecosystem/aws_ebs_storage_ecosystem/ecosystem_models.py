"""Typed metadata for the Amazon EBS storage category."""
from dataclasses import dataclass

@dataclass(frozen=True)
class StorageCategoryRecord:
    category: str = "EBS"
    provider: str = "AWS"
    connection_state: str = "NOT_CONFIGURED"
    storage_operations_enabled: bool = False
