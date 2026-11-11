"""Pure validation for Cohere request intents."""
from collections.abc import Mapping
from typing import Any

_SECRET_KEYS = frozenset({
    "api_key", "authorization", "client_secret", "access_token",
    "refresh_token", "password", "secret", "token",
})
_ALLOWED_OPERATIONS = frozenset({"infer", "generate", "chat", "embed", "rerank", "classify", "tokenize", "list", "get"})

def reject_inline_secrets(value: Any, path: str = "payload") -> None:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key).strip().lower() in _SECRET_KEYS:
                raise ValueError(f"credential-like field is not allowed at {path}.{key}")
            reject_inline_secrets(nested, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for index, nested in enumerate(value):
            reject_inline_secrets(nested, f"{path}[{index}]")

def validate_request(product_id: str, operation: str, payload: Mapping[str, Any] | None = None) -> None:
    if not isinstance(operation, str) or operation.strip().lower() not in _ALLOWED_OPERATIONS:
        raise ValueError("unsupported or missing Cohere operation")
    if payload is not None and not isinstance(payload, Mapping):
        raise TypeError("payload must be a mapping")
    body = payload or {}
    reject_inline_secrets(body)
    if product_id == "command":
        if operation.strip().lower() in {"generate", "chat", "infer"} and not any(
            key in body for key in ("message", "messages", "prompt", "inputs")
        ):
            raise ValueError("Command request requires message, messages, prompt, or inputs")
    elif product_id == "embed":
        if operation.strip().lower() == "embed" and not any(
            key in body for key in ("texts", "images", "inputs")
        ):
            raise ValueError("Embed request requires texts, images, or inputs")
    elif product_id == "rerank":
        if operation.strip().lower() == "rerank":
            if not isinstance(body.get("query"), str) or not body["query"].strip():
                raise ValueError("Rerank request requires a non-empty query")
            if not isinstance(body.get("documents"), list) or not body["documents"]:
                raise ValueError("Rerank request requires a non-empty documents list")
