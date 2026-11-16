"""Bada Business DNS capability metadata; not a DNS provider catalog."""
BADA_BUSINESS_DNS_ECOSYSTEM = {
    "ecosystem_id": "BADA-BUSINESS-DNS-ECOSYSTEM",
    "provider_id": "bada_business",
    "layer": "DNS",
    "purpose": "Bada Business tenant-domain DNS orchestration facade",
    "capabilities": [
        "tenant-domain-binding",
        "provider-neutral-record-discovery",
        "approved-dns-record-change-dispatch",
        "domain-dns-status",
    ],
    "supported_dns_providers": [
        "cloudflare", "google", "hostinger", "namecheap", "route53"
    ],
    "live_connection_verified": False,
}
