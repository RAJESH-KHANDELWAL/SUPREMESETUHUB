"""Typed hosting provider metadata contract."""
from dataclasses import dataclass,field
from typing import Any
@dataclass(frozen=True)
class HostingProviderRecord:
 ecosystem_id:str
 provider_id:str
 provider_name:str
 hosting_types:tuple[str,...]=()
 regions:tuple[str,...]=()
 status:str="CORE_CATALOG_ONLY"
 live_connection_verified:bool=False
 metadata:dict[str,Any]=field(default_factory=dict)
