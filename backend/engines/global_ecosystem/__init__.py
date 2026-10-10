
"""GLOBAL ECOSYSTEM engine package."""

from .models import GlobalEcosystemIdentity
from .registry import (
    GLOBAL_ECOSYSTEM_ID,
    GLOBAL_ECOSYSTEM_NAME,
    GlobalEcosystemRegistry,
)
from .manager import GlobalEcosystemManager

# Backward compatibility for existing integrations.
EcosystemIdentity = GlobalEcosystemIdentity
EcosystemRegistry = GlobalEcosystemRegistry
EcosystemManager = GlobalEcosystemManager

__all__ = [
    "GLOBAL_ECOSYSTEM_ID",
    "GLOBAL_ECOSYSTEM_NAME",
    "GlobalEcosystemIdentity",
    "GlobalEcosystemRegistry",
    "GlobalEcosystemManager",
    "EcosystemIdentity",
    "EcosystemRegistry",
    "EcosystemManager",
]
