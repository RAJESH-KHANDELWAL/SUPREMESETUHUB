"""Manager facade for Cultural Service / Work / Business CORE."""
from __future__ import annotations
from typing import Any
from .service import CulturalServiceWorkBusinessCore
class CulturalServiceWorkBusinessCoreManager:
 def __init__(self,core:CulturalServiceWorkBusinessCore|None=None)->None: self.core=core or CulturalServiceWorkBusinessCore()
 def status(self)->dict[str,Any]: return self.core.status()
 def catalogue(self,domain:str|None=None)->list[dict[str,Any]]: return self.core.catalogue(domain)
 def capability(self,capability_id:str)->dict[str,Any]|None: return self.core.capability(capability_id)
 def validate(self,record:Any)->list[str]: return self.core.validate(record)
 def can_publish(self,record:Any)->bool: return self.core.can_publish(record)
