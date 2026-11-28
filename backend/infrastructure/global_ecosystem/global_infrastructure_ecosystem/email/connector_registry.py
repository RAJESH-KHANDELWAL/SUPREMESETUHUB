"""Email provider connector registry for SUPREMESETUHUB."""

from __future__ import annotations

from typing import Dict

from .provider_connector import EmailProviderConnector


class EmailProviderConnectorRegistry:
    """Central registry for email provider connectors."""

    def __init__(self) -> None:
        self._connectors: Dict[str, EmailProviderConnector] = {}

    def register(
        self,
        connector: EmailProviderConnector,
    ) -> None:
        """Register or replace a provider connector."""
        self._connectors[connector.provider_id] = connector

    def get(
        self,
        provider_id: str,
    ) -> EmailProviderConnector | None:
        """Return a registered connector."""
        return self._connectors.get(provider_id)

    def has(
        self,
        provider_id: str,
    ) -> bool:
        """Check whether a connector is registered."""
        return provider_id in self._connectors

    def list_all(self) -> list[EmailProviderConnector]:
        """Return all registered connectors."""
        return list(self._connectors.values())

    def list_ids(self) -> list[str]:
        """Return registered provider IDs."""
        return list(self._connectors.keys())

    def metadata(self) -> list[dict]:
        """Return non-sensitive connector metadata."""
        return [
            connector.metadata()
            for connector in self._connectors.values()
        ]


email_provider_connector_registry = (
    EmailProviderConnectorRegistry()
)
