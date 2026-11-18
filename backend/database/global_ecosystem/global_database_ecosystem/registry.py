"""Central registry for provider data ecosystems; no live connection is implied."""

from __future__ import annotations

from typing import Type

from .provider_base import ProviderDataEcosystem
from .google_database_ecosystem import GoogleDatabaseEcosystem
from .aws_database_ecosystem import AWSDatabaseEcosystem
from .microsoft_database_ecosystem import MicrosoftDatabaseEcosystem
from .proton_database_ecosystem import ProtonDatabaseEcosystem
from .mega_database_ecosystem import MegaDatabaseEcosystem


class GlobalDatabaseEcosystemRegistry:
    """Discover supported provider adapters without opening network connections."""

    _providers: dict[str, Type[ProviderDataEcosystem]] = {
        cls.provider_id: cls
        for cls in (
            GoogleDatabaseEcosystem,
            AWSDatabaseEcosystem,
            MicrosoftDatabaseEcosystem,
            ProtonDatabaseEcosystem,
            MegaDatabaseEcosystem,
        )
    }

    @classmethod
    def list_providers(cls) -> list[dict[str, object]]:
        return [cls._providers[key]().describe() for key in sorted(cls._providers)]

    @classmethod
    def get_provider(cls, provider_id: str) -> ProviderDataEcosystem:
        """Return an adapter by stable ID; raise KeyError for unknown providers."""
        try:
            provider_type = cls._providers[provider_id.strip().lower()]
        except (AttributeError, KeyError) as exc:
            raise KeyError(f"Unknown provider ecosystem: {provider_id!r}") from exc
        return provider_type()
