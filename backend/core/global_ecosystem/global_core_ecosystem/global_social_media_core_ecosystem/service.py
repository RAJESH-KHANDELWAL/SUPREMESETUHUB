"""Public Global Social Media Core service."""
from typing import Any
from .orchestrator import SocialMediaCoreOrchestrator
class SocialMediaCoreService:
    def __init__(self)->None:self._orchestrator=SocialMediaCoreOrchestrator()
    def status(self)->dict[str,Any]:return self._orchestrator.health()
    def catalog(self)->dict[str,Any]:return self._orchestrator.catalog()
    def list_platforms(self,**filters:Any)->dict[str,Any]:return self._orchestrator.list_platforms(**filters)
    def get_platform(self,platform_id:str)->dict[str,Any]|None:return self._orchestrator.get_platform(platform_id)
    def list_domains(self)->dict[str,Any]:return self._orchestrator.domains()
    def dependency_map(self)->dict[str,Any]:return self._orchestrator.dependency_map()
