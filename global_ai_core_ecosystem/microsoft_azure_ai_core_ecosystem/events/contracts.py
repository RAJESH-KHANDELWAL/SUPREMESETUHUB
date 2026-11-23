from dataclasses import dataclass
@dataclass(frozen=True)
class ProviderLifecycleEvent:
 provider_id:str="microsoft_azure_ai"
 event_type:str="CATALOG_REGISTERED"
 live_connection_verified:bool=False
