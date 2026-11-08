"""DATABASE model for persisted SERVER inventory records."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class ServerInventoryRecord:
    server_id: str
    server_name: str
    provider_id: str
    server_type: str
    server_role: str
    country: str
    region: str
    environment: str
    status: str = "REGISTERED"
    authorized: bool = False
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self):
        for name in ("server_id","server_name","provider_id","server_type","server_role","country","region","environment"):
            value = getattr(self, name)
            if not str(value).strip():
                raise ValueError(f"{name} is required")
