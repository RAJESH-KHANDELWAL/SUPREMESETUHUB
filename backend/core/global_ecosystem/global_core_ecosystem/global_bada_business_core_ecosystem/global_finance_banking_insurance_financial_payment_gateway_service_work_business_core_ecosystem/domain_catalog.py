"""Commercial finance service/work/business taxonomy mapped to canonical Global CORE."""
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

BUSINESS_DOMAINS = tuple({
    "domain_id": row[0],
    "name": row[1],
    "core_domain_id": row[2],
    "canonical_domain_name": CANONICAL_DOMAIN_DEFINITIONS[row[2]]["name"],
    "package_names": list(CANONICAL_DOMAIN_PACKAGES[row[2]]),
    "service_work_business_capabilities": ["SERVICE", "WORK", "BUSINESS"],
    "business_lines": list(row[3]),
    "classification_only": True,
} for row in BUSINESS_DOMAIN_ROWS)

def list_domains():
    return deepcopy(list(BUSINESS_DOMAINS))

def get_domain(domain_id):
    key = domain_id.strip().casefold()
    return next((deepcopy(item) for item in BUSINESS_DOMAINS if item["domain_id"].casefold() == key), None)

def search_domains(keyword):
    key = keyword.strip().casefold()
    if not key:
        return []
    return [deepcopy(item) for item in BUSINESS_DOMAINS
            if key in " ".join((item["domain_id"], item["name"], item["core_domain_id"], *item["business_lines"])).casefold()]

def validate_mappings():
    ids = [item["domain_id"] for item in BUSINESS_DOMAINS]
    missing = sorted({item["core_domain_id"] for item in BUSINESS_DOMAINS} - set(CANONICAL_DOMAIN_DEFINITIONS))
    missing_packages = sorted({name for item in BUSINESS_DOMAINS for name in item["package_names"]}
                              - {name for names in CANONICAL_DOMAIN_PACKAGES.values() for name in names})
    return {
        "valid": len(ids) == len(set(ids)) and not missing and not missing_packages,
        "business_domain_count": len(ids),
        "unique_domain_ids": len(ids) == len(set(ids)),
        "missing_core_domain_ids": missing,
        "missing_canonical_packages": missing_packages,
    }
