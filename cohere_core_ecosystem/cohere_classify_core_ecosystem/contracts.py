"""Typed request contract for Cohere classification."""
from dataclasses import dataclass
from collections.abc import Mapping


@dataclass(frozen=True)
class ClassifyRequest:
    inputs: tuple[str, ...]
    model: str | None = None
    examples: tuple[dict, ...] = ()


def validate_request(request: ClassifyRequest) -> bool:
    if not isinstance(request, ClassifyRequest):
        raise TypeError("request must be ClassifyRequest")
    if isinstance(request.inputs, (str, bytes)) or not isinstance(request.inputs, (tuple, list)):
        raise ValueError("classify inputs must be a sequence of non-empty strings")
    if not request.inputs or any(not isinstance(item, str) or not item.strip() for item in request.inputs):
        raise ValueError("classify inputs must contain non-empty strings")
    if not isinstance(request.examples, (tuple, list)) or any(not isinstance(item, Mapping) for item in request.examples):
        raise ValueError("classify examples must be a sequence of mappings")
    if request.model is not None and (not isinstance(request.model, str) or not request.model.strip()):
        raise ValueError("model must be a non-empty string when supplied")
    return True
