"""Backward-compatible imports for the GLOBAL CORE ECOSYSTEM registry."""
from backend.core.global_ecosystem.global_core_ecosystem.registry import (
    EcosystemRegistry, GlobalEcosystemRegistry, utc_now,
)

__all__ = ["EcosystemRegistry", "GlobalEcosystemRegistry", "utc_now"]
