"""DNS provider registry metadata; no provider is assumed connected."""

PROVIDERS = [
    {"provider_id": "cloudflare", "name": "Cloudflare DNS", "capabilities": ["dns-record-management"], "status": "not_configured", "adapter_module": "backend.dns.global_ecosystem.global_dns_ecosystem.cloudflare_dns"},
    {"provider_id": "google", "name": "Google Cloud DNS", "capabilities": ["authoritative-dns"], "status": "not_configured", "adapter_module": "backend.dns.global_ecosystem.global_dns_ecosystem.google_dns"},
    {"provider_id": "hostinger", "name": "Hostinger DNS", "capabilities": ["dns-record-management"], "status": "not_configured", "adapter_module": "backend.dns.global_ecosystem.global_dns_ecosystem.hostinger_dns"},
    {"provider_id": "namecheap", "name": "Namecheap DNS", "capabilities": ["domain-and-dns-management"], "status": "not_configured", "adapter_module": "backend.dns.global_ecosystem.global_dns_ecosystem.namecheap_dns"},
    {"provider_id": "route53", "name": "Amazon Route 53", "capabilities": ["authoritative-dns"], "status": "not_configured", "adapter_module": "backend.dns.global_ecosystem.global_dns_ecosystem.route53_dns"},
]

def list_providers():
    return [dict(item, capabilities=list(item["capabilities"])) for item in PROVIDERS]

def get_provider(provider_id):
    if not isinstance(provider_id, str) or not provider_id.strip():
        raise ValueError("provider_id is required")
    key = provider_id.strip().lower()
    for item in PROVIDERS:
        if item["provider_id"] == key:
            return dict(item, capabilities=list(item["capabilities"]))
    raise KeyError(f"Unknown DNS provider: {provider_id!r}")
