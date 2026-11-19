"""VPN provider metadata; this registry does not start or change tunnels."""
PROVIDERS = [
 {"provider_id":"wireguard","name":"WireGuard","capabilities":["vpn-tunnel-management"],"status":"not_configured"},
 {"provider_id":"openvpn","name":"OpenVPN","capabilities":["vpn-tunnel-management"],"status":"not_configured"},
 {"provider_id":"tailscale","name":"Tailscale","capabilities":["mesh-vpn-management"],"status":"not_configured"},
 {"provider_id":"protonvpn","name":"Proton VPN","capabilities":["privacy-vpn-service"],"status":"not_configured"},
]
def list_providers(): return [dict(p, capabilities=list(p["capabilities"])) for p in PROVIDERS]
def get_provider(provider_id):
 for p in PROVIDERS:
  if p["provider_id"] == provider_id.strip().lower(): return dict(p, capabilities=list(p["capabilities"]))
 raise KeyError(f"Unknown VPN provider: {provider_id!r}")
