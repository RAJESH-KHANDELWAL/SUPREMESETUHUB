"""Complete domain inventory for global finance, banking, insurance and payment gateways."""
from collections import Counter
from typing import Any
DOMAIN_DEFINITIONS = {
    "BANKING": {"name": "Banking and Monetary Systems", "purpose": "Retail, commercial, cooperative, reserve, correspondent, deposit, digital and open banking."},
    "INSURANCE": {"name": "Insurance and Reinsurance", "purpose": "Life, health, general, reinsurance, actuarial, brokerage, underwriting and claims."},
    "CAPITAL_MARKETS_AND_INVESTMENTS": {"name": "Capital Markets and Investments", "purpose": "Securities, exchanges, brokerage, custody, clearing, funds, wealth and private capital."},
    "LENDING_CREDIT_AND_ASSET_FINANCE": {"name": "Lending, Credit and Asset Finance", "purpose": "Consumer/business credit, microfinance, leasing, asset finance, factoring and supply-chain finance."},
    "ACCOUNTING_TAX_AND_AUDIT": {"name": "Accounting, Tax and Audit", "purpose": "Accounting, tax, audit, reporting, reconciliation, invoicing and governance."},
    "CORPORATE_FINANCE_AND_TREASURY": {"name": "Corporate Finance and Treasury", "purpose": "Corporate funding, treasury, liquidity, cash and working-capital management."},
    "FINANCIAL_RISK_REGULATION_AND_COMPLIANCE": {"name": "Financial Risk, Regulation and Compliance", "purpose": "Regulators, KYC, AML, sanctions, fraud, disputes and payment security."},
    "FINANCIAL_DATA_AND_CREDIT_INTELLIGENCE": {"name": "Financial Data and Credit Intelligence", "purpose": "Credit bureaus, scoring, reporting, analytics and financial data services."},
    "FINTECH_OPEN_FINANCE_AND_INFRASTRUCTURE": {"name": "Fintech, Open Finance and Infrastructure", "purpose": "Fintech platforms, open-finance standards, digital assets and infrastructure."},
    "PAYMENT_GATEWAYS_AND_MERCHANT_ACQUIRING": {"name": "Payment Gateways and Merchant Acquiring", "purpose": "Gateways, processors, acquiring, merchant onboarding and provider-specific services."},
    "PAYMENT_RAILS_WALLETS_AND_TRANSFERS": {"name": "Payment Rails, Wallets and Transfers", "purpose": "Cards, UPI, bank transfers, wallets, QR/POS and domestic/international rails."},
    "PAYMENT_BILLING_SETTLEMENT_AND_PAYOUTS": {"name": "Payment Billing, Settlement and Payouts", "purpose": "Checkout, subscriptions, marketplace splits, refunds, chargebacks, settlement and payouts."},
    "FINANCIAL_ADVISORY_AND_EDUCATION": {"name": "Financial Advisory and Education", "purpose": "Financial planning, advisory, literacy and professional education."},
    "INTERNATIONAL_FINANCE_FX_AND_REMITTANCE": {"name": "International Finance, FX and Remittance", "purpose": "Cross-border finance, FX, remittance and trade finance."},
    "PUBLIC_DEVELOPMENT_AND_SOCIAL_FINANCE": {"name": "Public, Development and Social Finance", "purpose": "Public/development finance, pensions, social protection and inclusion."},
}
DOMAIN_PACKAGES = {
    "BANKING": (
        "global_banking_core_ecosystem",
        "commercial_retail_banking_core_ecosystem",
        "central_reserve_banking_monetary_policy_core_ecosystem",
        "digital_open_banking_core_ecosystem",
        "bank_transfer_neft_rtgs_imps_core_ecosystem",
        "open_banking_account_to_account_payment_core_ecosystem",
        "digital_neobanking_core_ecosystem",
        "cooperative_rural_banking_core_ecosystem",
        "investment_banking_core_ecosystem",
        "correspondent_banking_core_ecosystem",
        "deposit_accounts_savings_current_core_ecosystem",
    ),
    "INSURANCE": (
        "global_insurance_core_ecosystem",
        "life_health_insurance_core_ecosystem",
        "general_property_casualty_insurance_core_ecosystem",
        "reinsurance_catastrophe_risk_core_ecosystem",
        "insurance_distribution_underwriting_claims_core_ecosystem",
        "insurance_actuarial_pricing_risk_models_core_ecosystem",
        "insurance_broker_agency_distribution_core_ecosystem",
    ),
    "CAPITAL_MARKETS_AND_INVESTMENTS": (
        "capital_markets_securities_exchange_core_ecosystem",
        "asset_wealth_management_core_ecosystem",
        "funds_etf_pension_retirement_core_ecosystem",
        "securities_custody_clearing_settlement_core_ecosystem",
        "brokerage_trading_investment_services_core_ecosystem",
        "private_equity_venture_capital_core_ecosystem",
        "financial_market_infrastructure_depositories_core_ecosystem",
    ),
    "LENDING_CREDIT_AND_ASSET_FINANCE": (
        "global_lending_credit_financing_core_ecosystem",
        "microfinance_financial_inclusion_core_ecosystem",
        "consumer_personal_finance_core_ecosystem",
        "asset_financing_leasing_core_ecosystem",
        "factoring_invoice_discounting_core_ecosystem",
        "trade_supply_chain_finance_core_ecosystem",
    ),
    "ACCOUNTING_TAX_AND_AUDIT": (
        "accounting_tax_audit_reconciliation_core_ecosystem",
        "invoice_tax_reconciliation_accounting_core_ecosystem",
        "financial_governance_audit_reporting_core_ecosystem",
    ),
    "CORPORATE_FINANCE_AND_TREASURY": (
        "corporate_finance_treasury_cash_management_core_ecosystem",
    ),
    "FINANCIAL_RISK_REGULATION_AND_COMPLIANCE": (
        "financial_regulators_standards_deposit_protection_core_ecosystem",
        "financial_risk_compliance_aml_fraud_core_ecosystem",
        "fraud_risk_velocity_screening_core_ecosystem",
        "regulatory_kyc_aml_sanctions_compliance_core_ecosystem",
        "payment_security_tokenization_3ds_core_ecosystem",
        "adult_age_consent_privacy_compliance_payment_core_ecosystem",
    ),
    "FINANCIAL_DATA_AND_CREDIT_INTELLIGENCE": (
        "financial_data_analytics_credit_bureau_core_ecosystem",
        "credit_scoring_reporting_bureau_core_ecosystem",
    ),
    "FINTECH_OPEN_FINANCE_AND_INFRASTRUCTURE": (
        "fintech_infrastructure_open_finance_core_ecosystem",
        "digital_assets_blockchain_finance_core_ecosystem",
    ),
    "PAYMENT_GATEWAYS_AND_MERCHANT_ACQUIRING": (
        "payment_gateway_core_ecosystem",
        "global_payment_providers_core_ecosystem",
        "adult_industry_payment_provider_directory_core_ecosystem",
        "adult_merchant_account_high_risk_underwriting_core_ecosystem",
        "merchant_onboarding_underwriting_core_ecosystem",
        "apple_payment_core_ecosystem",
        "ccbill_payment_core_ecosystem",
        "epoch_payment_core_ecosystem",
        "paxum_payment_core_ecosystem",
        "paypal_payment_core_ecosystem",
        "segpay_payment_core_ecosystem",
        "shopify_payment_core_ecosystem",
        "stripe_payment_core_ecosystem",
        "verotel_payment_core_ecosystem",
        "adyen_payment_core_ecosystem",
        "razorpay_payment_core_ecosystem",
        "cashfree_payment_core_ecosystem",
        "payu_payment_core_ecosystem",
        "worldpay_payment_core_ecosystem",
        "braintree_payment_core_ecosystem",
        "square_payment_core_ecosystem",
        "authorize_net_payment_core_ecosystem",
        "checkout_com_payment_core_ecosystem",
        "amazon_pay_payment_core_ecosystem",
        "paytm_payment_core_ecosystem",
        "phonepe_payment_core_ecosystem",
        "billdesk_payment_core_ecosystem",
        "ccavenue_payment_core_ecosystem",
        "worldline_payment_core_ecosystem",
        "globalpayments_payment_core_ecosystem",
        "wise_payment_core_ecosystem",
        "payoneer_payment_core_ecosystem",
        "airwallex_payment_core_ecosystem",
        "revolut_payment_core_ecosystem",
        "skrill_payment_core_ecosystem",
        "neteller_payment_core_ecosystem",
    ),
    "PAYMENT_RAILS_WALLETS_AND_TRANSFERS": (
        "card_payment_core_ecosystem",
        "cross_border_multi_currency_fx_core_ecosystem",
        "digital_wallet_payment_core_ecosystem",
        "india_payment_core_ecosystem",
        "international_wire_transfer_core_ecosystem",
        "pos_qr_contactless_payment_core_ecosystem",
        "upi_payment_core_ecosystem",
    ),
    "PAYMENT_BILLING_SETTLEMENT_AND_PAYOUTS": (
        "adult_content_platform_payment_processing_core_ecosystem",
        "adult_creator_payouts_business_payments_core_ecosystem",
        "adult_refunds_chargebacks_disputes_core_ecosystem",
        "adult_subscription_membership_billing_core_ecosystem",
        "creator_freelancer_payout_core_ecosystem",
        "marketplace_split_payment_core_ecosystem",
        "payment_links_checkout_core_ecosystem",
        "payment_orchestration_routing_core_ecosystem",
        "payment_service_tiers_normal_to_supreme_core_ecosystem",
        "recurring_subscription_billing_core_ecosystem",
        "refunds_reversals_disputes_chargebacks_core_ecosystem",
    ),
    "FINANCIAL_ADVISORY_AND_EDUCATION": (
        "financial_advisory_planning_education_core_ecosystem",
    ),
    "INTERNATIONAL_FINANCE_FX_AND_REMITTANCE": (
        "international_finance_fx_remittance_trade_finance_core_ecosystem",
    ),
    "PUBLIC_DEVELOPMENT_AND_SOCIAL_FINANCE": (
        "government_public_development_finance_core_ecosystem",
        "pension_social_security_benefits_core_ecosystem",
    ),
}
DOMAIN_NAMES = {key: value["name"] for key, value in DOMAIN_DEFINITIONS.items()}
PACKAGE_TO_DOMAIN = {}
for _domain_id, _packages in DOMAIN_PACKAGES.items():
    for _package in _packages:
        if _package in PACKAGE_TO_DOMAIN: raise RuntimeError(f"DUPLICATE_FINANCE_PACKAGE_ASSIGNMENT: {_package}")
        PACKAGE_TO_DOMAIN[_package] = _domain_id
def list_domain_inventory() -> list[dict[str, Any]]:
    return [{"domain_id": k, "name": v["name"], "purpose": v["purpose"],
             "package_count": len(DOMAIN_PACKAGES[k]), "packages": list(DOMAIN_PACKAGES[k])}
            for k, v in DOMAIN_DEFINITIONS.items()]
def finance_domain_summary() -> dict[str, Any]:
    counts = Counter(PACKAGE_TO_DOMAIN.values())
    return {"domain_count": len(DOMAIN_DEFINITIONS), "package_count": len(PACKAGE_TO_DOMAIN),
            "domains": [{**x, "package_count": counts[x["domain_id"]]} for x in list_domain_inventory()],
            "unassigned_packages": [], "duplicate_assignments": []}
