"""Bada Business-specific configuration capability metadata.

Canonical Bada Business platform resources remain in backend.global_ecosystem.global_bada_business_ecosystem.
This catalog contains configuration capabilities only, not provider URLs or referrals.
"""

BADA_BUSINESS_CONFIG_CAPABILITIES = {
    "feature_control": "Enable or disable Bada Business integrations explicitly.",
    "resource_catalog_reference": "Identify the canonical Bada Business resource catalog module.",
    "approval_policy": "Configure approval requirements for sensitive workflows.",
    "request_limits": "Configure bounded request timeout and operational limits.",
    "localization": "Configure default locale for Bada Business workflows.",
    "environment_isolation": "Keep development, testing, and production settings separated.",
}


def get_bada_business_config_catalog():
    return {"name": "BADA BUSINESS CONFIG ECOSYSTEM", "namespace": "bada_business", "version": "1.0", "capabilities": dict(BADA_BUSINESS_CONFIG_CAPABILITIES)}
