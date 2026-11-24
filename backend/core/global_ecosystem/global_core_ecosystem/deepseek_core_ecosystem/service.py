"""DeepSeek Core request-contract dispatcher; never performs provider transport."""
from __future__ import annotations

from typing import Any

from .deepseek_chat_completions_core_ecosystem.contracts import validate_request as validate_chat_completions
from .deepseek_responses_core_ecosystem.contracts import validate_request as validate_responses
from .deepseek_search_core_ecosystem.contracts import validate_request as validate_search
from .deepseek_fetch_core_ecosystem.contracts import validate_request as validate_fetch

_VALIDATORS = {
    "chat_completions": validate_chat_completions,
    "responses": validate_responses,
    "search": validate_search,
    "fetch": validate_fetch,
}


class DeepSeekCoreService:
    """Validate capability payloads and explicitly keep execution disabled."""

    live_provider_calls_enabled = False

    def validate(self, capability: str, payload: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(capability, str) or capability not in _VALIDATORS:
            raise ValueError("unknown DeepSeek capability")
        result = _VALIDATORS[capability](payload)
        return {
            "provider": "deepseek",
            "ecosystem_id": "DEEPSEEK-CORE-ECOSYSTEM",
            **result,
            "live_call": False,
        }

    def execute(self, *args: Any, **kwargs: Any) -> None:
        raise RuntimeError(
            "LIVE_PROVIDER_CALLS_DISABLED: use approved API/ENGINE adapter"
        )
