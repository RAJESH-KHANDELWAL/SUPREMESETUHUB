"""Global AI ecosystem namespace.

Provider-specific packages live beside this module. Canonical execution,
CORE contracts, ENGINE orchestration, and persistence remain in their
respective backend layers; this namespace provides discovery and routing metadata.
"""
from backend.ai.global_ecosystem.global_ai_ecosystem import (
    ECOSYSTEM_ID,
    LAYER,
    GlobalAIEcosystemService,
    get_catalog,
    get_provider,
    list_providers,
)
from .providers import get_ai_provider, list_ai_providers, validate_provider_registry
from .capabilities import list_ai_capability_groups, list_ai_modalities
from .governance import evaluate_use_context, get_policy_catalog
from .scope import (
    AI_MATURITY_LEVELS,
    AI_SCOPE_DOMAINS,
    get_domain,
    get_scope_catalog,
    list_domain_ids,
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
    "get_domain",
    "list_domain_ids",
    "get_ai_provider",
    "list_ai_providers",
    "validate_provider_registry",
    "list_ai_modalities",
    "list_ai_capability_groups",
    "evaluate_use_context",
    "get_policy_catalog",
]
