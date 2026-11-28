"""Global DNS orchestration with injected, explicitly approved provider clients.

This package coordinates DNS contracts. Concrete provider SDKs and network
transport remain in provider adapters; metadata never implies live access.
"""
from __future__ import annotations

from .registry import list_providers, get_provider
from .models import DNSChangeRequest
from .policies import validate_change_request, ensure_client


class GlobalDNSService:
    def __init__(self, provider_clients=None):
        self.provider_clients = {
            str(key).strip().lower(): value
            for key, value in (provider_clients or {}).items()
        }

    def status(self):
        providers = list_providers()
        for item in providers:
            configured = item["provider_id"] in self.provider_clients
            item["client_configured"] = configured
            # Injection is configuration evidence, not a successful health check.
            item["connection_status"] = (
                "adapter_injected_unverified" if configured else "not_configured"
            )
        return {
            "success": True,
            "ecosystem_id": "GLOBAL-DNS-ECOSYSTEM",
            "layer": "DNS",
            "provider_count": len(providers),
            "live_dns_connectivity_verified": False,
            "providers": providers,
        }

    def list_providers(self):
        return list_providers()

    def get_provider(self, provider_id: str):
        return get_provider(provider_id)

    def list_records(self, provider_id: str, zone_id: str):
        provider_id = provider_id.strip().lower()
        if not zone_id.strip():
            raise ValueError("zone_id is required")
        # Validate provider before resolving its injected adapter.
        get_provider(provider_id)
        client = ensure_client(provider_id, self.provider_clients)
        records = client.list_records(zone_id)
        return {
            "success": True,
            "provider_id": provider_id,
            "zone_id": zone_id,
            "records": records,
            "read_only": True,
            "adapter_call_completed": True,
            "live_connection_verified": False,
        }

    def apply_change(self, request: DNSChangeRequest):
        validate_change_request(request)
        provider_id = request.provider_id.strip().lower()
        get_provider(provider_id)
        client = ensure_client(provider_id, self.provider_clients)
        result = client.apply_change(
            request.zone_id, request.action, request.record.to_dict()
        )
        return {
            "success": True,
            "provider_id": provider_id,
            "zone_id": request.zone_id,
            "action": request.action,
            "result": result,
            "explicit_approval_supplied": True,
            "approval_audit_persisted": False,
        }
