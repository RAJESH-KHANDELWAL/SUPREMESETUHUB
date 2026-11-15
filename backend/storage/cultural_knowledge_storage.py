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
        if max_bytes < 1:
            raise ValueError("MAX_BYTES_MUST_BE_POSITIVE")
        safe_name = str(filename or "source.bin").replace("\\\\", "/").split("/")[-1]
        content = stream.read(max_bytes + 1)
        if not content:
            raise ValueError("EMPTY_SOURCE_FILE")
        if len(content) > max_bytes:
            raise ValueError("CULTURAL_SOURCE_MAX_SIZE_EXCEEDED")
        key = self.storage.save_bytes(content, safe_name)
        return {"storage_key": key, "filename": safe_name, "area_id": self.AREA,
                "size_bytes": len(content), "storage_backend": "LOCAL_FILESYSTEM"}

    def open_source(self, storage_key: str):
        return self.storage.open_key(storage_key)

    def delete_source(self, storage_key: str) -> bool:
        return self.storage.delete_key(storage_key)
