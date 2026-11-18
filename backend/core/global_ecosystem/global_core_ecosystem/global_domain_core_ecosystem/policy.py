"""Fail-closed policy for domain Core metadata and operation classification."""

from collections.abc import Mapping

SECRET_KEYS = {
    "token", "access_token", "refresh_token", "api_key", "client_secret",
    "secret", "password", "authorization", "private_key", "credential_value",
}
MUTATING_OPERATIONS = {
    "REGISTER_DOMAIN", "PURCHASE_DOMAIN", "RENEW_DOMAIN", "TRANSFER_DOMAIN",
    "DELETE_DOMAIN", "UPDATE_DNS", "DELETE_DNS", "CHANGE_NAMESERVERS",
    "ISSUE_CERTIFICATE", "REVOKE_CERTIFICATE", "DEPLOY_CUSTOM_DOMAIN",
    "UPDATE_REGISTRANT", "UPDATE_CONTACT", "UPDATE_BILLING",
}


class DomainCorePolicyError(PermissionError):
    pass


def reject_secret_material(value):
    if isinstance(value, Mapping):
        for key, nested in value.items():
            normalized = str(key).casefold().replace("-", "_")
            if normalized in SECRET_KEYS:
                raise ValueError("SECRET_MATERIAL_FORBIDDEN_IN_DOMAIN_CORE")
            reject_secret_material(nested)
    elif isinstance(value, (list, tuple)):
        for nested in value:
            reject_secret_material(nested)


def classify_operation(operation: str) -> str:
    normalized = str(operation).strip().upper()
    if not normalized:
        raise ValueError("DOMAIN_OPERATION_REQUIRED")
    if normalized in MUTATING_OPERATIONS:
        return "MUTATING_REQUIRES_EXTERNAL_AUTHORIZATION_CONFIRMATION_AUDIT_AND_RUNTIME"
    return "METADATA_ONLY_UNLESS_PROVIDER_CONTRACT_SAYS_OTHERWISE"


def require_metadata_only(operation: str) -> None:
    classification = classify_operation(operation)
    if classification.startswith("MUTATING_"):
        raise DomainCorePolicyError("DOMAIN_PROVIDER_MUTATION_DISABLED_IN_CORE")
