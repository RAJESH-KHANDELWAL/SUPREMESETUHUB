"""Metadata-only provider registry; no network calls are made."""
PROVIDERS = [
 {"provider_id":"wireguard","name":"WireGuard","status":"not_configured"},
 {"provider_id":"openvpn","name":"OpenVPN","status":"not_configured"},
 {"provider_id":"tailscale","name":"Tailscale","status":"not_configured"},
 {"provider_id":"protonvpn","name":"Proton VPN","status":"not_configured"},
]
def list_providers(): return [dict(p) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p)
 raise KeyError(f"Unknown VPN provider: {provider_id!r}")
