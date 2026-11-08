"""Metadata-only provider registry; no network calls are made."""
PROVIDERS = [
 {"provider_id":"google","name":"Google Cloud","status":"not_configured"},
 {"provider_id":"aws","name":"Amazon Web Services","status":"not_configured"},
 {"provider_id":"microsoft","name":"Microsoft Azure","status":"not_configured"},
 {"provider_id":"cloudflare","name":"Cloudflare","status":"not_configured"},
]
def list_providers(): return [dict(p) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p)
 raise KeyError(f"Unknown CLOUD provider: {provider_id!r}")
