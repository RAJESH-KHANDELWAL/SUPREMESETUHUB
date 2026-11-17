"""Read-only facade for the Global Storage CORE Ecosystem."""
from .catalog import get_provider,list_providers
from .domain_catalog import list_domains
from .orchestrator import build_plan
from .policy import validate_resource_metadata
class GlobalStorageCoreService:
 def providers(self): return list_providers()
 def provider(self,provider_id): return get_provider(provider_id)
 def domains(self): return list_domains()
 def validate_resource(self,payload): return validate_resource_metadata(payload)
 def plan(self,**kwargs): return build_plan(**kwargs)
