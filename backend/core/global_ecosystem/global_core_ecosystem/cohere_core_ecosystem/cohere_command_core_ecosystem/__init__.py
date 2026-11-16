"""Cohere command/generation capability CORE contract."""
from dataclasses import dataclass
@dataclass(frozen=True)
class CommandRequest:
    message: str
    model: str | None = None
    chat_history: tuple[dict, ...] = ()
def validate_request(request):
    if not isinstance(request.message, str) or not request.message.strip():
        raise ValueError("message must be a non-empty string")
    return True

