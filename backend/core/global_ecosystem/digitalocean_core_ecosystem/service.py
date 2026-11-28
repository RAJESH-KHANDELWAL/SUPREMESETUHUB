"""DigitalOcean CORE capability router; validation only."""
from .digitalocean_cloud_core_ecosystem.contracts import validate_request as validate_cloud
from .digitalocean_hosting_core_ecosystem.contracts import validate_request as validate_hosting
from .digitalocean_server_core_ecosystem.contracts import validate_request as validate_server
from .digitalocean_storage_core_ecosystem.contracts import validate_request as validate_storage
from .digitalocean_vps_core_ecosystem.contracts import validate_request as validate_vps
_VALIDATORS={"cloud":validate_cloud,"hosting":validate_hosting,"server":validate_server,"storage":validate_storage,"vps":validate_vps}
class DigitalOceanCoreService:
    live_provider_calls_enabled=False
    def validate(self,capability,payload):
        if not isinstance(capability,str) or capability not in _VALIDATORS: raise ValueError("unknown DigitalOcean CORE capability")
        return {"provider":"digitalocean",**_VALIDATORS[capability](payload)}
    def execute(self,*args,**kwargs): raise RuntimeError("LIVE_PROVIDER_CALLS_DISABLED: use approved DigitalOcean API/ENGINE adapter")
