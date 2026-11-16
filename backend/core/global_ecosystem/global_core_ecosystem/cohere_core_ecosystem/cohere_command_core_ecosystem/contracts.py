"""Typed request contract for Cohere Command generation."""
from dataclasses import dataclass
from collections.abc import Mapping


@dataclass(frozen=True)
class CommandRequest:
    message: str
    model: str | None = None
    chat_history: tuple[dict, ...] = ()


def validate_request(request: CommandRequest) -> bool:
    if not isinstance(request, CommandRequest):
        raise TypeError("request must be CommandRequest")
    if not isinstance(request.message, str) or not request.message.strip():
        raise ValueError("message must be a non-empty string")
    if not isinstance(request.chat_history, (tuple, list)) or any(not isinstance(item, Mapping) for item in request.chat_history):
        raise ValueError("chat_history must be a sequence of mappings")
    if request.model is not None and (not isinstance(request.model, str) or not request.model.strip()):
        raise ValueError("model must be a non-empty string when supplied")
    return True
