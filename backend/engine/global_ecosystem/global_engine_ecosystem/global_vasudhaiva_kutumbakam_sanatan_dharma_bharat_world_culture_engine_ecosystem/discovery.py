"""Deterministic, dependency-free discovery helpers for cultural records."""
from __future__ import annotations
import re
from typing import Any

def normalize_query(query: str) -> str:
    return " ".join(re.findall(r"[\w-]+", str(query or "").casefold(), flags=re.UNICODE))

def rank_records(records: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    terms = set(normalize_query(query).split())
    ranked = []
    for record in records:
        title = normalize_query(str(record.get("title", "")))
        content = normalize_query(str(record.get("content", "")))
        title_terms, content_terms = set(title.split()), set(content.split())
        score = 5 * len(terms & title_terms) + len(terms & content_terms)
        if score:
            ranked.append((score, record))
    ranked.sort(key=lambda item: (-item[0], str(item[1].get("record_id", ""))))
    return [{"score": score, **record} for score, record in ranked]
