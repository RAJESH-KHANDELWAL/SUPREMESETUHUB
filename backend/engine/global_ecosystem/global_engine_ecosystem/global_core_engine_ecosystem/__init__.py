"""Public exports for GLOBAL CORE ENGINE ECOSYSTEM."""
from .manager import (
    ROOT,
    ROOT_ID,
    EcosystemManager,
    GlobalCoreEngineEcosystemManager,
    get_catalog,
)

LAYER = "ENGINE"
ECOSYSTEM_ID = ROOT_ID
ECOSYSTEM_NAME = "GLOBAL CORE ENGINE ECOSYSTEM"

__all__ = [
    "LAYER",
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "ROOT",
    "ROOT_ID",
    "get_catalog",
    "GlobalCoreEngineEcosystemManager",
    "EcosystemManager",
]
