"""GLOBAL DNS ECOSYSTEM public interfaces."""
from .registry import list_providers, get_provider
from .service import GlobalDNSService
from .manager import GlobalDNSManager
from .models import DNSRecord, DNSChangeRequest, DNSProviderClient

__all__ = [
    "list_providers", "get_provider", "GlobalDNSService", "GlobalDNSManager",
    "DNSRecord", "DNSChangeRequest", "DNSProviderClient",
]
