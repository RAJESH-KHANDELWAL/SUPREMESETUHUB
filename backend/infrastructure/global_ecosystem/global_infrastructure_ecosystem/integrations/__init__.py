"""Registered cross-layer integration adapters for Global Infrastructure.

This registry describes importable adapter packages only. It does not claim
that external infrastructure services or credentials are live/connected.
"""
from __future__ import annotations

from ..schemas import CatalogRecord

INTEGRATIONS: tuple[CatalogRecord, ...] = (
    CatalogRecord(
        id="core_foundation",
        name="CORE Foundation",
        category="core_foundation",
        description="Adapter to the canonical backend.core foundation package.",
        status="FOUNDATION_LINKED",
        metadata={
            "package": "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.integrations.core",
            "canonical_package": "backend.core",
            "live_external_connection": False,
        },
    ),
    CatalogRecord(
        id="global_core_ecosystem",
        name="Global CORE Ecosystem",
        category="global_core",
        description="Adapter to the canonical Global CORE Ecosystem hierarchy and infrastructure CORE contracts.",
        status="FOUNDATION_LINKED",
        metadata={
            "package": "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.integrations.global_core_ecosystem",
            "canonical_package": "backend.core.global_ecosystem.global_core_ecosystem",
            "live_external_connection": False,
        },
    ),
)

__all__ = ["INTEGRATIONS"]
