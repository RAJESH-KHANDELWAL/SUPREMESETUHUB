"""Canonical child/provider package inventory; no live connection is implied."""
from .domain_catalog import DOMAIN_DEFINITIONS, DOMAIN_PACKAGES
FINANCE_PACKAGES = tuple(
    {"package_id": n.removesuffix("_core_ecosystem").upper(), "package_name": n,
     "domain_id": d, "domain_name": DOMAIN_DEFINITIONS[d]["name"],
     "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_finance_banking_insurance_financial_payment_gateway_core_ecosystem/" + n, "status": "CORE_CATALOG_ONLY", "connected": False}
    for d, names in DOMAIN_PACKAGES.items() for n in names
)
def list_finance_packages(*, domain_id: str | None = None) -> list[dict]:
    return [dict(x) for x in FINANCE_PACKAGES if domain_id is None or x["domain_id"] == domain_id]
def finance_packages_summary() -> dict:
    return {"package_count": len(FINANCE_PACKAGES), "live_connections_verified": 0,
            "packages": list_finance_packages()}
