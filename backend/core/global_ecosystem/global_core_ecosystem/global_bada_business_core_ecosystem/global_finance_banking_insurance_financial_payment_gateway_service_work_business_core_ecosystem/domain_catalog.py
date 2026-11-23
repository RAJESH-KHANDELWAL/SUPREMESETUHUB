"""Business taxonomy mapped one-to-one to the canonical Global Finance CORE."""
from __future__ import annotations
from copy import deepcopy
from ...global_finance_banking_insurance_financial_payment_gateway_core_ecosystem.domain_catalog import (
    DOMAIN_DEFINITIONS as CANONICAL_DOMAIN_DEFINITIONS,
    DOMAIN_PACKAGES as CANONICAL_DOMAIN_PACKAGES,
)

BUSINESS_DOMAIN_ROWS = (
    ("banking_services", "Banking Services & Operations", "BANKING", ("retail_banking", "commercial_banking", "cooperative_banking", "digital_banking", "open_banking", "banking_operations", "banking_consulting")),
    ("insurance_services", "Insurance & Risk Services", "INSURANCE", ("life_insurance", "health_insurance", "general_insurance", "reinsurance", "brokerage", "claims_administration", "actuarial_services")),
    ("capital_markets_investment_services", "Capital Markets & Investment Services", "CAPITAL_MARKETS_AND_INVESTMENTS", ("brokerage_services", "investment_operations", "fund_management", "wealth_management", "custody_services", "capital_advisory")),
    ("lending_credit_asset_finance_services", "Lending, Credit & Asset Finance Services", "LENDING_CREDIT_AND_ASSET_FINANCE", ("loan_servicing", "credit_operations", "microfinance", "leasing", "invoice_factoring", "supply_chain_finance")),
    ("accounting_tax_audit_services", "Accounting, Tax & Audit Services", "ACCOUNTING_TAX_AND_AUDIT", ("bookkeeping", "tax_preparation", "audit_support", "financial_reporting", "reconciliation", "payroll_accounting")),
    ("corporate_finance_treasury_services", "Corporate Finance & Treasury Services", "CORPORATE_FINANCE_AND_TREASURY", ("treasury_operations", "cash_management", "working_capital_advisory", "fundraising_support", "financial_modelling")),
    ("financial_risk_compliance_services", "Financial Risk, Regulation & Compliance Services", "FINANCIAL_RISK_REGULATION_AND_COMPLIANCE", ("kyc_operations", "aml_compliance", "fraud_monitoring", "risk_assessment", "regulatory_reporting", "dispute_operations")),
    ("financial_data_credit_intelligence_services", "Financial Data & Credit Intelligence Services", "FINANCIAL_DATA_AND_CREDIT_INTELLIGENCE", ("credit_research", "credit_data_operations", "financial_analytics", "bureau_support", "risk_data_services")),
    ("fintech_open_finance_services", "Fintech, Open Finance & Infrastructure Services", "FINTECH_OPEN_FINANCE_AND_INFRASTRUCTURE", ("fintech_product_services", "open_finance_integrations", "financial_api_services", "digital_asset_infrastructure", "fintech_consulting")),
    ("payment_gateway_merchant_services", "Payment Gateway & Merchant Services", "PAYMENT_GATEWAYS_AND_MERCHANT_ACQUIRING", ("gateway_onboarding", "merchant_acquiring_support", "payment_integration", "checkout_optimization", "merchant_operations")),
    ("payment_rails_wallet_transfer_services", "Payment Rails, Wallet & Transfer Services", "PAYMENT_RAILS_WALLETS_AND_TRANSFERS", ("upi_operations", "card_payment_support", "wallet_operations", "bank_transfer_support", "qr_pos_services", "cross_border_transfer_support")),
    ("payment_billing_settlement_payout_services", "Payment Billing, Settlement & Payout Services", "PAYMENT_BILLING_SETTLEMENT_AND_PAYOUTS", ("subscription_billing", "payment_reconciliation", "settlement_operations", "marketplace_payouts", "refund_dispute_support")),
    ("financial_advisory_education_services", "Financial Advisory & Education Services", "FINANCIAL_ADVISORY_AND_EDUCATION", ("financial_literacy_training", "financial_education", "planning_support", "professional_training", "business_finance_coaching")),
    ("international_finance_fx_remittance_services", "International Finance, FX & Remittance Services", "INTERNATIONAL_FINANCE_FX_AND_REMITTANCE", ("fx_operations", "remittance_support", "trade_finance_support", "cross_border_finance_operations")),
    ("public_development_social_finance_services", "Public, Development & Social Finance Services", "PUBLIC_DEVELOPMENT_AND_SOCIAL_FINANCE", ("development_finance_support", "pension_administration_support", "financial_inclusion_programs", "public_finance_research")),
)

