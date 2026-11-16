"""Authentication event validation; no credential verification is performed."""
from dataclasses import dataclass
@dataclass(frozen=True)
class AuthenticationEvent:
    subject_id: str
    method: str
    success: bool
    source: str | None = None
    mfa_used: bool = False
def validate_authentication_event(event: AuthenticationEvent):
    issues=[]
    if not event.subject_id.strip(): issues.append("subject_id_required")
    if event.method not in {"password", "passkey", "mfa", "sso", "certificate", "service_token"}: issues.append("unsupported_authentication_method")
    if not event.success: issues.append("authentication_failed")
    return tuple(issues)
