"""STORAGE metadata model for server backup and artifact references."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class ServerArtifact:
    artifact_id: str
    server_id: str
    artifact_type: str
    storage_provider_id: str
    object_key: str
    content_type: str | None = None
    size_bytes: int | None = None
    checksum: str | None = None
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self):
        for name in ("artifact_id","server_id","artifact_type","storage_provider_id","object_key"):
            if not str(getattr(self, name)).strip():
                raise ValueError(f"{name} is required")
        if self.size_bytes is not None and self.size_bytes < 0:
            raise ValueError("size_bytes cannot be negative")
