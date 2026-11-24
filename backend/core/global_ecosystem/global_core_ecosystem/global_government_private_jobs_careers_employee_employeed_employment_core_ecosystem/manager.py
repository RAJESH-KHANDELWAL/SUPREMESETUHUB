"""Stable entry point for the global employment Core taxonomy."""
from .service import EmploymentCoreService
class GlobalEmploymentCoreManager:
    NAME="GLOBAL GOVERNMENT & PRIVATE JOBS, CAREERS, EMPLOYEE AND EMPLOYMENT CORE ECOSYSTEM"
    ECOSYSTEM_ID="GLOBAL-GOVERNMENT-PRIVATE-JOBS-CAREERS-EMPLOYEE-EMPLOYMENT-CORE-ECOSYSTEM"
    def __init__(self): self.service=EmploymentCoreService()
    def status(self): return self.service.status()
    def health(self): return {"success":True,"health":"HEALTHY","readiness":"CORE_CATALOG_READY","live_data_verified":False}
    def catalog(self): return self.service.catalog()
    def list_domains(self): return self.catalog()["domains"]
    def search(self,query="",domain_id=None): return self.service.search(query,domain_id)
    def validate_record(self,payload): return self.service.validate_record(payload)
def get_manager(): return GlobalEmploymentCoreManager()
__all__=["GlobalEmploymentCoreManager","get_manager"]
