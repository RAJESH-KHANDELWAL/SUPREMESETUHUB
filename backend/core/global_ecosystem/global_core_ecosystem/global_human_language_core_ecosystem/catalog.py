"""Canonical read-only human-language domain and provider catalogs."""

from copy import deepcopy
import json
from pathlib import Path

from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, STATUS

_CATALOG_PATH = Path(__file__).with_name("catalog.json")
_CATALOG_DATA = json.loads(_CATALOG_PATH.read_text(encoding="utf-8"))

HUMAN_LANGUAGE_DOMAINS = tuple(
    {
        **item,
        "division": "HUMAN",
        "status": STATUS,
        "consent_required": bool(item.get("age_restricted", False)),
    }
    for item in _CATALOG_DATA["domains"]
)

HUMAN_LANGUAGE_PROVIDERS = (
    {"provider_id": "ALIBABA_LANGUAGE", "name": "ALIBABA LANGUAGE", "folder": "alibaba_language_core_ecosystem"},
    {"provider_id": "AWS_LANGUAGE", "name": "AWS LANGUAGE", "folder": "aws_language_core_ecosystem"},
    {"provider_id": "BAIDU_LANGUAGE", "name": "BAIDU LANGUAGE", "folder": "baidu_language_core_ecosystem"},
    {"provider_id": "DEEPL_LANGUAGE", "name": "DEEPL LANGUAGE", "folder": "deepl_language_core_ecystem"},
    {"provider_id": "GOOGLE_LANGUAGE", "name": "GOOGLE LANGUAGE", "folder": "google_language_core_ecosystem"},
    {"provider_id": "IBM_LANGUAGE", "name": "IBM LANGUAGE", "folder": "ibm_language_core_ecosystem"},
    {"provider_id": "MICROSOFT_LANGUAGE", "name": "MICROSOFT LANGUAGE", "folder": "microsoft_language_core_ecosystem"},
    {"provider_id": "NAVER_LANGUAGE", "name": "NAVER LANGUAGE", "folder": "naver_language_core_ecosystem"},
    {"provider_id": "OPENAI_LANGUAGE", "name": "OPENAI LANGUAGE", "folder": "openai_language_core_ecosystem"},
    {"provider_id": "TENCENT_LANGUAGE", "name": "TENCENT LANGUAGE", "folder": "tencent_language_core_ecosystem"},
    {"provider_id": "YANDEX_LANGUAGE", "name": "YANDEX LANGUAGE", "folder": "yandex_language_core_ecosystem"},
)

SERVICE_TIERS = (
    {"tier_id": "NORMAL", "name": "Normal", "rank": 1, "description": "Foundational access and basic discovery."},
    {"tier_id": "BASIC", "name": "Basic", "rank": 2, "description": "Core human-language records and essential tools."},
    {"tier_id": "STANDARD", "name": "Standard", "rank": 3, "description": "Expanded human-language coverage and routine workflows."},
    {"tier_id": "PREMIUM", "name": "Premium", "rank": 4, "description": "Advanced human-language services and quality controls."},
    {"tier_id": "PROFESSIONAL", "name": "Professional", "rank": 5, "description": "Professional-grade workflows, governance and support."},
    {"tier_id": "ENTERPRISE", "name": "Enterprise", "rank": 6, "description": "Organization-scale governance, integrations and administration."},
    {"tier_id": "SUPREME", "name": "Supreme", "rank": 7, "description": "Highest defined service tier, subject to law, rights, safety and actual implementation."},
)


def get_divisions():
    return [{"division_id": "HUMAN-LANGUAGES", "name": "HUMAN LANGUAGES", "folder": "global_human_language_core_ecosystem"}]


def get_domains(division=None):
    if division is not None and division.upper() not in {"HUMAN", "HUMAN-LANGUAGES"}:
        return []
    return deepcopy(list(HUMAN_LANGUAGE_DOMAINS))


def get_domain(domain_id):
    for item in HUMAN_LANGUAGE_DOMAINS:
        if item["id"] == domain_id.upper():
            return deepcopy(item)
    return None


def get_provider_catalog():
    return deepcopy(list(HUMAN_LANGUAGE_PROVIDERS))


def get_service_tiers():
    return deepcopy(list(SERVICE_TIERS))


def get_catalog():
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "status": STATUS,
        "division_count": 1,
        "divisions": get_divisions(),
        "domain_count": len(HUMAN_LANGUAGE_DOMAINS),
        "domains": get_domains(),
        "providers": get_provider_catalog(),
        "service_tiers": get_service_tiers(),
        "human_language_coverage_exhaustive": False,
        "live_provider_connections_verified": False,
    }
