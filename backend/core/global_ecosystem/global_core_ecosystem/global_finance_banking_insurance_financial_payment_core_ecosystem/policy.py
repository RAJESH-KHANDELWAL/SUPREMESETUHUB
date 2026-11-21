"""Safety and scope policy for the finance ecosystem catalogue."""

FINANCIAL_TRANSACTION_EXECUTION_ENABLED = False
REQUIRES_JURISDICTIONAL_REVIEW = True
PROHIBITED_REPOSITORY_DATA = (
    "payment_card_security_codes",
    "plaintext_bank_credentials",
    "authentication_secrets",
    "unencrypted_personal_financial_records",
)

REQUIRED_CONTROLS_FOR_FUTURE_TRANSACTION_SERVICES = (
    "authorization_and_least_privilege",
    "strong_customer_authentication_where_required",
    "idempotency_and_duplicate_prevention",
    "immutable_audit_trail",
    "ledger_integrity_and_reconciliation",
    "fraud_and_sanctions_screening",
    "privacy_and_data_retention",
    "incident_response_and_operational_monitoring",
)
