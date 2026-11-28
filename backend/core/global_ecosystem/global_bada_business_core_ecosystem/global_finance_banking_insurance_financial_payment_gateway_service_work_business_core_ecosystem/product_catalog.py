"""Package inventory derived from the canonical Global Finance CORE package map."""
from __future__ import annotations
from .domain_catalog import BUSINESS_DOMAINS
from ...global_finance_banking_insurance_financial_payment_gateway_core_ecosystem.domain_catalog import DOMAIN_PACKAGES, DOMAIN_DEFINITIONS

_BUSINESS_BY_CORE = {item["core_domain_id"]: item for item in BUSINESS_DOMAINS}
FINANCE_BUSINESS_PACKAGES = tuple(
    {
        "package_id": package.removesuffix("_core_ecosystem").upper(),
        "package_name": package,
        "canonical_domain_id": domain_id,
        "canonical_domain_name": DOMAIN_DEFINITIONS[domain_id]["name"],
        "business_domain_id": _BUSINESS_BY_CORE[domain_id]["domain_id"],
        "business_domain_name": _BUSINESS_BY_CORE[domain_id]["name"],
        "business_lines": list(_BUSINESS_BY_CORE[domain_id]["business_lines"]),
        "classification_types": ["SERVICE", "WORK", "BUSINESS"],
        "core_module": (
            "backend/core/global_ecosystem/global_core_ecosystem/"
            "global_finance_banking_insurance_financial_payment_gateway_core_ecosystem/"
            + package
        ),
        "status": "CORE_CATALOG_ONLY",
        "connected": False,
        "execution_enabled": False,
    }
    for domain_id, package_names in DOMAIN_PACKAGES.items()
    for package in package_names
)

def list_packages(*, domain_id: str | None = None, business_domain_id: str | None = None) -> list[dict]:
    return [
        dict(item)
        for item in FINANCE_BUSINESS_PACKAGES
        if (domain_id is None or item["canonical_domain_id"] == domain_id)
        and (business_domain_id is None or item["business_domain_id"] == business_domain_id)
    ]

def get_package(package_name: str) -> dict | None:
    needle = package_name.strip().casefold()
    if not needle:
        return None
    item = next((x for x in FINANCE_BUSINESS_PACKAGES
                 if x["package_name"].casefold() == needle or x["package_id"].casefold() == needle), None)
    return dict(item) if item else None

def search_packages(keyword: str) -> list[dict]:
    needle = keyword.strip().casefold()
    if not needle:
        return []
    return [
        dict(x) for x in FINANCE_BUSINESS_PACKAGES
        if needle in " ".join((x["package_id"], x["package_name"], x["canonical_domain_name"],
                               x["business_domain_name"], *x["business_lines"])).casefold()
    ]

def package_summary() -> dict:
    return {
        "package_count": len(FINANCE_BUSINESS_PACKAGES),
        "canonical_package_count": len(FINANCE_BUSINESS_PACKAGES),
        "live_connections_verified": 0,
        "execution_enabled": False,
    }
