"""Cohere reranking capability CORE contract."""
from dataclasses import dataclass
@dataclass(frozen=True)
class RerankRequest:
    query: str
    documents: tuple[str, ...]
    top_n: int | None = None
def validate_request(request):
    if not request.query.strip() or not request.documents:
        raise ValueError("query and at least one document are required")
    if request.top_n is not None and request.top_n < 1:
        raise ValueError("top_n must be positive")
    return True

