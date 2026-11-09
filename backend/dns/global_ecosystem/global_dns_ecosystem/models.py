"""Provider-neutral DNS contracts. No network operations are implemented here."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

SUPPORTED_RECORD_TYPES = frozenset({"A", "AAAA", "CNAME", "MX", "TXT", "NS", "SRV", "CAA", "PTR"})

@dataclass(frozen=True)
class DNSRecord:
    name: str
    record_type: str
    value: str
    ttl: int = 300
    priority: int | None = None
    proxied: bool | None = None

    def validate(self):
        if not self.name.strip():
            raise ValueError("DNS record name is required")
        kind = self.record_type.strip().upper()
        if kind not in SUPPORTED_RECORD_TYPES:
            raise ValueError("Unsupported DNS record type")
        if not self.value.strip():
            raise ValueError("DNS record value is required")
        if not isinstance(self.ttl, int) or not 60 <= self.ttl <= 86400:
            raise ValueError("ttl must be between 60 and 86400 seconds")
        if self.priority is not None and (not isinstance(self.priority, int) or self.priority < 0):
            raise ValueError("priority must be a non-negative integer")
        return self

    def to_dict(self):
        return {
            "name": self.name.strip().rstrip("."),
            "type": self.record_type.strip().upper(),
            "value": self.value.strip(),
            "ttl": self.ttl,
            "priority": self.priority,
            "proxied": self.proxied,
        }


@dataclass(frozen=True)
class DNSChangeRequest:
    provider_id: str
    zone_id: str
    action: str
    record: DNSRecord
    approved: bool = False

    def validate(self):
        if self.provider_id.strip().lower() not in {"cloudflare", "google", "hostinger", "namecheap", "route53"}:
            raise ValueError("Unsupported DNS provider")
        if not self.zone_id.strip():
            raise ValueError("zone_id is required")
        if self.action not in {"CREATE", "UPDATE", "DELETE"}:
            raise ValueError("Unsupported DNS action")
        self.record.validate()
        return self


class DNSProviderClient:
    """Injected provider client contract; concrete SDK/network code lives elsewhere."""
    provider_id = "unknown"

    def list_records(self, zone_id: str):
        raise NotImplementedError

    def apply_change(self, zone_id: str, action: str, record: dict[str, Any]):
        raise NotImplementedError
