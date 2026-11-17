"""Typed request contract for Cohere Rerank."""
from dataclasses import dataclass


@dataclass(frozen=True)
class RerankRequest:
    query: str
    documents: tuple[str, ...]
    top_n: int | None = None


def validate_request(request: RerankRequest) -> bool:
    if not isinstance(request, RerankRequest):
        raise TypeError("request must be RerankRequest")
    if not isinstance(request.query, str) or not request.query.strip():
        raise ValueError("query must be a non-empty string")
    if isinstance(request.documents, (str, bytes)) or not isinstance(request.documents, (tuple, list)):
        raise ValueError("documents must be a sequence of non-empty strings")
    if not request.documents or any(not isinstance(item, str) or not item.strip() for item in request.documents):
        raise ValueError("documents must contain non-empty strings")
    if request.top_n is not None and (isinstance(request.top_n, bool) or not isinstance(request.top_n, int) or request.top_n < 1):
        raise ValueError("top_n must be a positive integer")
    return True
