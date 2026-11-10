"""Global AI ecosystem namespace.

The canonical AI implementation remains in backend.ai. This package exposes
that implementation through the global ecosystem namespace without duplicating
provider execution, CORE contracts, ENGINE orchestration, or data-layer logic.
"""
from backend.ai.global_ecosystem.global_ai_ecosystem import (
    ECOSYSTEM_ID,
    LAYER,
    GlobalAIEcosystemService,
    get_catalog,
    get_provider,
    list_providers,
)
from .scope import (
    AI_MATURITY_LEVELS,
    AI_SCOPE_DOMAINS,
    get_scope_catalog,
)

__all__ = [
    "ECOSYSTEM_ID",
    "LAYER",
    "GlobalAIEcosystemService",
    "get_catalog",
    "get_provider",
    "list_providers",
    "AI_MATURITY_LEVELS",
    "AI_SCOPE_DOMAINS",
    "get_scope_catalog",
]
