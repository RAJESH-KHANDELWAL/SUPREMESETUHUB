"""GLOBAL DNS ECOSYSTEM public interfaces."""
from .registry import list_providers, get_provider
from .service import GlobalDNSService
from .manager import GlobalDNSManager
from .models import DNSRecord, DNSChangeRequest, DNSProviderClient
from .bada_business_dns_ecosystem import (
    BADA_BUSINESS_DNS_ECOSYSTEM,
    BadaBusinessDNSService,
    BadaBusinessDNSManager,
    BusinessDomainDNSBinding,
)

__all__ = [
    "list_providers", "get_provider", "GlobalDNSService", "GlobalDNSManager",
    "DNSRecord", "DNSChangeRequest", "DNSProviderClient",
    "BADA_BUSINESS_DNS_ECOSYSTEM", "BadaBusinessDNSService",
    "BadaBusinessDNSManager", "BusinessDomainDNSBinding",
]
