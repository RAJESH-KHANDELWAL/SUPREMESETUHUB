"""Read-only provider capability metadata service."""
from .catalog import list_capabilities
from .domain_catalog import list_domains
class CohereModuleService:
    def capabilities(self): return list_capabilities()
    def domains(self): return list_domains()
