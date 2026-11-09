"""Compute Engine VM capabilities; Google Cloud does not call this product VPS."""
from __future__ import annotations

from ..core.service import capability

CAPABILITIES = [
    capability("vps", "Google Compute Engine VM", "Compute Engine API", notes="No VM is provisioned here. Project, zone, machine type, network, IAM, quotas, and billing must be configured before provisioning."),
]


def get_capabilities() -> list[dict]:
    return [dict(item) for item in CAPABILITIES]
