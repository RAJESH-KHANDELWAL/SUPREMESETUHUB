"""Stable manager for employment service-work business taxonomy."""
from .service import EmploymentServicesBusinessService
class GlobalEmploymentServicesBusinessManager:
 NAME="GLOBAL GOVERNMENT PRIVATE JOBS CAREERS EMPLOYMENT SERVICE-WORK BUSINESS CORE ECOSYSTEM"
 ECOSYSTEM_ID="GLOBAL-GOVERNMENT-PRIVATE-JOBS-CAREERS-EMPLOYMENT-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
 def __init__(self): self.service=EmploymentServicesBusinessService()
 def status(self): return self.service.status()
 def health(self): return {"success":True,"health":"HEALTHY","readiness":"CORE_CATALOG_READY","live_services_verified":False}
 def catalog(self): return self.service.catalog()
 def list_domains(self): return self.catalog()["domains"]
 def search(self,query="",domain_id=None): return self.service.search(query,domain_id)
 def validate_provider(self,payload): return self.service.validate_provider(payload)
def get_manager(): return GlobalEmploymentServicesBusinessManager()
__all__=["GlobalEmploymentServicesBusinessManager","get_manager"]
