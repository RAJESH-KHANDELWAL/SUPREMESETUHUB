"""Adapter manager for Global Security Ecosystem."""

from backend.foundation.core.ecosystem_adapter import FoundationEcosystemAdapter


class GlobalSecurityEcosystemManager(FoundationEcosystemAdapter):
    NAME = "GLOBAL_SECURITY_ECOSYSTEM"
    COMPONENT_KEY = "security"


__all__ = ["GlobalSecurityEcosystemManager"]
