"""Canonical finance domain-to-package mapping.

This module describes repository ownership only; it does not connect to providers
or execute regulated financial activities.
"""

DOMAIN_PACKAGES = {
    "BANKING": (
        "global_banking_core_ecosystem",
        "commercial_retail_banking_core_ecosystem",
        "central_reserve_banking_monetary_policy_core_ecosystem",
        "digital_open_banking_core_ecosystem",
        "bank_transfer_neft_rtgs_imps_core_ecosystem",
        "open_banking_account_to_account_payment_core_ecosystem",
    ),
    "INSURANCE": (
        "global_insurance_core_ecosystem",
        "life_health_insurance_core_ecosystem",
        "general_property_casualty_insurance_core_ecosystem",
        "reinsurance_catastrophe_risk_core_ecosystem",
        "insurance_distribution_underwriting_claims_core_ecosystem",
    ),
    "MARKETS_AND_INVESTMENTS": (
        "capital_markets_securities_exchange_core_ecosystem",
        "asset_wealth_management_core_ecosystem",
        "funds_etf_pension_retirement_core_ecosystem",
    ),
    "LENDING_AND_INCLUSION": (
        "global_lending_credit_financing_core_ecosystem",
        "microfinance_financial_inclusion_core_ecosystem",
        "merchant_onboarding_underwriting_core_ecosystem",
    ),
    "ACCOUNTING_AND_TAX": (
        "accounting_tax_audit_reconciliation_core_ecosystem",
        "invoice_tax_reconciliation_accounting_core_ecosystem",
    ),
    "CORPORATE_FINANCE_AND_TREASURY": (
        "corporate_finance_treasury_cash_management_core_ecosystem",
    ),
    "RISK_AND_COMPLIANCE": (
        "financial_risk_compliance_aml_fraud_core_ecosystem",
        "financial_regulators_standards_deposit_protection_core_ecosystem",
        "fraud_risk_velocity_screening_core_ecosystem",
        "regulatory_kyc_aml_sanctions_compliance_core_ecosystem",
        "payment_security_tokenization_3ds_core_ecosystem",
    ),
    "FINANCIAL_DATA_AND_CREDIT": (
        "financial_data_analytics_credit_bureau_core_ecosystem",
    ),
    "FINTECH_AND_OPEN_FINANCE": (
        "fintech_infrastructure_open_finance_core_ecosystem",
        "payment_orchestration_routing_core_ecosystem",
        "payment_gateway_core_ecosystem",
        "global_payment_providers_core_ecosystem",
        "integrations",
        "services",
        "tools",
    ),
    "PAYMENTS_AND_BILLING": (
        "adult_age_consent_privacy_compliance_payment_core_ecosystem",
        "adult_content_platform_payment_processing_core_ecosystem",
        "adult_creator_payouts_business_payments_core_ecosystem",
        "adult_industry_payment_provider_directory_core_ecosystem",
        "adult_merchant_account_high_risk_underwriting_core_ecosystem",
        "adult_refunds_chargebacks_disputes_core_ecosystem",
        "adult_subscription_membership_billing_core_ecosystem",
        "apple_payment_core_ecosystem",
        "card_payment_core_ecosystem",
        "ccbill_payment_core_ecosystem",
        "creator_freelancer_payout_core_ecosystem",
        "cross_border_multi_currency_fx_core_ecosystem",
        "digital_wallet_payment_core_ecosystem",
        "epoch_payment_core_ecosystem",
        "india_payment_core_ecosystem",
        "international_wire_transfer_core_ecosystem",
        "marketplace_split_payment_core_ecosystem",
        "paxum_payment_core_ecosystem",
        "payment_links_checkout_core_ecosystem",
        "payment_service_tiers_normal_to_supreme_core_ecosystem",
        "paypal_payment_core_ecosystem",
        "pos_qr_contactless_payment_core_ecosystem",
        "recurring_subscription_billing_core_ecosystem",
        "refunds_reversals_disputes_chargebacks_core_ecosystem",
        "segpay_payment_core_ecosystem",
        "shopify_payment_core_ecosystem",
        "stripe_payment_core_ecosystem",
        "upi_payment_core_ecosystem",
        "verotel_payment_core_ecosystem",
    ),
    "ADVISORY_AND_PLANNING": (
        "financial_advisory_planning_education_core_ecosystem",
    ),
    "INTERNATIONAL_FINANCE": (
        "international_finance_fx_remittance_trade_finance_core_ecosystem",
    ),
    "DIGITAL_ASSETS": (
        "digital_assets_blockchain_finance_core_ecosystem",
    ),
    "PUBLIC_AND_DEVELOPMENT_FINANCE": (
        "government_public_development_finance_core_ecosystem",
    ),
}

DOMAIN_NAMES = {
    "BANKING": "Banking and monetary systems",
    "INSURANCE": "Insurance and reinsurance",
    "MARKETS_AND_INVESTMENTS": "Capital markets and investments",
    "LENDING_AND_INCLUSION": "Lending, credit and financial inclusion",
    "ACCOUNTING_AND_TAX": "Accounting, taxation and reconciliation",
    "CORPORATE_FINANCE_AND_TREASURY": "Corporate finance and treasury",
    "RISK_AND_COMPLIANCE": "Financial risk, regulation and compliance",
    "FINANCIAL_DATA_AND_CREDIT": "Financial data, analytics and credit information",
    "FINTECH_AND_OPEN_FINANCE": "Fintech infrastructure and open finance",
    "PAYMENTS_AND_BILLING": "Payments, billing, settlement and payouts",
    "ADVISORY_AND_PLANNING": "Financial advisory, planning and education",
    "INTERNATIONAL_FINANCE": "International finance, FX and trade finance",
    "DIGITAL_ASSETS": "Digital assets and blockchain finance",
    "PUBLIC_AND_DEVELOPMENT_FINANCE": "Public and development finance",
}
