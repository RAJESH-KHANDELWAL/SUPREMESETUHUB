from __future__ import annotations

from typing import Any

from .adapters import ConnectorAdapter
from .registry import ConnectorRegistry


class ConnectorManager:
    """
    Central manager for SUPREMESETUHUB external connectors.

    Registry:
        Stores connector metadata.

    Adapter:
        Executes an authorized provider integration.

    External services remain on their own infrastructure.
    """

    def __init__(
        self,
        registry: ConnectorRegistry,
    ) -> None:

        self.registry = registry
        self._adapters: dict[str, ConnectorAdapter] = {}

    def register_adapter(
        self,
        adapter: ConnectorAdapter,
    ) -> dict[str, Any]:

        name = adapter.name.strip().lower()

        if not name:
            raise ValueError(
                "CONNECTOR_NAME_REQUIRED"
            )

        self._adapters[name] = adapter

        return {
            "success": True,
            "connector": name,
            "status": "REGISTERED",
        }

    def has_adapter(
        self,
        name: str,
    ) -> bool:

        return name.strip().lower() in self._adapters

    def get_adapter(
        self,
        name: str,
    ) -> ConnectorAdapter:

        key = name.strip().lower()

        adapter = self._adapters.get(key)

        if adapter is None:
            raise ValueError(
                "CONNECTOR_ADAPTER_NOT_FOUND"
            )

        return adapter

    def list_connectors(
        self,
        category: str | None = None,
    ) -> list[dict[str, Any]]:

        connectors = self.registry.list(
            category=category
        )

        result = []

        for connector in connectors:

            name = connector["name"]

            item = dict(connector)

            item["adapter"] = (
                "READY"
                if self.has_adapter(name)
                else "NOT_CONFIGURED"
            )

            result.append(item)

        return result

    def execute(
        self,
        name: str,
        **payload: Any,
    ) -> Any:

        adapter = self.get_adapter(name)

        return adapter.execute(
            **payload
        )

    def status(self) -> dict[str, Any]:

        connectors = self.list_connectors()

        return {
            "success": True,
            "total_connectors": len(connectors),
            "configured_adapters": sum(
                1
                for connector in connectors
                if connector["adapter"] == "READY"
            ),
            "connectors": connectors,
        }
