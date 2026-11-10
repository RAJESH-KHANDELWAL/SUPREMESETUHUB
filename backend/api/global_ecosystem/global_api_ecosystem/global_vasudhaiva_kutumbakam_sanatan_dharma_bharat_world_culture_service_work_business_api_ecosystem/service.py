"""Application service composing CORE, ENGINE, AI and infrastructure adapters."""
from __future__ import annotations
from typing import Any
from backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_core_ecosystem.service import GlobalCultureServiceWorkBusinessCore
from backend.engine.global_ecosystem.global_engine_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_engine_ecosystem.manager import GlobalCultureServiceWorkBusinessEngine
from backend.ai.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_ai_ecosystem.assistant import GlobalCultureServiceWorkBusinessAI
from backend.database.global_ecosystem.global_database_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_database_ecosystem.repository import GlobalCultureServiceWorkBusinessRepository
from backend.storage.global_ecosystem.global_storage_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_storage_ecosystem.manager import GlobalCultureServiceWorkBusinessStorage
from backend.cloud.global_ecosystem.global_cloud_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_cloud_ecosystem.bridge import GlobalCultureServiceWorkBusinessCloud

class GlobalCultureServiceWorkBusinessAPIService:
    def __init__(self)->None:
        self.core=GlobalCultureServiceWorkBusinessCore()
        self.engine=GlobalCultureServiceWorkBusinessEngine(self.core)
        self.ai=GlobalCultureServiceWorkBusinessAI(self.engine)
        self.repository=GlobalCultureServiceWorkBusinessRepository()
        self.storage=GlobalCultureServiceWorkBusinessStorage()
        self.cloud=GlobalCultureServiceWorkBusinessCloud()
    def status(self)->dict[str,Any]:
        return {"ecosystem_id":self.core.ecosystem_id,"status":"FOUNDATION_READY",
                "layers":{"api":"READY","core":self.core.status(),"engine":self.engine.status(),
                "ai":self.ai.status(),"database":self.repository.health(),
                "storage":self.storage.status(),"cloud":self.cloud.status()},
                "scope":{"domains":["SERVICE","WORK","BUSINESS"],"taxonomy_only":True,
                "live_providers":False,"live_jobs_or_gigs":False}}
    def catalogue(self,domain:str|None=None)->list[dict[str,Any]]:
        if domain and domain.upper() not in {"SERVICE","WORK","BUSINESS"}:raise ValueError("INVALID_DOMAIN")
        return self.engine.catalogue(domain)
    def search(self,query:str,domain:str|None=None)->dict[str,Any]:
        if domain and domain.upper() not in {"SERVICE","WORK","BUSINESS"}:raise ValueError("INVALID_DOMAIN")
        return self.engine.search(query,domain)
    def ai_context(self,question:str,domain:str|None=None)->dict[str,Any]:
        if domain and domain.upper() not in {"SERVICE","WORK","BUSINESS"}:raise ValueError("INVALID_DOMAIN")
        return self.ai.build_context(question,domain)
    def save_record(self,record:dict[str,Any])->None:self.repository.save(record)
    def get_record(self,record_id:str)->dict[str,Any]|None:return self.repository.get(record_id)
    def search_records(self,query:str="",capability_id:str|None=None,limit:int=50)->list[dict[str,Any]]:
        return self.repository.search(query,capability_id,limit)
