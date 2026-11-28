from dataclasses import dataclass
@dataclass(frozen=True)
class ProviderLifecycleEvent:
 provider_id:str="stable_diffusion_models"
 event_type:str="CATALOG_REGISTERED"
 live_connection_verified:bool=False
