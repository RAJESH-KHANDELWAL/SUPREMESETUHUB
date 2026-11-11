"""Domain service: catalog lookup and request-plan construction only."""
from collections.abc import Mapping
from typing import Any
from .catalog import ANTHROPIC_CAPABILITIES, get_capability, provider_catalog
from .constants import PROVIDER_ID, STATUS_CATALOG_ONLY
from .models import AnthropicRequestPlan
from .validation import reject_inline_secrets, validate_messages_payload

class AnthropicEcosystemService:
    provider_id = PROVIDER_ID

    def catalog(self) -> dict:
        return provider_catalog()

    def capabilities(self) -> tuple:
        return tuple(ANTHROPIC_CAPABILITIES.values())

    def plan(self, capability_id: str, operation: str,
             payload: Mapping[str, Any] | None = None,
             metadata: Mapping[str, Any] | None = None) -> AnthropicRequestPlan:
        capability = get_capability(capability_id)
        body, meta = dict(payload or {}), dict(metadata or {})
        if not operation.strip():
            raise ValueError("operation is required")
        reject_inline_secrets(body)
        reject_inline_secrets(meta)
        if capability.capability_id == "messages":
            validate_messages_payload(body)
        if capability.requires_explicit_permission and not meta.get("permission_granted", False):
            raise PermissionError(f"{capability_id} requires authorization in the authorization layer")
        return AnthropicRequestPlan(
            capability_id=capability.capability_id, operation=operation.strip(),
            payload=body,
            metadata={**meta, "provider_id": PROVIDER_ID,
                      "provider_status": STATUS_CATALOG_ONLY,
                      "execution_required": True},
        )
