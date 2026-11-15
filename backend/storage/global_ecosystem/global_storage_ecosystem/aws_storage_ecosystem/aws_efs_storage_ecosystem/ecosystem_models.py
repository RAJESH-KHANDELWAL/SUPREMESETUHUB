"""Typed metadata for the Amazon EFS storage category."""
from dataclasses import dataclass

@dataclass(frozen=True)
class StorageCategoryRecord:
    category: str = "EFS"
    provider: str = "AWS"
    connection_state: str = "NOT_CONFIGURED"
    storage_operations_enabled: bool = False
