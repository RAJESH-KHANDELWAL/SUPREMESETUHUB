"""CORE capability catalog for Bada Business programs.

This file describes CORE capabilities only. Program names and facts are
loaded from the canonical BADA BUSINESS resource catalog.
"""

ECOSYSTEM_ID = "BADA-BUSINESS-CORE-PROGRAMS"
ECOSYSTEM_NAME = "BADA BUSINESS CORE PROGRAMS"
LAYER = "CORE"
PARENT_ECOSYSTEM_ID = "BADA-BUSINESS-CORE-ECOSYSTEM"

CAPABILITIES = (
    "PROGRAM_DISCOVERY",
    "PROGRAM_LOOKUP",
    "PROGRAM_COMPARISON",
    "ENROLLMENT_REQUEST_VALIDATION",
    "PROGRAM_WORKFLOW_COORDINATION",
)

CANONICAL_RESOURCE_MODULE = "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog"
CANONICAL_PROGRAM_IDS = ("lfp_digital", "bb_impact", "idea_to_ipo")
IMPLEMENTATION_STATUS = "CORE_DOMAIN_SCAFFOLD"
LIVE_REGISTRATION_ENABLED = False
PAYMENT_PROCESSING_ENABLED = False
