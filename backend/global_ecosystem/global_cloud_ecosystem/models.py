"""Typed cloud provider metadata model."""
from dataclasses import dataclass
from typing import Literal
IntegrationStatus=Literal["catalog_only","scaffold","integration_in_progress","configured","live_verified"]
@dataclass(frozen=True,slots=True)
class CloudProviderRecord:
    id:str
    name:str
    origin:str
    capabilities:tuple[str,...]
    integration_status:IntegrationStatus="catalog_only"
    live_connection_verified:bool=False
__all__=["CloudProviderRecord","IntegrationStatus"]
