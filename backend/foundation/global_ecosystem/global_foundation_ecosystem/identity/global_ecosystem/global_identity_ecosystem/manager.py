"""Adapter manager for Global Identity Ecosystem."""

from backend.foundation.core.ecosystem_adapter import FoundationEcosystemAdapter


class GlobalIdentityEcosystemManager(FoundationEcosystemAdapter):
    NAME = "GLOBAL_IDENTITY_ECOSYSTEM"
    COMPONENT_KEY = "identity"


__all__ = ["GlobalIdentityEcosystemManager"]
