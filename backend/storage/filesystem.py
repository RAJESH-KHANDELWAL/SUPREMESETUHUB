"""Private local-filesystem storage backend for uploaded assets.

Set SUPREME_FILE_STORAGE_DIR to a persistent directory on the backend host.
Files are stored under generated opaque keys, never under user-supplied paths.
"""
from __future__ import annotations

import os
import re
import tempfile
from pathlib import Path
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
                "configured": False,
                "status": "NOT_CONFIGURED",
                "backend": None,
                "writable": False,
            }
        try:
            self.root.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(prefix=".supreme-health-", dir=self.root, delete=True):
                pass
            return {
                "configured": True,
                "status": "READY",
                "backend": "LOCAL_FILESYSTEM",
                "writable": True,
            }
        except OSError:
            return {
                "configured": True,
                "status": "UNAVAILABLE",
                "backend": "LOCAL_FILESYSTEM",
                "writable": False,
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

    def delete(self, storage_key: str) -> bool:
        target = self.resolve(storage_key)
        try:
            target.unlink(missing_ok=True)
            return True
        except OSError:
            return False
