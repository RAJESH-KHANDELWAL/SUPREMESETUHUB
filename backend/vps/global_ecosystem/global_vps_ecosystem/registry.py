"""VPS provider metadata; no provisioning actions are executed."""
PROVIDERS = [
 {"provider_id":"hostinger","name":"Hostinger VPS","capabilities":["virtual-private-servers"],"status":"not_configured"},
 {"provider_id":"digitalocean","name":"DigitalOcean Droplets","capabilities":["virtual-private-servers"],"status":"not_configured"},
 {"provider_id":"hetzner","name":"Hetzner Cloud","capabilities":["virtual-private-servers"],"status":"not_configured"},
 {"provider_id":"aws-lightsail","name":"AWS Lightsail","capabilities":["virtual-private-servers"],"status":"not_configured"},
]
def list_providers(): return [dict(p, capabilities=list(p["capabilities"])) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p, capabilities=list(p["capabilities"]))
 raise KeyError(f"Unknown VPS provider: {provider_id!r}")
