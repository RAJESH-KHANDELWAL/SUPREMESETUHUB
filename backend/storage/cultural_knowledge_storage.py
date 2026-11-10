"""Storage boundary for cultural source files; metadata stays in DATABASE."""
from __future__ import annotations
from typing import BinaryIO
from backend.storage.filesystem import LocalFileStorage

class CulturalKnowledgeStorage:
    AREA = "cultural-knowledge"

    def __init__(self, storage: LocalFileStorage | None = None) -> None:
        self.storage = storage or LocalFileStorage()

    def status(self) -> dict:
        return {"area": self.AREA, **self.storage.health()}

    def save_source(self, stream: BinaryIO, filename: str, max_bytes: int = 25 * 1024 * 1024) -> dict:
        safe_name = str(filename or "source.bin").split("/")[-1].split("\\\\")[-1]
        key = self.storage.save_bytes(stream.read(max_bytes + 1), safe_name)
        return {"storage_key": key, "filename": safe_name, "area_id": self.AREA,
                "max_bytes": max_bytes}

    def open_source(self, storage_key: str):
        return self.storage.open_key(storage_key)

    def delete_source(self, storage_key: str) -> bool:
        return self.storage.delete(storage_key)
