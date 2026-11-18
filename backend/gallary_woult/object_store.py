from __future__ import annotations

import os
import re
from io import BytesIO
from pathlib import Path
from typing import BinaryIO

from backend.storage.filesystem import LocalFileStorage
from backend.storage.provider_registry import get_storage_provider_status
from backend.storage.s3 import S3ObjectStorage


class UploadTooLargeError(ValueError):
    """Raised when an uploaded object exceeds the configured size limit."""


class GalleryWoultObjectStore:
    """GALLARY WOULT adapter to the shared STORAGE infrastructure.

    GALLARY WOULT owns file-management behavior and metadata; provider adapters
    own file bytes. Selecting a cloud provider never silently falls back to disk.
    """

    def __init__(self, root: str | None = None, max_upload_bytes: int | None = None):
        self.hosted_environment = bool(os.getenv("RENDER") or os.getenv("RENDER_SERVICE_ID"))
        configured_root = str(
            root or os.getenv("SUPREME_FILE_STORAGE_DIR", "")
            or os.getenv("GALLERY_WOULT_STORAGE_ROOT", "")
        ).strip()
        self.explicit_root = bool(configured_root)
        if not configured_root and not self.hosted_environment:
            configured_root = "data/shared_storage"
        self.durability_acknowledged = (
            os.getenv("SUPREME_FILE_STORAGE_DURABILITY_ACKNOWLEDGED", "").strip().casefold() == "true"
            or os.getenv("GALLERY_WOULT_STORAGE_DURABILITY_ACKNOWLEDGED", "").strip().casefold() == "true"
        )
        try:
            configured_limit = int(
                max_upload_bytes if max_upload_bytes is not None
                else os.getenv("GALLERY_WOULT_MAX_UPLOAD_BYTES", str(100 * 1024 * 1024))
            )
        except (TypeError, ValueError):
            configured_limit = 100 * 1024 * 1024
        self.max_upload_bytes = max(1, configured_limit)
        self.provider_status = get_storage_provider_status()
        self.storage = LocalFileStorage(root_dir=configured_root or None)
        self.s3_storage = S3ObjectStorage() if self.provider_status.get("selected_provider") == "aws_s3" else None
        self.root = self.storage.root

    @property
    def writes_allowed(self) -> bool:
        selected = self.provider_status.get("selected_provider")
        if selected == "aws_s3":
            return bool(self.s3_storage and self.s3_storage.health().get("writable"))
        if selected != "local":
            return False
        if not self.hosted_environment:
            return self.storage.root is not None
        return (
            self.explicit_root and self.durability_acknowledged
            and bool(self.storage.health()["writable"])
        )

    def status(self) -> dict:
        selected = self.provider_status.get("selected_provider")
        if selected == "aws_s3":
            backend_status = self.s3_storage.health() if self.s3_storage else {}
            return {
                **backend_status,
                "backend": "AWS_S3",
                "status": backend_status.get("status", "AWS_S3_CONNECTION_FAILED"),
                "writable": bool(backend_status.get("writable")),
                "max_upload_bytes": self.max_upload_bytes,
                "provider": self.provider_status,
                "durability_verified": False,
            }
        shared_status = self.storage.health()
        if selected != "local":
            state = "ADAPTER_NOT_IMPLEMENTED"
        elif self.hosted_environment and not self.writes_allowed:
            state = "PERSISTENCE_NOT_VERIFIED"
        elif not self.explicit_root:
            state = "LOCAL_DEVELOPMENT_DEFAULT" if not self.hosted_environment else "PERSISTENCE_NOT_VERIFIED"
        elif self.durability_acknowledged:
            state = "CONFIGURED_OPERATOR_ACKNOWLEDGED"
        else:
            state = "CONFIGURED_DURABILITY_UNVERIFIED"
        return {
            **shared_status,
            "backend": "SHARED_STORAGE_SERVICE",
            "status": state,
            "root_configured": self.explicit_root,
            "durability_acknowledged": self.durability_acknowledged,
            "durability_verified": False,
            "hosted_environment": self.hosted_environment,
            "max_upload_bytes": self.max_upload_bytes,
            "writable": self.writes_allowed,
            "provider": self.provider_status,
        }

    def _ensure_writes_allowed(self) -> None:
        if not self.writes_allowed:
            raise RuntimeError("PERSISTENT_STORAGE_NOT_CONFIGURED_OR_VERIFIED")

    @staticmethod
    def _safe_name(name: str) -> str:
        value = Path(name or "file").name
        value = re.sub(r"[^A-Za-z0-9._ -]", "_", value).strip()
        return value or "file"

    @staticmethod
    def _safe_component(value: str) -> str:
        value = re.sub(r"[^A-Za-z0-9._-]", "_", str(value))
        return value.strip("._") or "unknown"

    def _path_for(self, storage_key: str) -> Path:
        return self.storage.resolve_key(storage_key)

    def make_storage_key(self, owner_id: str, object_id: str, filename: str) -> str:
        return (
            f"gallary_woult/{self._safe_component(owner_id)}/"
            f"{self._safe_component(object_id)}/{self._safe_name(filename)}"
        )

    def save_stream(self, stream: BinaryIO, storage_key: str) -> tuple[int, str]:
        self._ensure_writes_allowed()
        backend = self.s3_storage if self.provider_status.get("selected_provider") == "aws_s3" else self.storage
        try:
            return backend.save_stream_at_key(stream, storage_key, max_bytes=self.max_upload_bytes)
        except ValueError as exc:
            if str(exc) == "MAX_UPLOAD_SIZE_EXCEEDED":
                raise UploadTooLargeError(str(exc)) from exc
            raise

    def save_bytes(self, data: bytes, storage_key: str) -> tuple[int, str]:
        return self.save_stream(BytesIO(data), storage_key)

    def open(self, storage_key: str) -> BinaryIO:
        if self.provider_status.get("selected_provider") == "aws_s3":
            if not self.s3_storage:
                raise RuntimeError("PERSISTENT_STORAGE_NOT_CONFIGURED_OR_VERIFIED")
            return self.s3_storage.open_key(storage_key)
        return self.storage.open_key(storage_key)

    def exists(self, storage_key: str) -> bool:
        if self.provider_status.get("selected_provider") == "aws_s3":
            return bool(self.s3_storage and self.s3_storage.exists_key(storage_key))
        return self.storage.exists_key(storage_key)

    def copy(self, source_storage_key: str, target_storage_key: str) -> tuple[int, str]:
        self._ensure_writes_allowed()
        backend = self.s3_storage if self.provider_status.get("selected_provider") == "aws_s3" else self.storage
        try:
            return backend.copy_key(source_storage_key, target_storage_key)
        except ValueError as exc:
            if str(exc) == "MAX_UPLOAD_SIZE_EXCEEDED":
                raise UploadTooLargeError(str(exc)) from exc
            raise

    def delete(self, storage_key: str) -> bool:
        self._ensure_writes_allowed()
        if self.provider_status.get("selected_provider") == "aws_s3":
            return bool(self.s3_storage and self.s3_storage.delete_key(storage_key))
        return self.storage.delete_key(storage_key)
