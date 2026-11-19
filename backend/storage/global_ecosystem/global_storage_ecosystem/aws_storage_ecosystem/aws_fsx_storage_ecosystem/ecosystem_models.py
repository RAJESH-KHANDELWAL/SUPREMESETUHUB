"""Typed metadata for the Amazon FSx storage category."""
from dataclasses import dataclass

@dataclass(frozen=True)
class StorageCategoryRecord:
    category: str = "FSX"
    provider: str = "AWS"
    connection_state: str = "NOT_CONFIGURED"
    storage_operations_enabled: bool = False
