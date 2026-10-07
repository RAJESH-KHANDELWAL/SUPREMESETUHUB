from __future__ import annotations

from typing import Any, Callable


class ConnectorAdapter:
    """
    Adapter for one external service.

    The external service remains on its own
    official infrastructure.
    """

    def __init__(
        self,
        name: str,
        handler: Callable[..., Any],
    ) -> None:
        self.name = name.strip().lower()
        self.handler = handler

        if not self.name:
            raise ValueError("CONNECTOR_ADAPTER_NAME_REQUIRED")

        if not callable(self.handler):
            raise ValueError("CONNECTOR_HANDLER_REQUIRED")

    def execute(self, **payload: Any) -> Any:
        return self.handler(**payload)


class ConnectorAdapterManager:
    """
    Manages authorized connector adapters.
    """

    def __init__(self) -> None:
        self._adapters: dict[str, ConnectorAdapter] = {}

    def register(
        self,
        adapter: ConnectorAdapter,
    ) -> dict[str, Any]:

        self._adapters[adapter.name] = adapter

        return {
            "success": True,
            "name": adapter.name,
            "status": "REGISTERED",
        }

    def get(
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

    def execute(
        self,
        name: str,
        **payload: Any,
    ) -> Any:

        adapter = self.get(name)

        return adapter.execute(
            **payload
        )

    def list(self) -> list[dict[str, Any]]:

        return [
            {
                "name": adapter.name,
                "status": "REGISTERED",
            }
            for adapter in self._adapters.values()
        ]


adapter_manager = ConnectorAdapterManager()
