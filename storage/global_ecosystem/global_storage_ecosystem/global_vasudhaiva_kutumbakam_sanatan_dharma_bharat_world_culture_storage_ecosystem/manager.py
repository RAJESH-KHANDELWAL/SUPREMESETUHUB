"""Safe local storage adapter for cultural source assets."""
from __future__ import annotations
from typing import BinaryIO, Any
from backend.storage.cultural_knowledge_storage import CulturalKnowledgeStorage

class GlobalCulturalStorage:
    def __init__(self, adapter: CulturalKnowledgeStorage | None = None) -> None:
        self.adapter = adapter or CulturalKnowledgeStorage()

    def status(self) -> dict[str, Any]:
        return {"ecosystem": "GLOBAL_CULTURAL_STORAGE", **self.adapter.status()}

    def store_source(self, stream: BinaryIO, filename: str, max_bytes: int = 25 * 1024 * 1024) -> dict[str, Any]:
        return self.adapter.save_source(stream, filename, max_bytes=max_bytes)

    def open_source(self, storage_key: str):
        return self.adapter.open_source(storage_key)

    def delete_source(self, storage_key: str) -> bool:
        return self.adapter.delete_source(storage_key)
