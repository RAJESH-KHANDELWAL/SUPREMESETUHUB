"""Stable typed contracts for programming-language CORE metadata."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

class Readiness(str, Enum):
    CATALOG_ONLY = "CORE_CATALOG_ONLY"
    CONFIGURATION_REQUIRED = "READY_FOR_CONFIGURATION"
    ADAPTER_SCAFFOLD = "ADAPTER_SCAFFOLD_NOT_LIVE_VERIFIED"
    READY = "READY"
    DISABLED = "DISABLED"
    ERROR = "ERROR"

@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    actor_id: str
    actor_type: str = "user"
    roles: tuple[str, ...] = ()
    request_id: str | None = None
    def validate(self) -> None:
        if not isinstance(self.tenant_id, str) or not self.tenant_id.strip():
            raise ValueError("TENANT_ID_REQUIRED")
        if not isinstance(self.actor_id, str) or not self.actor_id.strip():
            raise ValueError("ACTOR_ID_REQUIRED")

@dataclass(frozen=True)
class SecretReference:
    provider: str
    reference: str
    version: str | None = None
    def __post_init__(self) -> None:
        if not self.provider.strip() or not self.reference.strip():
            raise ValueError("SECRET_REFERENCE_REQUIRED")

@dataclass(frozen=True)
class ProgrammingLanguageRecord:
    language_id: str
    canonical_name: str
    language_type: str
    aliases: tuple[str, ...] = ()
    paradigms: tuple[str, ...] = ()
    versions: tuple[str, ...] = ()
    specification: str | None = None
    runtime_or_compiler: str | None = None
    platforms: tuple[str, ...] = ()
    license: str | None = None
    support_status: str = "METADATA_ONLY"
    security_lifecycle: str = "NOT_ASSESSED"
    def __post_init__(self) -> None:
        if not all(isinstance(v, str) and v.strip() for v in (self.language_id, self.canonical_name, self.language_type)):
            raise ValueError("PROGRAMMING_LANGUAGE_ID_NAME_AND_TYPE_REQUIRED")

@dataclass
class CoreResult:
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    request_id: str | None = None
    timestamp: str = field(default_factory=utc_now)
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
