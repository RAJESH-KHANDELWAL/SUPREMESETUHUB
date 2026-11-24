"""Typed request contract for Cohere Embed."""
from dataclasses import dataclass


@dataclass(frozen=True)
class EmbedRequest:
    texts: tuple[str, ...]
    model: str | None = None
    input_type: str | None = None


def validate_request(request: EmbedRequest) -> bool:
    if not isinstance(request, EmbedRequest):
        raise TypeError("request must be EmbedRequest")
    if isinstance(request.texts, (str, bytes)) or not isinstance(request.texts, (tuple, list)):
        raise ValueError("texts must be a sequence of non-empty strings")
    if not request.texts or any(not isinstance(item, str) or not item.strip() for item in request.texts):
        raise ValueError("texts must contain non-empty strings")
    if request.model is not None and (not isinstance(request.model, str) or not request.model.strip()):
        raise ValueError("model must be a non-empty string when supplied")
    if request.input_type is not None and (not isinstance(request.input_type, str) or not request.input_type.strip()):
        raise ValueError("input_type must be a non-empty string when supplied")
    return True
