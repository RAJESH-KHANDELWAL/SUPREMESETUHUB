"""Public-source research engine for freelance work and business opportunities.

This module searches public web indexes through configured official APIs. It does
not scrape login-gated sites, bypass access controls, harvest private contact
details, or claim that a listing/person is verified merely because it appears in
search results.
"""
from __future__ import annotations

import os
import re
from typing import Any
from urllib.parse import urlparse

import httpx


BRAVE_ENDPOINT = "https://api.search.brave.com/res/v1/web/search"
GOOGLE_CSE_ENDPOINT = "https://www.googleapis.com/customsearch/v1"

CATEGORIES: dict[str, tuple[str, ...]] = {
    "freelance_work": (
        "freelance writing translation retyping copywriting remote paid project",
        "freelance jobs content writing translation virtual assistant remote",
    ),
    "clients": (
        "looking for freelancer hire freelance writer translator developer",
        "business seeking freelance services remote contractor",
    ),
    "business": (
        "small business digital services vendor partnership project opportunity",
        "business opportunities independent consultant service provider",
    ),
    "research": (
        "official freelance opportunity contract request for proposal",
        "remote contract project open call freelancer",
    ),
}
MARKETS = {
    "bharat": ("India", "IN"),
    "global": ("global", ""),
}


def _clean(value: Any, max_length: int = 1200) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text[:max_length]


def _host(url: str) -> str:
    try:
        return (urlparse(url).hostname or "").lower().removeprefix("www.")
    except ValueError:
        return ""


def _safe_http_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        return parsed.scheme in {"http", "https"} and bool(parsed.hostname)
    except ValueError:
        return False


def _relevance_score(title: str, description: str, query: str) -> int:
    """A transparent keyword relevance heuristic, not a truth or fraud verdict."""
    text = f"{title} {description}".casefold()
    terms = {term.casefold() for term in re.findall(r"[a-zA-Z0-9+#.-]{3,}", query)}
    if not terms:
        return 0
    matched = sum(1 for term in terms if term in text)
    return min(100, round(100 * matched / len(terms)))


