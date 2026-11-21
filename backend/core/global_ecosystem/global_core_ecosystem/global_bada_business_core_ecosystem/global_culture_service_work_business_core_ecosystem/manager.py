"""Manager entry point for cultural service/work/business CORE."""
from __future__ import annotations
from typing import Any
from .service import GlobalBadaBusinessCultureServiceWorkBusinessCore
class GlobalBadaBusinessCultureServiceWorkBusinessManager:
    def __init__(self,core:GlobalBadaBusinessCultureServiceWorkBusinessCore|None=None)->None: self.core=core or GlobalBadaBusinessCultureServiceWorkBusinessCore()
    def status(self)->dict[str,Any]: return self.core.status()
    def catalogue(self,domain:str|None=None)->list[dict[str,Any]]: return self.core.catalogue(domain)
    def capability(self,capability_id:str)->dict[str,Any]|None: return self.core.capability(capability_id)
    def validate(self,record:dict[str,Any])->list[str]: return self.core.validate(record)
    def can_publish(self,record:dict[str,Any])->bool: return self.core.can_publish(record)
