"""Global payee verification provider contract and registry.

Country/network support is adapter-driven. A method listed as planned is not
live until a vetted provider adapter is configured and its response is verified.
No credentials or real bank details belong in source control.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True)
class PayeeVerificationResult:
    status: str
    verified: bool
    account_holder_name: str | None
    country_code: str | None
    network: str
    provider_reference: str | None = None
    message: str = ""


class PayeeVerificationProvider(Protocol):
    """Adapter contract implemented by an authorized provider integration."""

    provider_id: str
    supported_countries: set[str]
    supported_methods: set[str]

    def verify_payee(self, *, country_code: str, payment_method: str,
                     details: dict[str, Any]) -> PayeeVerificationResult:
        """Return a provider-authenticated result; raise on provider errors."""
        ...


# Deliberately empty until provider contracts, credentials, compliance and
# sandbox tests are complete. Never interpret registry absence as verification.
_PROVIDER_REGISTRY: list[PayeeVerificationProvider] = []


def register_provider(provider: PayeeVerificationProvider) -> None:
    """Register an adapter at application startup after secure configuration."""
    if any(p.provider_id == provider.provider_id for p in _PROVIDER_REGISTRY):
        raise ValueError("DUPLICATE_PAYMENT_PROVIDER_ID")
    _PROVIDER_REGISTRY.append(provider)


def configured_providers() -> list[dict[str, Any]]:
    return [
        {
            "provider_id": provider.provider_id,
            "supported_countries": sorted(provider.supported_countries),
            "supported_methods": sorted(provider.supported_methods),
        }
        for provider in _PROVIDER_REGISTRY
    ]


def find_provider(*, country_code: str, payment_method: str) -> PayeeVerificationProvider | None:
    country = country_code.strip().upper()
    method = payment_method.strip().upper()
    for provider in _PROVIDER_REGISTRY:
        if country in provider.supported_countries and method in provider.supported_methods:
            return provider
    return None
