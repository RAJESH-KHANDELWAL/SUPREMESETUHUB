"""Deterministic search and ranking for the cultural capability catalogue."""
from __future__ import annotations
import re
from typing import Any
def normalize_query(value: str) -> str:
    return " ".join(re.findall(r"[\w-]+", str(value or "").casefold(), flags=re.UNICODE))
def search_catalogue(items: list[dict[str, Any]], query: str, domain: str | None = None) -> list[dict[str, Any]]:
    needle=normalize_query(query)
    if not needle: raise ValueError("SEARCH_QUERY_REQUIRED")
    terms=set(needle.split()); ranked=[]
    for item in items:
        if domain and item.get("domain") != domain.upper(): continue
        haystack=normalize_query(" ".join([str(item.get("name","")),str(item.get("description",""))," ".join(item.get("keywords",[]))," ".join(item.get("work_types",[]))," ".join(item.get("business_types",[]))]))
        title_terms=set(normalize_query(str(item.get("name",""))).split())
        score=4*len(terms & title_terms)+len(terms & set(haystack.split()))
        if score: ranked.append((score,item))
    ranked.sort(key=lambda row:(-row[0],row[1]["id"]))
    return [{"score":score,**item} for score,item in ranked]
