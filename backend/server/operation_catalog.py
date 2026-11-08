"""Canonical SERVER-owned operational capability catalog.

Catalog entries describe responsibilities; they do not imply that a provider
or remote infrastructure is configured.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class ServerCapability:
    key: str
    responsibility: str
    requires_external_adapter: bool = True

_CAPABILITIES = (
    ServerCapability("PROVISIONING", "Create and remove compute/server resources"),
    ServerCapability("DEPLOYMENT", "Release and roll back applications and workloads"),
    ServerCapability("NETWORKING", "Manage server networks, addresses, DNS and firewall integrations"),
    ServerCapability("MONITORING", "Collect metrics, events and operational health"),
    ServerCapability("SECURITY", "Coordinate server access, policy and security integrations"),
    ServerCapability("BACKUP", "Coordinate server backup and recovery operations"),
    ServerCapability("SCALING", "Coordinate capacity and scaling operations"),
)

def list_capabilities():
    return _CAPABILITIES

def get_capability(key: str):
    normalized = str(key or "").strip().upper()
    return next((item for item in _CAPABILITIES if item.key == normalized), None)

__all__ = ["ServerCapability", "list_capabilities", "get_capability"]
