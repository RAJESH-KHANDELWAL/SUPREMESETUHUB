"""Controlled organization taxonomy; classifications are not legal verification."""
from .organization_domain_api_ecosystems.registry import ORGANIZATION_DOMAINS
from .organization_type_api_ecosystems.registry import ORGANIZATION_TYPES, ORGANIZATION_TYPE_GROUPS

VERIFICATION_STATES = ["unverified", "source_checked", "identity_verified", "registry_verified", "suspended"]
LEGAL_FORM_DIMENSIONS = ["statutory_body", "nonprofit_legal_entity", "company_or_corporate_body", "cooperative_or_mutual", "trust_or_foundation", "association_or_society", "public_authority", "informal_or_unincorporated", "other", "unknown"]
GOVERNANCE_MODELS = ["public_governance", "member_governed", "board_governed", "trustee_governed", "community_governed", "owner_governed", "intergovernmental", "mixed", "unknown"]
GEOGRAPHIC_SCOPES = ["local", "regional", "national", "multinational", "international", "global", "unknown"]
