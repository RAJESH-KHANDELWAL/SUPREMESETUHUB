"""Default-deny access policy evaluation helper."""
from dataclasses import dataclass
@dataclass(frozen=True)
class AccessPolicy:
    subject: str
    resource: str
    action: str
    allowed_subjects: tuple[str, ...] = ()
    allowed_actions: tuple[str, ...] = ()
    enabled: bool = True
def evaluate_access(policy: AccessPolicy) -> bool:
    if not policy.enabled:
        return False
    return policy.subject in policy.allowed_subjects and policy.action in policy.allowed_actions and bool(policy.resource.strip())
