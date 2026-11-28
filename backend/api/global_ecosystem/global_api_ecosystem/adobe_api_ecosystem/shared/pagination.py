"""Pagination helper driven by provider-specific extractors; no cursor format is assumed."""
from __future__ import annotations
from collections.abc import Callable, Iterator
from typing import Any, TypeVar
T = TypeVar("T")

def iter_pages(fetch_page: Callable[[str | None], T], next_cursor: Callable[[T], str | None], *, max_pages: int = 100) -> Iterator[T]:
    if max_pages < 1:
        raise ValueError("max_pages must be positive")
    cursor: str | None = None
    for _ in range(max_pages):
        page = fetch_page(cursor)
        yield page
        cursor = next_cursor(page)
        if cursor is None:
            return
    raise RuntimeError("Pagination safety limit reached")
