"""Shared contract for provider-specific data ecosystem adapters."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ProviderDataEcosystem(ABC):
    """Base contract; concrete adapters must use official authorized APIs."""

    provider_id: str
    display_name: str
    capabilities: tuple[str, ...] = ()

    @abstractmethod
    def describe(self) -> dict[str, Any]:
        """Return safe capability metadata; never return credentials or tokens."""
        raise NotImplementedError
