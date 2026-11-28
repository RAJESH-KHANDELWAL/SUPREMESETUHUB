"""Provider metadata package; no external network calls."""
from pathlib import Path
import re
_folder=Path(__file__).resolve().parent.name.removesuffix("_hosting_core_ecosystem").removeprefix("global_")
def _provider_id():
 try:
  from ..catalog import list_providers
  for item in list_providers():
   if re.sub(r"[^a-z0-9]+","_",item["provider_id"].lower()).strip("_")==_folder:return item["provider_id"]
 except Exception:pass
 return _folder.upper()
class HostingProviderManager:
 def status(self):return {"success":True,"provider_id":_provider_id(),"status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_transport_in_core":False,"persistence_enabled":False}
 def get_metadata(self):return self.status()
def get_manager():return HostingProviderManager()
