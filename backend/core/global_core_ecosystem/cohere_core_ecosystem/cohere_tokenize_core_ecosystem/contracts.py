"""Typed request contract for Cohere Tokenize."""
from dataclasses import dataclass


@dataclass(frozen=True)
class TokenizeRequest:
    text: str
    model: str | None = None


def validate_request(request: TokenizeRequest) -> bool:
    if not isinstance(request, TokenizeRequest):
        raise TypeError("request must be TokenizeRequest")
    if not isinstance(request.text, str) or not request.text.strip():
        raise ValueError("text must be a non-empty string")
    if request.model is not None and (not isinstance(request.model, str) or not request.model.strip()):
        raise ValueError("model must be a non-empty string when supplied")
    return True
