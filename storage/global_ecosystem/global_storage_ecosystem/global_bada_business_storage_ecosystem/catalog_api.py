"""Read-only GLOBAL BADA BUSINESS catalog API."""
from .ecosystem_taxonomy import list_ecosystems,find_ecosystem
from .ecosystem_service import EcosystemService
class GlobalBadaBusinessCatalog:
 def health(self)->dict:return EcosystemService().health()
 def list(self)->list[dict]:return list_ecosystems()
 def get(self,value:str)->dict|None:return find_ecosystem(value)
