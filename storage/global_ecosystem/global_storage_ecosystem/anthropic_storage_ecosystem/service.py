"""Provider adapter boundary; no live Anthropic API calls are made here."""
from typing import Any

class AnthropicStorageEcosystem:
    provider_id = "anthropic"
    display_name = "Anthropic"
    capabilities = ("claude-storage-catalog", "metadata-taxonomy")

    def describe(self) -> dict[str, Any]:
        return {
            "provider_id": self.provider_id,
            "display_name": self.display_name,
            "capabilities": list(self.capabilities),
            "connection_status": "not_configured",
            "external_connections_verified": False,
        }
