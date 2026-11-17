"""Cross-layer integration adapters for Global Infrastructure.

The adapters in this package expose metadata and lazy loaders only. They do
not imply that external services are configured or actively connected.
"""
from __future__ import annotations

from ..schemas import CatalogRecord

INTEGRATIONS: tuple[CatalogRecord, ...] = (
    CatalogRecord(
        id="core_foundation",
        name="CORE Foundation Adapter",
        category="internal_core",
        description=(
            "Lazy adapter to the canonical backend CORE package; "
            "metadata only until explicitly invoked."
        ),
        status="FOUNDATION_LINKED",
        metadata={
            "module": "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.integrations.core",
            "canonical_path": "backend/core",
            "loader": "load_core",
        },
    ),
    CatalogRecord(
        id="global_core_ecosystem",
        name="Global CORE Ecosystem Adapter",
        category="internal_core",
        description=(
            "Lazy adapter to the canonical Global CORE ecosystem and its "
            "infrastructure CORE contracts."
        ),
        status="FOUNDATION_LINKED",
        metadata={
            "module": "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.integrations.global_core_ecosystem",
            "canonical_path": "backend/core/global_ecosystem/global_core_ecosystem",
            "loader": "load_global_core_ecosystem",
        },
    ),
)

__all__ = ["INTEGRATIONS"]
