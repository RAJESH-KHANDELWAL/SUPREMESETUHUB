"""Metadata-only provider registry; no network calls are made."""
PROVIDERS = [
 {"provider_id":"hostinger","name":"Hostinger VPS","status":"not_configured"},
 {"provider_id":"digitalocean","name":"DigitalOcean Droplets","status":"not_configured"},
 {"provider_id":"hetzner","name":"Hetzner Cloud","status":"not_configured"},
 {"provider_id":"aws-lightsail","name":"AWS Lightsail","status":"not_configured"},
]
def list_providers(): return [dict(p) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p)
 raise KeyError(f"Unknown VPS provider: {provider_id!r}")
