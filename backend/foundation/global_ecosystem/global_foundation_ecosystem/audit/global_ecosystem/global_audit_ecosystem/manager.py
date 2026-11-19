"""Adapter manager for Global Audit Ecosystem."""

from backend.foundation.core.ecosystem_adapter import FoundationEcosystemAdapter


class GlobalAuditEcosystemManager(FoundationEcosystemAdapter):
    NAME = "GLOBAL_AUDIT_ECOSYSTEM"
    COMPONENT_KEY = "audit"


__all__ = ["GlobalAuditEcosystemManager"]
