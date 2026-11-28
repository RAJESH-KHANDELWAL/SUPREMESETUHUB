from __future__ import annotations

from dataclasses import asdict, dataclass
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
    availability_status: str | None = None

    def public_info(self) -> dict[str, Any]:
        data = asdict(self)
        data.pop("handler", None)
        data["capabilities"] = list(self.capabilities)
        if self.handler is not None:
            data["status"] = "CONNECTED"
        else:
            data["status"] = self.availability_status or "NOT_CONFIGURED"
        return data


class ConnectorRegistry:
    """Registry for external providers and locally available catalog adapters."""

    def __init__(self) -> None:
        self._connectors: dict[str, Connector] = {}

    def register(self, connector: Connector) -> dict[str, Any]:
        key = connector.name.strip().lower()
        if not key:
            raise ValueError("CONNECTOR_NAME_REQUIRED")
        self._connectors[key] = connector
        return connector.public_info()

    def get(self, name: str) -> Connector:
        key = name.strip().lower()
        connector = self._connectors.get(key)
        if connector is None:
            raise ValueError("CONNECTOR_NOT_FOUND")
        return connector

    def list(self, category: str | None = None) -> list[dict[str, Any]]:
        wanted = category.strip().lower() if category else None
        result = []
        for connector in self._connectors.values():
            if wanted and connector.category.lower() != wanted:
                continue
            result.append(connector.public_info())
        return sorted(result, key=lambda item: item["name"])

    def categories(self) -> list[str]:
        return sorted({item.category for item in self._connectors.values()})

    def execute(self, name: str, **payload: Any) -> Any:
        connector = self.get(name)
        if connector.handler is None:
            raise ValueError("CONNECTOR_NOT_CONFIGURED")
        return connector.handler(**payload)


connector_registry = ConnectorRegistry()


# Registered external providers and resource-catalog connectors.
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
        official_api="https://generativelanguage.googleapis.com",
        handler=None,
    )
)
connector_registry.register(
    Connector(
        name="bada_business",
        display_name="Bada Business",
        category="business_ecosystem",
        region="IN",
        capabilities=(
            "RESOURCE_CATALOG",
            "REFERRAL_LINK_DIRECTORY",
            "PROGRAM_DIRECTORY",
            "RESOURCE_LOOKUP",
        ),
        auth="NOT_REQUIRED_FOR_CATALOG; PROVIDER_AUTH_NOT_CONFIGURED",
        official_api="https://www.badabusiness.com",
        handler=None,
        availability_status="CATALOG_ONLY",
    )
)
