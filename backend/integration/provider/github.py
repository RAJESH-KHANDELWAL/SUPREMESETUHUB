"""Authenticated GitHub REST API provider.

Uses a server-side GitHub token from GITHUB_TOKEN (or GH_TOKEN). Never logs
or returns the token. The health check reports configuration only; API routes
perform live validation when called.
"""
from __future__ import annotations

import os
from typing import Any, Dict

import httpx

from ..base import IntegrationProvider
from .readiness import provider_health


class GitHubProvider(IntegrationProvider):
    """GitHub REST API provider with token-backed requests."""

    name = "GITHUB"
    category = "DEVELOPER"

    BASE_URL = "https://api.github.com"
    API_VERSION = "2022-11-28"

    @staticmethod
    def token() -> str:
        return (
            os.getenv("GITHUB_TOKEN", "").strip()
            or os.getenv("GH_TOKEN", "").strip()
        )

    def metadata(self) -> Dict[str, Any]:
        return {
            **super().metadata(),
            "api_base_url": self.BASE_URL,
            "api_version": self.API_VERSION,
            "auth_method": "GitHub fine-grained PAT or GitHub App installation token",
            "required_configuration": ["GITHUB_TOKEN (or GH_TOKEN)"],
            "setup_guide": (
                "backend/api/global_ecosystem/global_api_ecosystem/"
                "github_api_ecosystem/README.md"
            ),
            "api_families": [
                "REST", "GRAPHQL", "REPOSITORIES", "ISSUES",
                "PULL_REQUESTS", "ACTIONS", "APPS", "AUTHENTICATION",
                "WEBHOOKS", "CHECKS", "SECURITY", "ORGANIZATIONS",
            ],
            "live_connection_verified": False,
        }

    def health(self) -> Dict[str, Any]:
        return provider_health(
            provider=self.name,
            category=self.category,
            configured=bool(self.token()),
            auth_method="GitHub Bearer token",
            required_configuration=["GITHUB_TOKEN (or GH_TOKEN)"],
            capabilities=[
                "REST", "GRAPHQL", "REPOSITORIES", "ISSUES",
                "PULL_REQUESTS", "ACTIONS", "APPS", "WEBHOOKS",
                "CHECKS", "SECURITY", "ORGANIZATIONS",
            ],
        )

    def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        token = self.token()
        if not token:
            raise RuntimeError("GITHUB_TOKEN_NOT_CONFIGURED")

        if not endpoint.startswith("/") or endpoint.startswith("//"):
            raise ValueError("GitHub endpoint must be a relative API path")

        response = httpx.request(
            method=method.upper(),
            url=f"{self.BASE_URL}{endpoint}",
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": self.API_VERSION,
            },
            params=params,
            json=json,
            timeout=15.0,
        )
        if response.status_code >= 400:
            raise httpx.HTTPStatusError(
                f"GitHub API returned HTTP {response.status_code}",
                request=response.request,
                response=response,
            )
        if response.status_code == 204:
            return {"success": True}
        payload = response.json()
        return payload if isinstance(payload, dict) else {"items": payload}
