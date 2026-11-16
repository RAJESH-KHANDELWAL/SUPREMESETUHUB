"""Cohere embedding capability CORE contract."""
from dataclasses import dataclass
@dataclass(frozen=True)
class EmbedRequest:
    texts: tuple[str, ...]
    model: str | None = None
    input_type: str | None = None
def validate_request(request):
    if not request.texts or any(not isinstance(item, str) or not item.strip() for item in request.texts):
        raise ValueError("texts must contain non-empty strings")
    return True
