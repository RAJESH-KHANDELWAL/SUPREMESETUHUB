"""DATABASE-owned GLOBAL APP persistence contracts.

This module defines record shape only. It does not claim that a database,
connection, migration, or durable repository has been configured.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Any
@dataclass(frozen=True)
class AppProviderRecord:
 provider_id:str
 name:str
 category:str
 origin:str
 ecosystem_kind:str
 integration_status:str="catalog_only"
 metadata:dict[str,Any]|None=None
 created_at:datetime|None=None
 updated_at:datetime|None=None
 def __post_init__(self):
  for field in ("provider_id","name","category","origin","ecosystem_kind"):
   if not str(getattr(self,field) or "").strip(): raise ValueError(f"{field} is required")
  if self.integration_status not in {"catalog_only","scaffold","integration_in_progress","configured","live_verified"}:
   raise ValueError("invalid integration_status")
