"""Canonical manager for the GitHub Core Ecosystem.

This is a metadata-only control plane. Authentication and GitHub API transport
remain in backend/integration and backend/api.
"""
from __future__ import annotations

from typing import Any

from .orchestrator import GitHubCoreOrchestrator
from .service import GitHubCoreEcosystemService


class GitHubCoreManager:
    """Stable application entry point for GitHub Core metadata."""

    NAME = "GITHUB CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GITHUB-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = GitHubCoreOrchestrator()
        self._service = GitHubCoreEcosystemService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_families(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_families(enabled_only=enabled_only)

    def get_family(self, family: str) -> dict[str, Any] | None:
        return self._orchestrator.get_family(family)

    def list_offerings(self) -> dict[str, Any]:
        return self._orchestrator.offerings()

    def get_offering(self, family: str) -> dict[str, Any] | None:
        return self._orchestrator.get_offering(family)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()


def get_manager() -> GitHubCoreManager:
    """Return a fresh canonical manager, matching Google Core's public API."""
    return GitHubCoreManager()


__all__ = ["GitHubCoreManager", "get_manager"]
