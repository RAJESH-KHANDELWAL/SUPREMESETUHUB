"""Metadata registry; does not connect to servers."""
PROVIDERS = [
 {"provider_id":"hostinger","name":"Hostinger Servers","capabilities":["server-management"],"status":"not_configured"},
 {"provider_id":"aws","name":"AWS Compute","capabilities":["cloud-server-management"],"status":"not_configured"},
 {"provider_id":"google","name":"Google Cloud Compute","capabilities":["cloud-server-management"],"status":"not_configured"},
 {"provider_id":"digitalocean","name":"DigitalOcean","capabilities":["cloud-server-management"],"status":"not_configured"},
 {"provider_id":"azure","name":"Azure Compute","capabilities":["cloud-server-management"],"status":"not_configured"},
]
def list_providers(): return [dict(p, capabilities=list(p["capabilities"])) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p, capabilities=list(p["capabilities"]))
 raise KeyError(f"Unknown server provider: {provider_id!r}")
