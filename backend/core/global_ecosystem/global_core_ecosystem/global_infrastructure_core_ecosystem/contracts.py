"""Provider-neutral infrastructure contracts; no transport or provider SDKs."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Mapping
@dataclass(frozen=True)
class InfrastructureResourceContract:
    resource_id:str
    resource_type:str
    category:str
    provider_id:str|None=None
    region:str|None=None
    environment:str|None=None
    metadata:Mapping[str,Any]=field(default_factory=dict)
    def validate(self)->list[str]:
        errors=[]
        for key in ("resource_id","resource_type","category"):
            value=getattr(self,key)
            if not isinstance(value,str) or not value.strip(): errors.append(f"{key} must be a non-empty string")
        if not isinstance(self.metadata,Mapping): errors.append("metadata must be a mapping")
        return errors
@dataclass(frozen=True)
class InfrastructureProviderDescriptor:
    provider_id:str
    display_name:str
    status:str="CATALOG_ONLY"
    live_connection_verified:bool=False
