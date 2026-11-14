"""Runtime provider selection for GLOBAL STORAGE ECOSYSTEM.

This is the orchestration boundary over the existing physical storage adapters.
It deliberately does not duplicate asset metadata, ACLs, or audit ownership:
those remain in backend.engine.storage.StorageEngine.
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import BinaryIO
from uuid import uuid4

from backend.storage.filesystem import LocalFileStorage
from backend.storage.s3 import S3ObjectStorage


class StorageProviderRuntime:
    """Select and operate an explicitly configured physical storage backend."""

    BACKENDS = {
        "local": ("LOCAL_FILESYSTEM", "Local / persistent filesystem"),
        "aws_s3": ("AWS_S3", "Amazon S3"),
    }
    BACKEND_ALIASES = {
        "LOCAL_FILESYSTEM": "local",
        "LOCAL": "local",
        "AWS_S3": "aws_s3",
        "S3": "aws_s3",
    }

    def __init__(self, provider_id: str | None = None, *, s3_client=None):
        selected = (provider_id or os.getenv("SUPREME_STORAGE_PROVIDER", "local")).strip().lower()
        selected = self.BACKEND_ALIASES.get(selected.upper(), selected)
        if selected not in self.BACKENDS:
            raise ValueError("UNSUPPORTED_STORAGE_PROVIDER")
        self.provider_id = selected
        self.backend_name, self.display_name = self.BACKENDS[selected]
        if selected == "local":
            self.backend = LocalFileStorage()
        else:
            self.backend = S3ObjectStorage(client=s3_client)

    @classmethod
    def available_providers(cls) -> list[dict]:
        return [
            {"provider_id": key, "backend": value[0], "name": value[1],
             "implementation_state": "IMPLEMENTED"}
            for key, value in cls.BACKENDS.items()
        ]

    def status(self) -> dict:
        health = self.backend.health()
        writable = bool(health.get("writable"))
        return {
            "provider_id": self.provider_id,
            "provider": self.display_name,
            "backend": self.backend_name,
            "status": health.get("status", "UNKNOWN"),
            "configured": bool(health.get("configured")),
            "connected": bool(health.get("connected", writable)),
            "read_verified": False,  # no independent read-back probe is performed by health()
            "write_verified": writable,
            "durability_verified": bool(health.get("durability_verified", False)),
            "health": health,
        }

    @staticmethod
    def _safe_segment(value: str, fallback: str) -> str:
        result = re.sub(r"[^A-Za-z0-9._-]", "_", str(value or "").strip())
        result = result.strip("._-")
        return result[:80] or fallback

    def store_stream(
        self, stream: BinaryIO, *, owner_id: str, area_id: str,
        filename: str, max_bytes: int,
    ) -> dict:
        status = self.status()
        if not status["write_verified"]:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        suffix = Path(str(filename or "")).suffix.lower()
        if not re.fullmatch(r"\.[a-z0-9]{1,10}", suffix):
            suffix = ""
        key = "/".join((
            "users", self._safe_segment(owner_id, "unknown"),
            self._safe_segment(area_id, "personal"), uuid4().hex + suffix,
        ))
        size, checksum = self.backend.save_stream_at_key(stream, key, max_bytes=max_bytes)
        if size <= 0:
            self.backend.delete_key(key)
            raise ValueError("EMPTY_FILE_NOT_ALLOWED")
        return {
            "storage_key": key, "size_bytes": size, "checksum": checksum,
            "storage_backend": self.backend_name, "storage_provider": self.provider_id,
        }

    def open_key(self, storage_key: str):
        return self.backend.open_key(storage_key)

    def exists_key(self, storage_key: str) -> bool:
        return self.backend.exists_key(storage_key)

    def delete_key(self, storage_key: str) -> bool:
        return self.backend.delete_key(storage_key)


__all__ = ["StorageProviderRuntime"]
