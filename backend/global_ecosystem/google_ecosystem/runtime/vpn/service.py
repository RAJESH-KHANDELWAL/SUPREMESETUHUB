"""Google Cloud VPN capabilities; descriptive metadata only."""
from __future__ import annotations

from ..core.service import capability

CAPABILITIES = [
    capability("vpn", "Google Cloud VPN", "Cloud VPN / Compute Engine APIs", notes="Setup requires network topology, gateways, peer details, routing, and approved configuration; no tunnel is created by this catalog."),
]


def get_capabilities() -> list[dict]:
    return [dict(item) for item in CAPABILITIES]
