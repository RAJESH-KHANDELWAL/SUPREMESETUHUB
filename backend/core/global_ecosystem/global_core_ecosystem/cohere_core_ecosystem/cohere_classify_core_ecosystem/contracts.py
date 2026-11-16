"""Cohere classification capability CORE contract."""
from dataclasses import dataclass
@dataclass(frozen=True)
class ClassifyRequest:
    inputs: tuple[str, ...]
    model: str | None = None
    examples: tuple[dict, ...] = ()
def validate_request(request):
    if not request.inputs or any(not isinstance(item, str) or not item.strip() for item in request.inputs):
        raise ValueError("classify inputs must contain non-empty strings")
    return True
