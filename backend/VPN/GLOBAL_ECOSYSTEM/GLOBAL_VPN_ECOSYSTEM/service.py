"""GLOBAL_VPN_ECOSYSTEM service facade; providers are not yet connected."""
from .registry import list_providers
class EcosystemService:
    def describe(self): return {"ecosystem": "GLOBAL_VPN_ECOSYSTEM", "providers": list_providers(), "live_connections_enabled": False}
