"""CORE capability catalog for Bada Business programs.

This file describes CORE capabilities only. Program names and facts are
loaded from the canonical BADA BUSINESS resource catalog. Provider URLs and
resource records remain owned by the Global Bada Business Ecosystem.
"""

ECOSYSTEM_ID = "BADA-BUSINESS-CORE-PROGRAMS"
ECOSYSTEM_NAME = "BADA BUSINESS CORE PROGRAMS"
LAYER = "CORE"
PARENT_ECOSYSTEM_ID = "BADA-BUSINESS-CORE-ECOSYSTEM"

CANONICAL_ECOSYSTEM_ROOT = "backend.global_ecosystem.global_bada_business_ecosystem"
CANONICAL_RESOURCE_MODULE = "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog"
CANONICAL_LINKS_MODULE = "backend.global_ecosystem.global_bada_business_ecosystem.links.platform_links"
CANONICAL_COURSE_LINK_DIRECTORY = "backend/global_ecosystem/global_bada_business_ecosystem/course_resources/BADA_BUSINESS_COMMUNITY_COURSE_LINKS.md"
CANONICAL_PROGRAM_IDS = ("lfp_digital", "bb_impact", "idea_to_ipo")

CAPABILITIES = (
    "PROGRAM_DISCOVERY",
    "PROGRAM_LOOKUP",
    "PROGRAM_COMPARISON",
    "ENROLLMENT_REQUEST_VALIDATION",
    "PROGRAM_WORKFLOW_COORDINATION",
)

IMPLEMENTATION_STATUS = "CORE_DOMAIN_SCAFFOLD"
LIVE_REGISTRATION_ENABLED = False
PAYMENT_PROCESSING_ENABLED = False
