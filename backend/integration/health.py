from typing import Any, Dict

from .registry import IntegrationRegistry


class IntegrationHealth:
    """Global integration health service with evidence-based readiness counts."""

    def __init__(self):
        self.registry = IntegrationRegistry()

    def status(self) -> Dict[str, Any]:
        providers = self.registry.health()
        configured_count = sum(
            1 for provider in providers
            if provider.get("authentication") == "CONFIGURED"
        )
        connected_count = sum(
            1 for provider in providers
            if provider.get("connection") == "CONNECTED"
            and provider.get("live_connection_verified") is True
        )
        return {
            "system": "SUPREMESETUHUB",
            "integration_count": len(providers),
            "configured_count": configured_count,
            "connected_count": connected_count,
            "ready_count": connected_count,
            "providers": providers,
            "note": "Configured credentials are not proof of live connectivity; connected_count requires a verified provider check.",
        }
