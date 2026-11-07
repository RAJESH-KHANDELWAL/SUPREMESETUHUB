"""Backward-compatible ENGINE identity model, backed by CORE."""
from backend.core.global_ecosystem.global_core_ecosystem.models import (
    GlobalEcosystemIdentity as EcosystemIdentity,
)

GlobalEcosystemIdentity = EcosystemIdentity

__all__ = ["EcosystemIdentity", "GlobalEcosystemIdentity"]
