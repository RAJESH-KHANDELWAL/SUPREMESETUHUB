from dataclasses import dataclass
@dataclass(frozen=True)
class ProviderLifecycleEvent:
 provider_id:str="nemotron_models"
 event_type:str="CATALOG_REGISTERED"
 live_connection_verified:bool=False
