"""SUPREMESETUHUB external connectors."""

from .adapters import ConnectorAdapter
from .https import ExternalHTTPSConnector
from .http import ExternalHTTPConnector
from .manager import ConnectorManager
from .registry import Connector
from .registry import ConnectorRegistry
from .registry import connector_registry
from .tls import TLSConfiguration
from .tls import tls_configuration

__all__ = [
    "Connector",
    "ConnectorRegistry",
    "connector_registry",
    "ConnectorAdapter",
    "ConnectorManager",
    "ExternalHTTPConnector",
    "ExternalHTTPSConnector",
    "TLSConfiguration",
    "tls_configuration",
]
