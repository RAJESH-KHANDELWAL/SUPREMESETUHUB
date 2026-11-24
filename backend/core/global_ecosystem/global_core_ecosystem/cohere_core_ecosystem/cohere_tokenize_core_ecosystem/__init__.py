"""Cohere tokenization capability CORE contract."""
from dataclasses import dataclass
@dataclass(frozen=True)
class TokenizeRequest:
    text: str
    model: str | None = None
def validate_request(request):
    if not request.text.strip():
        raise ValueError("text must be non-empty")
    return True