CLASSIFICATION_TYPES = ("SERVICE", "WORK", "BUSINESS")
SERVICE_WORK_BUSINESS_LAYERS = {
    "SERVICE": "A deliverable offered to an individual, organization or institution.",
    "WORK": "A role, task, project, profession, operation or engagement performed by people or systems.",
    "BUSINESS": "An organization, enterprise, practice, marketplace or commercial operating model.",
}
DELIVERY_MODELS = (
    "B2B", "B2C", "B2B2C", "B2G", "G2B", "G2C", "D2C",
    "MARKETPLACE", "PLATFORM", "AGENCY", "CONSULTANCY", "FREELANCE",
    "EMPLOYMENT", "SUBSCRIPTION", "TRANSACTIONAL", "NONPROFIT", "COOPERATIVE",
)

BUSINESS_DOMAINS = tuple({
    "domain_id": row[0],
    "name": row[1],
    "core_domain_id": row[2],
    "canonical_domain_name": CANONICAL_DOMAIN_DEFINITIONS[row[2]]["name"],
    "canonical_purpose": CANONICAL_DOMAIN_DEFINITIONS[row[2]]["purpose"],
    "package_names": list(CANONICAL_DOMAIN_PACKAGES[row[2]]),
    "service_work_business_capabilities": list(CLASSIFICATION_TYPES),
    "business_lines": list(row[3]),
    "delivery_models": list(DELIVERY_MODELS),
    "jurisdictional_review_required": True,
    "execution_enabled": False,
} for row in BUSINESS_DOMAIN_ROWS)

BUSINESS_DOMAIN_BY_ID = {item["domain_id"]: item for item in BUSINESS_DOMAINS}
BUSINESS_DOMAIN_BY_CORE_ID = {item["core_domain_id"]: item for item in BUSINESS_DOMAINS}
PACKAGE_TO_BUSINESS_DOMAIN = {
    package: item["domain_id"]
    for item in BUSINESS_DOMAINS
    for package in item["package_names"]
}

def list_domains() -> list[dict]:
    return deepcopy(list(BUSINESS_DOMAINS))

def get_domain(domain_id: str) -> dict | None:
    if not isinstance(domain_id, str):
        return None
    key = domain_id.strip().casefold()
    item = next((x for x in BUSINESS_DOMAINS if x["domain_id"].casefold() == key
                 or x["core_domain_id"].casefold() == key), None)
    return deepcopy(item) if item else None

def search_domains(keyword: str) -> list[dict]:
    if not isinstance(keyword, str) or not keyword.strip():
        return []
    key = keyword.strip().casefold()
    return [deepcopy(item) for item in BUSINESS_DOMAINS
            if key in " ".join((item["domain_id"], item["name"], item["core_domain_id"],
                                item["canonical_domain_name"], item["canonical_purpose"],
                                *item["package_names"], *item["business_lines"])).casefold()]

def business_domain_summary() -> dict:
    return {
        "success": True,
        "domain_count": len(BUSINESS_DOMAINS),
        "package_count": len(PACKAGE_TO_BUSINESS_DOMAIN),
        "classification_types": list(CLASSIFICATION_TYPES),
        "domains": list_domains(),
    }

def validate_mappings() -> dict:
    ids = [item["domain_id"] for item in BUSINESS_DOMAINS]
    core_ids = [item["core_domain_id"] for item in BUSINESS_DOMAINS]
    all_canonical_packages = {
        package for package_names in CANONICAL_DOMAIN_PACKAGES.values() for package in package_names
    }
    mapped_packages = list(PACKAGE_TO_BUSINESS_DOMAIN)
    missing_core_ids = sorted(set(CANONICAL_DOMAIN_DEFINITIONS) - set(core_ids))
    unknown_core_ids = sorted(set(core_ids) - set(CANONICAL_DOMAIN_DEFINITIONS))
    missing_packages = sorted(all_canonical_packages - set(mapped_packages))
    unknown_packages = sorted(set(mapped_packages) - all_canonical_packages)
    duplicate_packages = sorted({name for name in mapped_packages if mapped_packages.count(name) > 1})
    valid = (
        len(ids) == len(set(ids))
        and len(core_ids) == len(set(core_ids))
        and not missing_core_ids and not unknown_core_ids
        and not missing_packages and not unknown_packages and not duplicate_packages
        and all(item["package_names"] and item["business_lines"] for item in BUSINESS_DOMAINS)
    )
    return {
        "valid": valid,
        "business_domain_count": len(ids),
        "canonical_domain_count": len(CANONICAL_DOMAIN_DEFINITIONS),
        "canonical_package_count": len(all_canonical_packages),
        "mapped_package_count": len(mapped_packages),
        "unique_domain_ids": len(ids) == len(set(ids)),
        "unique_canonical_domain_ids": len(core_ids) == len(set(core_ids)),
        "missing_core_domain_ids": missing_core_ids,
        "unknown_core_domain_ids": unknown_core_ids,
        "missing_canonical_packages": missing_packages,
        "unknown_packages": unknown_packages,
        "duplicate_packages": duplicate_packages,
    }

__all__ = [
    "BUSINESS_DOMAINS", "BUSINESS_DOMAIN_BY_ID", "BUSINESS_DOMAIN_BY_CORE_ID",
    "PACKAGE_TO_BUSINESS_DOMAIN", "CLASSIFICATION_TYPES", "SERVICE_WORK_BUSINESS_LAYERS",
    "DELIVERY_MODELS", "list_domains", "get_domain", "search_domains",
    "business_domain_summary", "validate_mappings",
]
