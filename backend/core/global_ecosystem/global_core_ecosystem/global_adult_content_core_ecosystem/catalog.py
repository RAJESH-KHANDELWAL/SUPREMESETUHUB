"""Read-only catalog facade for Global Adult Content CORE."""

from __future__ import annotations

from copy import deepcopy

from .taxonomy import ORIENTATION_CATALOG, PARTICIPANT_CONFIGURATION_CATALOG

ECOSYSTEM_ID = "GLOBAL-ADULT-CONTENT-CORE-ECOSYSTEM"
CANONICAL_PATH = "backend/core/global_ecosystem/global_core_ecosystem/global_adult_content_core_ecosystem"

DOMAINS = (
    {"id": "ORIENTATION_LABELS", "folder": "orientation_labels", "status": "CATALOG_ONLY"},
    {"id": "PARTICIPANT_CONFIGURATION", "folder": "participant_configuration", "status": "CATALOG_ONLY"},
    {"id": "AGE_ASSURANCE_POLICY", "folder": "age_assurance_policy", "status": "POLICY_METADATA_ONLY"},
    {"id": "CONSENT_AND_RIGHTS", "folder": "consent_and_rights", "status": "POLICY_METADATA_ONLY"},
    {"id": "CONTENT_MODERATION", "folder": "content_moderation", "status": "POLICY_METADATA_ONLY"},
    {"id": "PRIVACY_AND_RETENTION", "folder": "privacy_and_retention", "status": "POLICY_METADATA_ONLY"},
    {"id": "JURISDICTION_COMPLIANCE", "folder": "jurisdiction_compliance", "status": "POLICY_METADATA_ONLY"},
    {"id": "REPORTING_AND_TAKEDOWN", "folder": "reporting_and_takedown", "status": "POLICY_METADATA_ONLY"},
)


def get_catalog() -> dict:
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "canonical_path": CANONICAL_PATH,
        "status": "CORE_CATALOG_ONLY",
        "domains": deepcopy(list(DOMAINS)),
        "orientation_labels": deepcopy(list(ORIENTATION_CATALOG)),
        "participant_configurations": deepcopy(list(PARTICIPANT_CONFIGURATION_CATALOG)),
        "orientation_inference_enabled": False,
        "media_execution_enabled": False,
    }