class FreelancerResearchEngine:
    """Search configured public web indexes and normalize source-backed results."""

    def __init__(self, timeout_seconds: float = 12.0) -> None:
        self.timeout_seconds = timeout_seconds

    def status(self) -> dict[str, Any]:
        brave_configured = bool(os.getenv("BRAVE_SEARCH_API_KEY", "").strip())
        google_configured = bool(
            os.getenv("GOOGLE_CSE_API_KEY", "").strip()
            and os.getenv("GOOGLE_CSE_CX", "").strip()
        )
        providers = [
            {
                "provider_id": "brave_search",
                "configured": brave_configured,
                "status": "READY" if brave_configured else "API_KEY_REQUIRED",
            },
            {
                "provider_id": "google_custom_search",
                "configured": google_configured,
                "status": "READY" if google_configured else "API_KEY_AND_ENGINE_ID_REQUIRED",
            },
        ]
        return {
            "success": True,
            "engine": "GLOBAL FREELANCER ECOSYSTEM RESEARCH ENGINE",
            "search_enabled": any(item["configured"] for item in providers),
            "providers": providers,
            "markets": ["bharat", "global"],
            "categories": list(CATEGORIES),
            "verification_policy": (
                "Search results are leads, not verified people, clients, jobs, or payment promises. "
                "Check the original source and employer/client before sharing information or doing work."
            ),
        }

    def search(
        self,
        query: str,
        market: str = "global",
        category: str = "freelance_work",
        limit: int = 10,
    ) -> dict[str, Any]:
        query = _clean(query, 220)
        market = market.strip().lower()
        category = category.strip().lower()
        limit = max(1, min(int(limit), 20))

        if len(query) < 2:
            raise ValueError("QUERY_TOO_SHORT")
        if market not in MARKETS:
            raise ValueError("MARKET_MUST_BE_BHARAT_OR_GLOBAL")
        if category not in CATEGORIES:
            raise ValueError("UNSUPPORTED_RESEARCH_CATEGORY")

        status = self.status()
        configured = [p["provider_id"] for p in status["providers"] if p["configured"]]
        if not configured:
            return {
                "success": False,
                "status": "SEARCH_PROVIDER_CONFIGURATION_REQUIRED",
                "query": query,
                "market": market,
                "category": category,
                "results": [],
                "provider_status": status["providers"],
                "required_configuration": [
                    "BRAVE_SEARCH_API_KEY",
                    "or GOOGLE_CSE_API_KEY and GOOGLE_CSE_CX",
                ],
            }

        region_name, country_code = MARKETS[market]
        queries = [f"{query} {template}" for template in CATEGORIES[category]]
        results: list[dict[str, Any]] = []
        errors: list[dict[str, str]] = []

        for provider_id in configured:
            for search_query in queries:
                try:
                    if provider_id == "brave_search":
                        found = self._search_brave(search_query, country_code, limit)
                    else:
                        found = self._search_google(search_query, country_code, limit)
                    results.extend(found)
                except (httpx.HTTPError, ValueError, KeyError) as exc:
                    errors.append({
                        "provider": provider_id,
                        "error": type(exc).__name__,
                    })

        deduped: dict[str, dict[str, Any]] = {}
        for item in results:
            url = item.get("url", "")
            if not _safe_http_url(url):
                continue
            key = url.split("#", 1)[0].rstrip("/").casefold()
            if not key:
                continue
            item["relevance_score"] = _relevance_score(
                item.get("title", ""), item.get("description", ""), query
            )
            item["verification_status"] = "UNVERIFIED_PUBLIC_LISTING"
            item["verification_checks"] = [
                "Open the original source",
                "Confirm the client/employer identity through an independent official channel",
                "Confirm scope, deadline, payment terms, and platform rules",
                "Never pay a registration fee to unlock a job or share OTPs/passwords",
            ]
            previous = deduped.get(key)
            if previous is None or item["relevance_score"] > previous["relevance_score"]:
                deduped[key] = item

        ranked = sorted(
            deduped.values(),
            key=lambda item: (item["relevance_score"], item["title"].casefold()),
            reverse=True,
        )[:limit]
        return {
            "success": True,
            "status": "RESULTS_FOUND" if ranked else (
                "PROVIDER_ERROR" if errors else "NO_PUBLIC_RESULTS"
            ),
            "query": query,
            "market": market,
            "market_label": region_name,
            "category": category,
            "count": len(ranked),
            "results": ranked,
            "provider_errors": errors,
            "data_note": (
                "Results come from configured public search APIs. They are not endorsements "
                "and do not prove that a person, client, vacancy, or payment is genuine."
            ),
        }

    def _search_brave(
        self, query: str, country_code: str, limit: int
    ) -> list[dict[str, Any]]:
        api_key = os.getenv("BRAVE_SEARCH_API_KEY", "").strip()
        if not api_key:
            return []
        params: dict[str, Any] = {"q": query, "count": limit}
        if country_code:
            params["country"] = country_code
        with httpx.Client(timeout=self.timeout_seconds) as client:
            response = client.get(
                BRAVE_ENDPOINT,
                params=params,
                headers={"X-Subscription-Token": api_key, "Accept": "application/json"},
            )
            response.raise_for_status()
            payload = response.json()
        rows = payload.get("web", {}).get("results", [])
        return [
            self._normalize(item, "brave_search")
            for item in rows if isinstance(item, dict)
        ]

    def _search_google(
        self, query: str, country_code: str, limit: int
    ) -> list[dict[str, Any]]:
        api_key = os.getenv("GOOGLE_CSE_API_KEY", "").strip()
        engine_id = os.getenv("GOOGLE_CSE_CX", "").strip()
        if not api_key or not engine_id:
            return []
        params: dict[str, Any] = {
            "key": api_key,
            "cx": engine_id,
            "q": query,
            "num": min(limit, 10),
        }
        if country_code:
            params["gl"] = country_code.lower()
        with httpx.Client(timeout=self.timeout_seconds) as client:
            response = client.get(GOOGLE_CSE_ENDPOINT, params=params)
            response.raise_for_status()
            payload = response.json()
        rows = payload.get("items", [])
        return [
            self._normalize(item, "google_custom_search")
            for item in rows if isinstance(item, dict)
        ]

    @staticmethod
    def _normalize(item: dict[str, Any], provider: str) -> dict[str, Any]:
        url = _clean(item.get("url") or item.get("link"), 2000)
        title = _clean(item.get("title") or item.get("htmlTitle"), 300)
        description = _clean(
            item.get("description") or item.get("snippet") or item.get("htmlSnippet"), 1200
        )
        return {
            "title": title,
            "url": url,
            "domain": _host(url),
            "description": description,
            "source_provider": provider,
        }
