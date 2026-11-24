"""Read-only catalog API; no external app/store provider calls."""
from __future__ import annotations
from typing import Any
from .ecosystem_taxonomy import list_ecosystems,find_ecosystem
from .ecosystem_service import EcosystemService
class GlobalAppStorageCatalog:
 def __init__(self):self._service=EcosystemService()
 def health(self)->dict[str,Any]:return self._service.health()
 def list(self,group:str|None=None)->list[dict[str,str]]:
  rows=list_ecosystems()
  return rows if group is None else [row for row in rows if group.strip().casefold() in row["group"].casefold()]
 def get(self,name_or_category:str)->dict[str,str]|None:return find_ecosystem(name_or_category)
