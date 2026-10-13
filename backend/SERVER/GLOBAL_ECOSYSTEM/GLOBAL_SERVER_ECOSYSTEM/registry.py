"""Metadata-only provider registry; no network calls are made."""
PROVIDERS = [
 {"provider_id":"hostinger","name":"Hostinger Servers","status":"not_configured"},
 {"provider_id":"aws","name":"AWS Compute","status":"not_configured"},
 {"provider_id":"google","name":"Google Cloud Compute","status":"not_configured"},
 {"provider_id":"digitalocean","name":"DigitalOcean","status":"not_configured"},
 {"provider_id":"azure","name":"Microsoft Azure","status":"not_configured"},
]
def list_providers(): return [dict(p) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p)
 raise KeyError(f"Unknown SERVER provider: {provider_id!r}")
