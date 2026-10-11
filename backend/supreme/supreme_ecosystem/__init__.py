"""SUPREME ECOSYSTEM package and public connector interface."""

from .supreme_ecosystem import (
    ACCESS_POLICY,
    CORE_MODULES,
    PARENT_SYSTEM,
    SYSTEM_NAME,
    SupremeEcosystem,
    supreme_ecosystem,
)
from .connectors.base import (
    ConnectorResult,
    ConnectorCapability,
    EcosystemProviderConnector,
)
from .connectors.registry import ConnectorRegistry, registry
from .connectors.manager import ConnectorManager, connector_manager

__all__ = [
    "ACCESS_POLICY", "CORE_MODULES", "PARENT_SYSTEM", "SYSTEM_NAME",
    "SupremeEcosystem", "supreme_ecosystem",
    "ConnectorResult", "ConnectorCapability", "EcosystemProviderConnector",
    "ConnectorRegistry", "registry", "ConnectorManager", "connector_manager",
]
