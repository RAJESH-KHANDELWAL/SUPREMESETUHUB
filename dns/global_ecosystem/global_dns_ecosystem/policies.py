"""Fail-closed DNS change policies."""
from .models import DNSChangeRequest

def validate_change_request(request: DNSChangeRequest):
    request.validate()
    if not request.approved:
        raise PermissionError("EXPLICIT_DNS_CHANGE_APPROVAL_REQUIRED")
    return True

def ensure_client(provider_id: str, clients: dict):
    client = clients.get(provider_id.strip().lower())
    if client is None:
        raise RuntimeError(f"DNS_PROVIDER_CLIENT_NOT_CONFIGURED:{provider_id}")
    return client
