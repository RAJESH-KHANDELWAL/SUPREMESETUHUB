"""Bada Business tenant-to-DNS-provider binding contract."""
from __future__ import annotations
from dataclasses import dataclass
from .catalog import BADA_BUSINESS_DNS_ECOSYSTEM


@dataclass(frozen=True)
class BusinessDomainDNSBinding:
    tenant_id: str
    domain: str
    provider_id: str
    zone_id: str
    enabled: bool = True

    def validate(self):
        if not self.tenant_id.strip():
            raise ValueError("tenant_id is required")
        domain = self.domain.strip().lower().rstrip(".")
        if not domain or "." not in domain or " " in domain:
            raise ValueError("A valid domain name is required")
        provider = self.provider_id.strip().lower()
        if provider not in BADA_BUSINESS_DNS_ECOSYSTEM["supported_dns_providers"]:
            raise ValueError("Unsupported DNS provider for Bada Business domain")
        if not self.zone_id.strip():
            raise ValueError("zone_id is required")
        return self

    @property
    def normalized_domain(self):
        return self.domain.strip().lower().rstrip(".")
