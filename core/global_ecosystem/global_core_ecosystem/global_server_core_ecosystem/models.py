"""Provider-neutral models owned by SERVER CORE."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class ServerIdentity:
    server_id: str
    provider_id: str
    server_type: str
    server_role: str
    country: str
    region: str
    environment: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        required = ("server_id","provider_id","server_type","server_role","country","region","environment")
        for name in required:
            if not str(getattr(self, name)).strip():
                raise ValueError(f"{name} is required")

@dataclass(frozen=True)
class ServerLifecycleState:
    status: str = "REGISTERED"
    enabled: bool = True
    authorized: bool = False
    health: str = "UNKNOWN"

@dataclass(frozen=True)
class ServerResourceDescriptor:
    identity: ServerIdentity
    lifecycle: ServerLifecycleState = field(default_factory=ServerLifecycleState)
