"""Provider-scoped read-only manager; identity is derived from package name."""
PACKAGE=__package__.rsplit(".",1)[-1]
PROVIDER_ID=PACKAGE.removesuffix("_hosting_core_ecosystem").upper()
ECOSYSTEM_ID="GLOBAL-"+PROVIDER_ID.replace("_","-")+"-HOSTING-CORE-ECOSYSTEM"
NAME="GLOBAL "+PROVIDER_ID.replace("_"," ")+" HOSTING CORE ECOSYSTEM"
class HostingProviderManager:
 def status(self):return {"success":True,"ecosystem_id":ECOSYSTEM_ID,"provider_id":PROVIDER_ID,"name":NAME,"status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_transport_in_core":False,"persistence_enabled":False}
 def capabilities(self):return {"provider_id":PROVIDER_ID,"capabilities":["HOSTING_METADATA","PROVIDER_DISCOVERY","READINESS_REPORTING"],"requires_provider_api_adapter":True}
def get_manager():return HostingProviderManager()
