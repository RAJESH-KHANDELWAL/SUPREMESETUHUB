"""Resolve Google subsystem names to their metadata modules."""
from __future__ import annotations

from importlib import import_module

_SUBSYSTEM_MODULES = {
    "cloud": "backend.global_ecosystem.google_ecosystem.runtime.cloud.service",
    "database": "backend.global_ecosystem.google_ecosystem.runtime.database.service",
    "dns": "backend.global_ecosystem.google_ecosystem.runtime.dns.service",
    "storage": "backend.global_ecosystem.google_ecosystem.runtime.storage.service",
    "vps": "backend.global_ecosystem.google_ecosystem.runtime.vps.service",
    "vpn": "backend.global_ecosystem.google_ecosystem.runtime.vpn.service",
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
