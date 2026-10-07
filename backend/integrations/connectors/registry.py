from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Callable


@dataclass(frozen=True)
class Connector:
    name: str
    display_name: str
    category: str
    region: str
    capabilities: tuple[str, ...]
    auth: str
    official_api: str
    handler: Callable[..., Any] | None = None

    def public_info(self) -> dict[str, Any]:
        data = asdict(self)
        data.pop("handler", None)
        data["capabilities"] = list(self.capabilities)
        data["status"] = (
            "CONNECTED"
            if self.handler
            else "AVAILABLE"
        )
        return data


class ConnectorRegistry:
    """
    Universal external connector registry.

    External AI/platform services remain on their
    own official infrastructure.

    SUPREMESETUHUB only maintains connector metadata
    and authorized adapter execution.
    """

    def __init__(self) -> None:
        self._connectors: dict[str, Connector] = {}

    def register(
        self,
        connector: Connector,
    ) -> dict[str, Any]:

        key = connector.name.strip().lower()

        if not key:
            raise ValueError(
                "CONNECTOR_NAME_REQUIRED"
            )

        self._connectors[key] = connector

        return connector.public_info()

    def get(self, name: str) -> Connector:

        key = name.strip().lower()

        connector = self._connectors.get(key)

        if connector is None:
            raise ValueError(
                "CONNECTOR_NOT_FOUND"
            )

        return connector

    def list(
        self,
        category: str | None = None,
    ) -> list[dict[str, Any]]:

        wanted = (
            category.strip().lower()
            if category
            else None
        )

        result = []

        for connector in self._connectors.values():

            if (
                wanted
                and connector.category.lower()
                != wanted
            ):
                continue

            result.append(
                connector.public_info()
            )

        return sorted(
            result,
            key=lambda item: item["name"],
        )

    def categories(self) -> list[str]:

        return sorted(
            {
                connector.category
                for connector
                in self._connectors.values()
            }
        )

    def execute(
        self,
        name: str,
        **payload: Any,
    ) -> Any:

        connector = self.get(name)

        if connector.handler is None:
            raise ValueError(
                "CONNECTOR_NOT_CONFIGURED"
            )

        return connector.handler(
            **payload
        )


connector_registry = ConnectorRegistry()


# ============================================================
# EXISTING REAL EXTERNAL PROVIDERS
# ============================================================

connector_registry.register(
    Connector(
        name="openai_image",
        display_name="OpenAI Image",
        category="image",
        region="GLOBAL",
        capabilities=("image",),
        auth="environment/provider_credentials",
        official_api="https://api.openai.com",
        handler=None,
    )
)


connector_registry.register(
    Connector(
        name="google_veo",
        display_name="Google Veo",
        category="video",
        region="GLOBAL",
        capabilities=("video",),
        auth="environment/provider_credentials",
        official_api=(
            "https://generativelanguage.googleapis.com"
        ),
        handler=None,
    )
)
