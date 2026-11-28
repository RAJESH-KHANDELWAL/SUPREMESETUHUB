"""Typed Hosting Core provider metadata contract."""
from dataclasses import dataclass,field
from typing import Any
@dataclass(frozen=True)
class HostingProviderRecord:
 ecosystem_id:str;provider_id:str;provider_name:str;hosting_category:str="UNCLASSIFIED";entity_type:str="SERVICE_PROVIDER";capabilities:tuple[str,...]=();status:str="CORE_CATALOG_ONLY";enabled:bool=True;live_connection_verified:bool=False;metadata:dict[str,Any]=field(default_factory=dict)
