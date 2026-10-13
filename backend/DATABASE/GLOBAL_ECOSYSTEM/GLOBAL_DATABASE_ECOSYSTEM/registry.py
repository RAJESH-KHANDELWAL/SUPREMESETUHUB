"""Safe metadata registry for database ecosystem providers."""
PROVIDERS = [
 {"provider_id":"google","name":"Google database services","status":"not_configured"},
 {"provider_id":"aws","name":"AWS database services","status":"not_configured"},
 {"provider_id":"microsoft","name":"Microsoft database services","status":"not_configured"},
]
def list_providers(): return [dict(p) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p)
 raise KeyError(f"Unknown database provider: {provider_id!r}")
