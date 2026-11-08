"""SERVER-owned operational capabilities for the GLOBAL SERVER ECOSYSTEM.

The catalog describes supported responsibility areas; it does not imply that
remote infrastructure or provider credentials are configured.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class ServerCapability:
    key: str
    responsibility: str
    requires_external_adapter: bool = True

_CAPABILITIES = (
    ServerCapability("PROVISIONING", "Create, inspect and remove server resources"),
    ServerCapability("DEPLOYMENT", "Deploy, update and roll back workloads"),
    ServerCapability("NETWORKING", "Coordinate network, IP, DNS and firewall operations"),
    ServerCapability("MONITORING", "Collect metrics, events and operational health"),
    ServerCapability("SECURITY", "Coordinate access controls and security policies"),
    ServerCapability("BACKUP", "Coordinate backup, restore and recovery operations"),
    ServerCapability("SCALING", "Coordinate capacity and scaling operations"),
)

def list_capabilities():
    return _CAPABILITIES

def get_capability(key: str):
    normalized = str(key or "").strip().upper()
    return next((item for item in _CAPABILITIES if item.key == normalized), None)

__all__ = ["ServerCapability", "list_capabilities", "get_capability"]
