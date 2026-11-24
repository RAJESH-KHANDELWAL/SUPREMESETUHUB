"""Discoverable Anthropic capability catalog; not a live API client."""
from types import MappingProxyType
from .constants import PROVIDER_ID
from .models import AnthropicCapability

_CAPABILITIES = {
    "messages": AnthropicCapability("messages", "Messages", "Create conversational model responses.", "POST /v1/messages"),
    "message_batches": AnthropicCapability("message_batches", "Message Batches", "Submit and retrieve asynchronous message batches.", "/v1/messages/batches"),
    "models": AnthropicCapability("models", "Models", "Discover available model identifiers and metadata.", "GET /v1/models"),
    "token_counting": AnthropicCapability("token_counting", "Token Counting", "Estimate input token usage before execution.", "POST /v1/messages/count_tokens"),
    "files": AnthropicCapability("files", "Files", "Manage provider-supported file resources.", "/v1/files", requires_explicit_permission=True),
    "admin_workspaces": AnthropicCapability("admin_workspaces", "Admin Workspaces", "Administrative workspace operations.", "/v1/organizations/workspaces", requires_explicit_permission=True),
    "managed_agents": AnthropicCapability("managed_agents", "Managed Agents", "Managed agent capabilities where enabled.", "provider-managed agent surface", requires_explicit_permission=True),
    "tool_use": AnthropicCapability("tool_use", "Tool Use", "Describe and validate model tool-use requests.", "Messages API tool definitions"),
    "auth_identity": AnthropicCapability("auth_identity", "Authentication Identity", "Credential readiness metadata only.", "credential readiness only", requires_explicit_permission=True),
}
ANTHROPIC_CAPABILITIES = MappingProxyType(_CAPABILITIES)
ANTHROPIC_PROVIDER = MappingProxyType({
    "provider_id": PROVIDER_ID, "provider_name": "Anthropic",
    "provider_type": "foundation_model_provider",
    "status": "CATALOG_ONLY", "live_connection_verified": False,
})

def get_capability(capability_id: str) -> AnthropicCapability:
    key = capability_id.strip().lower()
    try:
        return ANTHROPIC_CAPABILITIES[key]
    except KeyError as exc:
        raise KeyError(f"Unknown Anthropic capability: {capability_id}") from exc

def provider_catalog() -> dict:
    return {
        **dict(ANTHROPIC_PROVIDER), "catalog_version": "1.0.0",
        "capabilities": [
            {"capability_id": item.capability_id, "display_name": item.display_name,
             "description": item.description, "api_surface": item.api_surface,
             "enabled_by_default": item.enabled_by_default,
             "requires_explicit_permission": item.requires_explicit_permission,
             "status": item.status}
            for item in ANTHROPIC_CAPABILITIES.values()
        ],
    }
