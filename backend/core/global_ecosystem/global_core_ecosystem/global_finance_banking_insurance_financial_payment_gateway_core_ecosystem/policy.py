"""Security, legal and operational boundaries for finance Core."""
FINANCIAL_TRANSACTION_EXECUTION_ENABLED = False
PROVIDER_CONNECTIONS_ENABLED = False
REQUIRES_JURISDICTIONAL_REVIEW = True
REQUIRES_LICENSE_OR_AUTHORIZATION_WHERE_APPLICABLE = True
PROHIBITED_REPOSITORY_DATA = ("payment_card_security_codes","plaintext_bank_credentials",
"authentication_secrets","private_keys_or_seed_phrases","unencrypted_personal_financial_records")
REQUIRED_CONTROLS_FOR_FUTURE_TRANSACTION_SERVICES = ("authorization_and_least_privilege",
"strong_customer_authentication_where_required","idempotency_and_duplicate_prevention",
"immutable_audit_trail","ledger_integrity_and_reconciliation","fraud_sanctions_and_aml_screening",
"privacy_and_data_retention","incident_response_and_operational_monitoring",
"provider_webhook_signature_validation","settlement_and_chargeback_controls")
class FinancePolicyError(ValueError): pass
class FinanceCorePolicy:
    @staticmethod
    def assert_catalogue_only(operation: str) -> None:
        if operation.strip().casefold() in {"charge","capture","refund","transfer","payout","underwrite",
        "bind_policy","lend","invest","trade"}:
            raise FinancePolicyError("FINANCIAL_OPERATION_NOT_ENABLED_IN_CORE")
