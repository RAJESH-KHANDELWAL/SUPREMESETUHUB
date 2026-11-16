"""Finance, Banking & Insurance category taxonomy."""
from __future__ import annotations

FINANCE_BANKING_INSURANCE_CATEGORIES = [
    {
        "id": "banking_and_deposits",
        "name": "Banking & Deposits",
        "subcategories": [
            "retail_banking", "business_banking", "digital_banking",
            "deposit_services", "banking_services"
        ]
    },
    {
        "id": "payments_and_remittances",
        "name": "Payments & Remittances",
        "subcategories": [
            "payment_gateways",
            "upi_and_account_transfers",
            "cross_border_remittances",
            "merchant_acquiring"
        ]
    },
    {
        "id": "lending_and_credit",
        "name": "Lending & Credit",
        "subcategories": [
            "personal_loans", "business_loans", "working_capital", "credit_scoring",
            "loans_credit"
        ]
    },
    {
        "id": "insurance_services",
        "name": "Insurance Services",
        "subcategories": [
            "life_insurance", "health_insurance", "general_insurance",
            "commercial_insurance", "insurance"
        ]
    },
    {
        "id": "wealth_and_investment_advisory",
        "name": "Wealth & Investment Advisory",
        "subcategories": [
            "financial_planning", "portfolio_advisory", "investment_research",
            "wealth_management"
        ]
    },
    {
        "id": "capital_markets_and_brokerage",
        "name": "Capital Markets & Brokerage",
        "subcategories": [
            "equity_broking",
            "debt_markets",
            "mutual_fund_distribution",
            "market_infrastructure"
        ]
    },
    {
        "id": "accounting_and_bookkeeping",
        "name": "Accounting, Tax & Bookkeeping",
        "subcategories": [
            "bookkeeping", "tax_preparation", "audit_support", "financial_reporting",
            "tax_services", "accounting_audit"
        ]
    },
    {
        "id": "fintech_and_financial_software",
        "name": "FinTech & Financial Software",
        "subcategories": [
            "core_banking_technology",
            "lending_software",
            "personal_finance_apps",
            "financial_automation"
        ]
    },
    {
        "id": "microfinance_and_inclusion",
        "name": "Microfinance & Financial Inclusion",
        "subcategories": [
            "microfinance_institutions",
            "self_help_group_finance",
            "rural_finance",
            "financial_literacy"
        ]
    },
    {
        "id": "corporate_finance_and_advisory",
        "name": "Corporate Finance & Advisory",
        "subcategories": [
            "mergers_and_acquisitions", "valuation_services", "fundraising_advisory",
            "transaction_advisory", "business_finance", "capital_raising",
            "grants_subsidies", "government_schemes", "msme_support",
            "business_valuation"
        ]
    },
    {
        "id": "pension_and_retirement",
        "name": "Pension & Retirement Services",
        "subcategories": [
            "retirement_planning",
            "pension_administration",
            "provident_fund_services",
            "annuity_products"
        ]
    },
    {
        "id": "risk_and_compliance",
        "name": "Risk, Compliance & RegTech",
        "subcategories": [
            "kyc_and_aml", "fraud_prevention", "regulatory_reporting",
            "enterprise_risk", "risk_management"
        ]
    },
    {
        "id": "foreign_exchange_and_trade_finance",
        "name": "Foreign Exchange & Trade Finance",
        "subcategories": [
            "currency_exchange", "trade_credit", "letters_of_credit",
            "export_finance", "export_import_support"
        ]
    },
    {
        "id": "insurance_broking_and_claims",
        "name": "Insurance Broking & Claims",
        "subcategories": [
            "insurance_brokers",
            "claims_assessment",
            "claims_administration",
            "reinsurance_services"
        ]
    },
    {
        "id": "financial_education",
        "name": "Financial Education & Literacy",
        "subcategories": [
            "personal_finance_education", "investment_education",
            "investor_education",
            "business_finance_training",
            "debt_management_guidance"
        ]
    }
]

def list_categories() -> list[dict[str, object]]:
    """Return defensive copies of all categories."""
    return [dict(item, subcategories=list(item["subcategories"])) for item in FINANCE_BANKING_INSURANCE_CATEGORIES]

def get_category(category_id: str) -> dict[str, object] | None:
    """Return one category by stable identifier."""
    for item in FINANCE_BANKING_INSURANCE_CATEGORIES:
        if item["id"] == category_id:
            return dict(item, subcategories=list(item["subcategories"]))
    return None


# Legacy finance-support IDs are mapped into the canonical finance categories.
LEGACY_CATEGORY_CROSSWALK = {
    "banking_services": "banking_and_deposits",
    "loans_credit": "lending_and_credit",
    "insurance": "insurance_services",
    "tax_services": "accounting_and_bookkeeping",
    "accounting_audit": "accounting_and_bookkeeping",
    "investment_education": "financial_education",
    "business_finance": "corporate_finance_and_advisory",
    "personal_finance_education": "financial_education",
    "capital_raising": "corporate_finance_and_advisory",
    "grants_subsidies": "corporate_finance_and_advisory",
    "government_schemes": "corporate_finance_and_advisory",
    "msme_support": "corporate_finance_and_advisory",
    "export_import_support": "foreign_exchange_and_trade_finance",
    "business_valuation": "corporate_finance_and_advisory",
    "risk_management": "risk_and_compliance",
}
