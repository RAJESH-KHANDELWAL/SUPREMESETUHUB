from dataclasses import dataclass
@dataclass(frozen=True)
class ProviderLifecycleEvent:
 provider_id:str="salesforce_einstein"
 event_type:str="CATALOG_REGISTERED"
 live_connection_verified:bool=False
