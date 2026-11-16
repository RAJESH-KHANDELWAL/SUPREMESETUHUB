"""Provider-level Cohere CORE registry and capability validation facade.

This layer validates contracts only. It never calls Cohere or executes provider work.
"""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Callable

from .contracts import CapabilityRequest, CoreResult
from .policies import ensure_operation_allowed
from .capabilities.catalog import CAPABILITIES
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


def _string_tuple(value: Any, field: str) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, (list, tuple)):
        raise ValueError(f"{field} must be a list or tuple of strings")
    if any(not isinstance(item, str) for item in value):
        raise ValueError(f"{field} must contain only strings")
    return tuple(value)


class CohereCoreService:
    """Stable provider facade that dispatches to capability-specific validators."""

    def capabilities(self):
        return {name: dict(metadata) for name, metadata in CAPABILITIES.items()}

    def validate(self, request: CapabilityRequest) -> CoreResult:
        if not isinstance(request, CapabilityRequest):
            return CoreResult(False, "", errors=("request must be a CapabilityRequest",), status="rejected")

        capability = request.capability.strip().lower()
        if capability not in CAPABILITIES:
            return CoreResult(False, capability, errors=("Unsupported Cohere capability",), status="rejected")
        if not isinstance(request.inputs, Mapping):
            return CoreResult(False, capability, errors=("inputs must be a mapping",), status="rejected")

        values = dict(request.inputs)
        try:
            if capability == "classify":
                typed_request = ClassifyRequest(
                    inputs=_string_tuple(values.get("inputs"), "inputs"),
                    model=request.model,
                    examples=tuple(values.get("examples", ())),
                )
                ClassifyCoreService().validate(typed_request)
            elif capability == "command":
                typed_request = CommandRequest(
                    message=values.get("message", ""),
                    model=request.model,
                    chat_history=tuple(values.get("chat_history", ())),
                )
                CommandCoreService().validate(typed_request)
            elif capability == "embed":
                typed_request = EmbedRequest(
                    texts=_string_tuple(values.get("texts"), "texts"),
                    model=request.model,
                    input_type=values.get("input_type"),
                )
                EmbedCoreService().validate(typed_request)
            elif capability == "rerank":
                typed_request = RerankRequest(
                    query=values.get("query", ""),
                    documents=_string_tuple(values.get("documents"), "documents"),
                    top_n=values.get("top_n"),
                )
                RerankCoreService().validate(typed_request)
            else:
                typed_request = TokenizeRequest(
                    text=values.get("text", ""),
                    model=request.model,
                )
                TokenizeCoreService().validate(typed_request)
        except (TypeError, ValueError) as exc:
            return CoreResult(False, capability, errors=(str(exc),), status="rejected")

        return CoreResult(
            True,
            capability,
            data={"model": request.model, "input_keys": tuple(sorted(values.keys()))},
            status="validated",
        )

    def authorize_operation(self, operation: str) -> None:
        ensure_operation_allowed(operation)
