"""People, Work, and Business Global Engine Ecosystem package."""
from .manager import EcosystemIdentity, ROOT, ROOT_ID, SUPPORTED_DOMAINS
from .registry import EcosystemRegistry, GlobalEcosystemRegistry

__all__ = [
    "EcosystemIdentity",
    "ROOT",
    "ROOT_ID",
    "SUPPORTED_DOMAINS",
    "EcosystemRegistry",
    "GlobalEcosystemRegistry",
]
