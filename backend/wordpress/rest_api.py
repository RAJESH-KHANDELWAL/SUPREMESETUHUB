"""Client for the REAL, already-installed WordPress sites.

WordPress core/PHP runs on its own WordPress host. This backend talks to that
installation over its authenticated WordPress REST API; it does not pretend
that a site registry is a live connection and it never stores credentials in Git.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import httpx


@dataclass(frozen=True)
class WordPressRestConfig:
    site_id: str
    base_url: str
    username: str
    application_password: str

    @classmethod
    def from_environment(cls, site_id: str) -> "WordPressRestConfig":
        prefixes = {
            "rajeshkhandelwalofficial": "WORDPRESS",
            "drrajeshkhandelwalibc": "WORDPRESS_IBC",
        }
        prefix = prefixes.get(site_id)
        if prefix is None:
            raise ValueError("WORDPRESS_SITE_NOT_REGISTERED")

        base_url = os.getenv(f"{prefix}_SITE_URL", "").strip().rstrip("/")
        username = os.getenv(f"{prefix}_USERNAME", "").strip()
        password = os.getenv(f"{prefix}_APPLICATION_PASSWORD", "").strip()

        missing = [
            key for key, value in (
                (f"{prefix}_SITE_URL", base_url),
                (f"{prefix}_USERNAME", username),
                (f"{prefix}_APPLICATION_PASSWORD", password),
            ) if not value
        ]
        if missing:
            raise RuntimeError("Missing private backend environment variables: " + ", ".join(missing))

        if not base_url.startswith("https://"):
            raise RuntimeError(f"{prefix}_SITE_URL must use HTTPS")

        return cls(site_id, base_url, username, password)


class WordPressRestClient:
    """Authenticated client for the existing live WordPress REST API."""

    def __init__(self, config: WordPressRestConfig) -> None:
        self.config = config

    def _get(self, endpoint: str, params: dict[str, Any] | None = None) -> Any:
        url = f"{self.config.base_url}/wp-json/wp/v2/{endpoint.lstrip('/')}"
        try:
            response = httpx.get(
                url,
                params=params,
                auth=(self.config.username, self.config.application_password),
                timeout=20.0,
                follow_redirects=True,
                headers={"Accept": "application/json", "User-Agent": "SUPREMESETUHUB-WordPress-Bridge/1.0"},
            )
        except httpx.HTTPError as exc:
            raise RuntimeError("Could not reach the live WordPress REST API") from exc

        if response.status_code in (401, 403):
            raise PermissionError("WordPress rejected the credentials or REST API permission")
        if response.status_code == 404:
            raise RuntimeError("WordPress REST API endpoint not found; check the site URL and REST API availability")
        if response.status_code >= 400:
            raise RuntimeError(f"WordPress REST API returned HTTP {response.status_code}")

        try:
            return response.json()
        except ValueError as exc:
            raise RuntimeError("WordPress REST API did not return JSON") from exc

    def health(self) -> dict[str, Any]:
        data = self._get("users/me", {"context": "edit"})
        return {
            "success": True,
            "status": "CONNECTED",
            "site_id": self.config.site_id,
            "site_url": self.config.base_url,
            "authenticated_user": data.get("slug") or data.get("name"),
            "wordpress_rest_api": "reachable",
        }

    def list_posts(self, per_page: int = 10) -> list[dict[str, Any]]:
        return self._get("posts", {"per_page": max(1, min(per_page, 100)), "context": "edit"})

    def list_pages(self, per_page: int = 10) -> list[dict[str, Any]]:
        return self._get("pages", {"per_page": max(1, min(per_page, 100)), "context": "edit"})

    def list_plugins(self) -> list[dict[str, Any]]:
        # Requires an authenticated WordPress user with plugin-management capability.
        return self._get("plugins", {"context": "edit"})
