"""Adapter manager for the Global Android Ecosystem."""

from backend.foundation.core.ecosystem_adapter import FoundationEcosystemAdapter


class GlobalAndroidEcosystemManager(FoundationEcosystemAdapter):
    NAME = "GLOBAL_ANDROID_ECOSYSTEM"
    COMPONENT_KEY = "android"


__all__ = ["GlobalAndroidEcosystemManager"]
