"""Provider facade registry; transport belongs in the API layer."""
from ..catalog import get_provider,list_providers
from ..module_service import ToolProviderCoreService
class RegisteredToolProviderService(ToolProviderCoreService):
 def __init__(self,key): self.PROVIDER_ID=key; super().__init__()
def get_provider_service(key):
 p=get_provider(key)
 if p is None: raise LookupError("TOOLS_PROVIDER_NOT_REGISTERED")
 return RegisteredToolProviderService(p["provider_id"])
def list_provider_services(): return [get_provider_service(x["provider_id"]) for x in list_providers()]
