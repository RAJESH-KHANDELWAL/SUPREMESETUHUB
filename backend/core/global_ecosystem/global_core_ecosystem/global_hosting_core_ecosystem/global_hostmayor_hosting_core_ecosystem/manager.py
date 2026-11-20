"""Provider-package metadata manager; no external API calls are made."""
from pathlib import Path
_folder=Path(__file__).resolve().parent.name.removesuffix("_hosting_core_ecosystem")
PROVIDER_ID=_folder.removeprefix("global_").upper()
class HostingProviderManager:
 def status(self):
  return {"provider_id":PROVIDER_ID,"status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_transport_in_core":False,"persistence_enabled":False}
 def get_metadata(self):return self.status()
def get_manager():return HostingProviderManager()
