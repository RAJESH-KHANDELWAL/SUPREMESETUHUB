"""DNS provider metadata; no DNS records are changed by registry calls."""
PROVIDERS = [
 {"provider_id":"cloudflare","name":"Cloudflare DNS","capabilities":["dns-record-management"],"status":"not_configured"},
 {"provider_id":"namecheap","name":"Namecheap DNS","capabilities":["domain-and-dns-management"],"status":"not_configured"},
 {"provider_id":"hostinger","name":"Hostinger DNS","capabilities":["dns-record-management"],"status":"not_configured"},
 {"provider_id":"route53","name":"Amazon Route 53","capabilities":["authoritative-dns"],"status":"not_configured"},
 {"provider_id":"google","name":"Google Cloud DNS","capabilities":["authoritative-dns"],"status":"not_configured"},
]
def list_providers(): return [dict(p, capabilities=list(p["capabilities"])) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p, capabilities=list(p["capabilities"]))
 raise KeyError(f"Unknown DNS provider: {provider_id!r}")
