"""Regulatory and operational guardrails for finance service/work/business metadata."""
FINANCIAL_EXECUTION_ENABLED = False
PROVIDER_CONNECTIONS_ENABLED = False
REQUIRES_JURISDICTIONAL_REVIEW = True
REQUIRES_LICENSE_OR_AUTHORIZATION_WHERE_APPLICABLE = True

PROHIBITED_REPOSITORY_DATA = (
    "payment_card_security_codes",
    "plaintext_bank_credentials",
    "authentication_secrets",
    "private_keys_or_seed_phrases",
    "unencrypted_personal_financial_records",
)

BLOCKED_OPERATION_MARKERS = {
    "charge", "capture", "refund", "transfer", "payout", "underwrite",
    "bind_policy", "lend", "invest", "trade", "open_account", "close_account",
}

class FinanceBusinessPolicyError(PermissionError):
    """Raised when a metadata-only CORE request attempts operational execution."""

class FinanceServiceWorkBusinessPolicy:
    @staticmethod
    def assert_classification_only(operation: str) -> None:
        normalized = operation.strip().casefold().replace("-", "_").replace(" ", "_")
        if normalized in BLOCKED_OPERATION_MARKERS:
            raise FinanceBusinessPolicyError("FINANCIAL_OPERATION_NOT_ENABLED_IN_CLASSIFICATION_CORE")

    @staticmethod
    def safe_public_summary(payload: dict) -> dict:
        blocked = {"token", "access_token", "refresh_token", "client_secret", "api_key", "secret",
                   "account_number", "card_number", "cvv", "security_code"}
        return {key: value for key, value in payload.items() if key.casefold() not in blocked}
