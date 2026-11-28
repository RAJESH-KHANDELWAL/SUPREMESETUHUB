"""Read-only bridge to the canonical 2468-target master catalogue."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from .constants import MASTER_CATALOG_PATH, MASTER_CATALOG_TARGET

def get_master_catalog_status() -> dict[str, Any]:
    path = Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    if not path.is_file():
        return {"available": False, "path": MASTER_CATALOG_PATH, "access_mode": "READ_ONLY_ON_DEMAND", "target_unique_entries": MASTER_CATALOG_TARGET}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        finance = data.get("implementation_registry", {}).get("global_finance_banking_insurance_financial_payment_gateway_core_ecosystem", {})
        domains = finance.get("domains", [])
        payment_domain = next((d for d in domains if d.get("domain_id") == "PAYMENT_GATEWAYS_AND_MERCHANT_ACQUIRING"), {})
        billing_domain = next((d for d in domains if d.get("domain_id") == "PAYMENT_BILLING_SETTLEMENT_AND_PAYOUTS"), {})
        paypal_registered = "paypal_payment_core_ecosystem" in payment_domain.get("package_names", [])
        return {"available": True, "path": MASTER_CATALOG_PATH, "access_mode": "READ_ONLY_ON_DEMAND", "target_unique_entries": data.get("expansion", {}).get("target_unique_entries", MASTER_CATALOG_TARGET), "current_unique_entries": data.get("expansion", {}).get("current_unique_entries"), "finance_registry_id": finance.get("ecosystem_id"), "paypal_payment_package_registered": paypal_registered, "payment_gateway_domain": payment_domain.get("domain_id"), "billing_payout_domain": billing_domain.get("domain_id"), "taxonomy_entries_added": 0, "source_modified": False}
    except (OSError, json.JSONDecodeError, AttributeError):
        return {"available": False, "path": MASTER_CATALOG_PATH, "access_mode": "READ_ONLY_ON_DEMAND", "error": "MASTER_CATALOG_READ_FAILED"}
