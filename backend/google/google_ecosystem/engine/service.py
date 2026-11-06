"""Resolve Google subsystem names to their metadata modules."""
from __future__ import annotations

from importlib import import_module

_SUBSYSTEM_MODULES = {
    "cloud": "backend.google.google_ecosystem.cloud.service",
    "database": "backend.google.google_ecosystem.database.service",
    "dns": "backend.google.google_ecosystem.dns.service",
    "storage": "backend.google.google_ecosystem.storage.service",
    "vps": "backend.google.google_ecosystem.vps.service",
    "vpn": "backend.google.google_ecosystem.vpn.service",
}


def list_subsystems() -> list[str]:
    """Return supported subsystem keys in stable order."""
    return sorted(_SUBSYSTEM_MODULES)


def get_subsystem(subsystem: str) -> dict:
    """Load and return one subsystem's capability records."""
    key = subsystem.strip().lower()
    if key not in _SUBSYSTEM_MODULES:
        raise KeyError(f"Unsupported Google ecosystem subsystem: {subsystem}")
    module = import_module(_SUBSYSTEM_MODULES[key])
    return {"subsystem": key, "capabilities": module.get_capabilities()}
