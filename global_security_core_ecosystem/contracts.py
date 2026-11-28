"""Typed contracts for security CORE metadata and tenant context."""
from __future__ import annotations
from dataclasses import asdict,dataclass,field
from datetime import datetime,timezone
from typing import Any
def utc_now(): return datetime.now(timezone.utc).isoformat()
@dataclass(frozen=True)
class TenantContext:
    tenant_id:str
    actor_id:str
    roles:tuple[str,...]=()
    request_id:str|None=None
    def validate(self):
        if not self.tenant_id.strip(): raise ValueError("TENANT_ID_REQUIRED")
        if not self.actor_id.strip(): raise ValueError("ACTOR_ID_REQUIRED")
@dataclass(frozen=True)
class SecretReference:
    provider:str
    reference:str
    version:str|None=None
    def __post_init__(self):
        if not self.provider.strip() or not self.reference.strip(): raise ValueError("SECRET_REFERENCE_REQUIRED")
@dataclass
class CoreResult:
    success:bool
    ecosystem_id:str
    status:str
    data:dict[str,Any]=field(default_factory=dict)
    errors:list[str]=field(default_factory=list)
    request_id:str|None=None
    timestamp:str=field(default_factory=utc_now)
    def to_dict(self): return asdict(self)
