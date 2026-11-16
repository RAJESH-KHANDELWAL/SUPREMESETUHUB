"""Cohere CORE validation facade.

Requests are dispatched to capability-owned contracts. This module performs no
HTTP transport, SDK execution, credential exchange, persistence or UI work.
"""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .catalog import CAPABILITIES, get_cohere_core_catalog
from .contracts import CapabilityRequest, CoreResult, TenantContext
from .policy import CohereCorePolicy, ensure_operation_allowed
from .cohere_shared_security.policy import assert_no_secret_fields
from .cohere_classify_core_ecosystem.contracts import ClassifyRequest
from .cohere_classify_core_ecosystem.service import ClassifyCoreService
from .cohere_command_core_ecosystem.contracts import CommandRequest
from .cohere_command_core_ecosystem.service import CommandCoreService
from .cohere_embed_core_ecosystem.contracts import EmbedRequest
from .cohere_embed_core_ecosystem.service import EmbedCoreService
from .cohere_rerank_core_ecosystem.contracts import RerankRequest
from .cohere_rerank_core_ecosystem.service import RerankCoreService
from .cohere_tokenize_core_ecosystem.contracts import TokenizeRequest
from .cohere_tokenize_core_ecosystem.service import TokenizeCoreService


def _required_string(value: Any, field: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    return value


def _string_tuple(value: Any, field: str) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, (list, tuple)):
        raise ValueError(f"{field} must be a list or tuple of strings")
    if any(not isinstance(item, str) for item in value):
        raise ValueError(f"{field} must contain only strings")
    return tuple(value)


def _record_tuple(value: Any, field: str) -> tuple[dict, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, (list, tuple)):
        raise ValueError(f"{field} must be a list or tuple")
    if any(not isinstance(item, Mapping) for item in value):
        raise ValueError(f"{field} must contain mapping items")
    return tuple(dict(item) for item in value)


class CohereCoreService:
    """Stable provider facade for discovery, policy and contract validation."""

    def capabilities(self) -> dict[str, dict[str, Any]]:
        return {name: dict(metadata) for name, metadata in CAPABILITIES.items()}

    def status(self) -> dict[str, Any]:
        catalog = get_cohere_core_catalog()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": catalog["name"],
            "provider": "cohere",
            "layer": "CORE",
            "status": "interface_only",
            "capability_count": len(CAPABILITIES),
            "live_provider_calls_enabled": False,
            "live_connection_verified": False,
            "api_calls_performed": 0,
        }

    def validate(self, request: CapabilityRequest) -> CoreResult:
        if not isinstance(request, CapabilityRequest):
            return CoreResult(False, "", errors=("request must be a CapabilityRequest",), status="rejected")
        if not isinstance(request.capability, str):
            return CoreResult(False, "", errors=("capability must be a string",), status="rejected")

        capability = request.capability.strip().lower()
        if capability not in CAPABILITIES:
            return CoreResult(False, capability, errors=("Unsupported Cohere capability",), status="rejected")
        if not isinstance(request.inputs, Mapping):
            return CoreResult(False, capability, errors=("inputs must be a mapping",), status="rejected")
        if not isinstance(request.options, Mapping):
            return CoreResult(False, capability, errors=("options must be a mapping",), status="rejected")
        if request.model is not None and (not isinstance(request.model, str) or not request.model.strip()):
            return CoreResult(False, capability, errors=("model must be a non-empty string when supplied",), status="rejected")

        values = dict(request.inputs)
        try:
            assert_no_secret_fields(values)
            assert_no_secret_fields(dict(request.options))
            if request.options:
                raise ValueError("options are not defined by the current CORE contracts; execution options belong to API/ENGINE")
            allowed_fields = {
                "classify": {"inputs", "examples"},
                "command": {"message", "chat_history"},
                "embed": {"texts", "input_type"},
                "rerank": {"query", "documents", "top_n"},
                "tokenize": {"text"},
            }[capability]
            unexpected = set(values) - allowed_fields
            if unexpected:
                raise ValueError("unsupported input fields: " + ", ".join(sorted(str(key) for key in unexpected)))
            if capability == "classify":
                typed = ClassifyRequest(
                    inputs=_string_tuple(values.get("inputs"), "inputs"),
                    model=request.model,
                    examples=_record_tuple(values.get("examples", ()), "examples"),
                )
                ClassifyCoreService().validate(typed)
            elif capability == "command":
                typed = CommandRequest(
                    message=_required_string(values.get("message", ""), "message"),
                    model=request.model,
                    chat_history=_record_tuple(values.get("chat_history", ()), "chat_history"),
                )
                CommandCoreService().validate(typed)
            elif capability == "embed":
                typed = EmbedRequest(
                    texts=_string_tuple(values.get("texts"), "texts"),
                    model=request.model,
                    input_type=values.get("input_type"),
                )
                EmbedCoreService().validate(typed)
            elif capability == "rerank":
                typed = RerankRequest(
                    query=_required_string(values.get("query", ""), "query"),
                    documents=_string_tuple(values.get("documents"), "documents"),
                    top_n=values.get("top_n"),
                )
                RerankCoreService().validate(typed)
            else:
                typed = TokenizeRequest(
                    text=_required_string(values.get("text", ""), "text"),
                    model=request.model,
                )
                TokenizeCoreService().validate(typed)
        except (TypeError, ValueError) as exc:
            return CoreResult(False, capability, errors=(str(exc),), status="rejected")

        return CoreResult(
            True,
            capability,
            data={"model": request.model, "input_keys": tuple(sorted(str(key) for key in values))},
            status="validated",
        )

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        try:
            CohereCorePolicy.require_tenant_context(context)
            CohereCorePolicy.validate_capability(capability)
        except (TypeError, ValueError, PermissionError) as exc:
            return {
                "success": False,
                "status": "POLICY_DENIED",
                "capability": capability if isinstance(capability, str) else "",
                "errors": [str(exc)],
                "api_call_performed": False,
            }
        return {
            "success": True,
            "status": "CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED",
            "capability": capability.strip().lower(),
            "tenant_id": context.tenant_id,
            "actor_id": context.actor_id,
            "authorization_class": CohereCorePolicy.classify_capability(capability),
            "api_call_performed": False,
        }

    def authorize_operation(self, operation: str, *, explicitly_authorized: bool = False) -> None:
        ensure_operation_allowed(operation, explicitly_authorized=explicitly_authorized)
