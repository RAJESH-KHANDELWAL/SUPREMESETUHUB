"""Validated immutable Core metadata contracts."""
from dataclasses import asdict, dataclass, field
from typing import Any
@dataclass(frozen=True)
class ProviderDescriptor:
    provider_id:str
    display_name:str
    category:str="GENERAL"
    status:str="CATALOG_ONLY"
    live_connection_verified:bool=False
    def __post_init__(self):
        if not self.provider_id.strip() or not self.display_name.strip(): raise ValueError("PROVIDER_ID_AND_NAME_REQUIRED")
    def to_dict(self)->dict[str,Any]: return asdict(self)
@dataclass(frozen=True)
class IntegrationDescriptor:
    integration_id:str
    display_name:str
    domain_id:str
    folder:str
    category:str
    capabilities:tuple[str,...]=field(default_factory=tuple)
    sensitivity:str="STANDARD"
    age_restricted:bool=False
    consent_required:bool=False
    status:str="CORE_CATALOG_ONLY"
    live_connection_verified:bool=False
    def __post_init__(self):
        for key in ("integration_id","display_name","domain_id","folder","category"):
            if not getattr(self,key).strip(): raise ValueError(f"{key.upper()}_REQUIRED")
        if self.age_restricted and not self.consent_required: raise ValueError("AGE_RESTRICTED_DOMAIN_REQUIRES_CONSENT")
        if len(self.capabilities)!=len(set(self.capabilities)): raise ValueError("DUPLICATE_CAPABILITY")
    def to_dict(self)->dict[str,Any]: return asdict(self)
