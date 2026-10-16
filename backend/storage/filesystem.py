"""Private local-filesystem storage backend for uploaded assets.

Set SUPREME_FILE_STORAGE_DIR to a persistent directory on the backend host.
Files are stored under generated opaque keys, never under user-supplied paths.
"""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import tempfile
from pathlib import Path, PurePosixPath
from uuid import uuid4


class LocalFileStorage:
    """Safe local disk storage with explicit configuration and path validation."""

    def __init__(self, root_dir: str | None = None):
        configured = root_dir if root_dir is not None else os.getenv("SUPREME_FILE_STORAGE_DIR", "")
        configured = str(configured or "").strip()
        self.root = Path(configured).expanduser().resolve() if configured else None

    @property
    def configured(self) -> bool:
        return self.root is not None

    def health(self) -> dict:
        if self.root is None:
            return {
                "configured": False, "status": "NOT_CONFIGURED", "backend": None,
                "writable": False, "durability_verified": False, "durability_acknowledged": False,
            }
        hosted = bool(os.getenv("RENDER") or os.getenv("RENDER_SERVICE_ID"))
        acknowledged = (
            os.getenv("SUPREME_FILE_STORAGE_DURABILITY_ACKNOWLEDGED", "").strip().casefold() == "true"
            or os.getenv("GALLERY_WOULT_STORAGE_DURABILITY_ACKNOWLEDGED", "").strip().casefold() == "true"
        )
        if hosted and not acknowledged:
            return {
                "configured": True, "status": "PERSISTENCE_NOT_VERIFIED",
                "backend": "LOCAL_FILESYSTEM", "writable": False, "hosted_environment": True,
                "durability_verified": False, "durability_acknowledged": acknowledged,
            }
        try:
            self.root.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(prefix=".supreme-health-", dir=self.root, delete=True):
                pass
            return {
                "configured": True, "status": "READY", "backend": "LOCAL_FILESYSTEM",
                "writable": True, "hosted_environment": hosted, "durability_verified": False,
                "durability_acknowledged": acknowledged,
            }
        except OSError:
            return {
                "configured": True, "status": "UNAVAILABLE", "backend": "LOCAL_FILESYSTEM",
                "writable": False, "hosted_environment": hosted, "durability_verified": False,
                "durability_acknowledged": acknowledged,
            }

    @staticmethod
    def _safe_suffix(filename: str) -> str:
        suffix = Path(str(filename or "")).suffix.lower()
        if not suffix or not re.fullmatch(r"\.[a-z0-9]{1,10}", suffix):
            return ""
        return suffix

    def save_bytes(self, content: bytes, filename: str) -> str:
        health = self.health()
        if not health["writable"] or self.root is None:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        key = uuid4().hex + self._safe_suffix(filename)
        target = self.resolve(key)
        try:
            with target.open("xb") as handle:
                handle.write(content)
        except OSError as exc:
            raise RuntimeError("STORAGE_WRITE_FAILED") from exc
        return key

    def resolve(self, storage_key: str) -> Path:
        key = str(storage_key or "")
        if not re.fullmatch(r"[a-f0-9]{32}(?:\.[a-z0-9]{1,10})?", key):
            raise ValueError("INVALID_STORAGE_KEY")
        if self.root is None:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED")
        target = (self.root / key).resolve()
        if target.parent != self.root:
            raise ValueError("INVALID_STORAGE_KEY")
        return target

    def resolve_key(self, storage_key: str) -> Path:
        """Resolve a platform-owned relative key without allowing path traversal."""
        key = str(storage_key or "").replace("\\", "/")
        relative = PurePosixPath(key)
        if not key or relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
            raise ValueError("INVALID_STORAGE_KEY")
        if self.root is None:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED")
        target = self.root.joinpath(*relative.parts).resolve()
        if target == self.root or self.root not in target.parents:
            raise ValueError("INVALID_STORAGE_KEY")
        return target

    def save_stream_at_key(self, stream, storage_key: str, max_bytes: int | None = None) -> tuple[int, str]:
        """Persist a stream at a generated/platform-owned key using atomic replace."""
        health = self.health()
        if not health["writable"] or self.root is None:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        target = self.resolve_key(storage_key)
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name(f".{target.name}.{uuid4().hex}.tmp")
        digest = hashlib.sha256()
        size = 0
        try:
            with temporary.open("xb") as output:
                while True:
                    chunk = stream.read(1024 * 1024)
                    if not chunk:
                        break
                    size += len(chunk)
                    if max_bytes is not None and size > max_bytes:
                        raise ValueError("MAX_UPLOAD_SIZE_EXCEEDED")
                    output.write(chunk)
                    digest.update(chunk)
            os.replace(temporary, target)
        except Exception:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass
            raise
        return size, digest.hexdigest()

    def open_key(self, storage_key: str):
        target = self.resolve_key(storage_key)
        if not target.is_file():
            raise FileNotFoundError(storage_key)
        return target.open("rb")

    def exists_key(self, storage_key: str) -> bool:
        return self.resolve_key(storage_key).is_file()

    def copy_key(self, source_storage_key: str, target_storage_key: str) -> tuple[int, str]:
        health = self.health()
        if not health["writable"]:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        source = self.resolve_key(source_storage_key)
        if not source.is_file():
            raise FileNotFoundError(source_storage_key)
        with source.open("rb") as stream:
            return self.save_stream_at_key(stream, target_storage_key)

    def delete_key(self, storage_key: str) -> bool:
        health = self.health()
        if not health["writable"]:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        target = self.resolve_key(storage_key)
        if not target.is_file():
            return False
        target.unlink()
        return True

    def delete(self, storage_key: str) -> bool:
        target = self.resolve(storage_key)
        try:
            target.unlink(missing_ok=True)
            return True
        except OSError:
            return False
