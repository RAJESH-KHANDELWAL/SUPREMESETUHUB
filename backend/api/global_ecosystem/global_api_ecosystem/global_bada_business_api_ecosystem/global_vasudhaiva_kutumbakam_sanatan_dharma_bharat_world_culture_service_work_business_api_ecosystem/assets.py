"""Asset operations delegated to the independent STORAGE layer."""
from __future__ import annotations

from typing import Any


class CultureServiceWorkBusinessAssets:
    def __init__(self, storage: Any) -> None:
        self.storage = storage

    def status(self) -> dict[str, Any]:
        return self.storage.status()

    def store(self, stream: Any, filename: str, max_bytes: int = 25 * 1024 * 1024) -> dict[str, Any]:
        return self.storage.store_asset(stream, filename, max_bytes)

    def open(self, storage_key: str) -> Any:
        return self.storage.open_asset(storage_key)

    def delete(self, storage_key: str) -> bool:
        return self.storage.delete_asset(storage_key)
}
