"""Offline contract tests for provider service package wiring."""
import pytest

from global_cloudflare_ecosystem.dns import DNSService
from global_cloudflare_ecosystem.cdn import CDNService
from global_cloudflare_ecosystem.workers import WorkersService
from global_cloudflare_ecosystem.pages import PagesService
from global_cloudflare_ecosystem.r2 import R2Service
from global_cloudflare_ecosystem.d1 import D1Service
from global_cloudflare_ecosystem.zero_trust import ZeroTrustService
from global_cloudflare_ecosystem.security import SecurityService
from global_cloudflare_ecosystem.observability import ObservabilityService


class FakeClient:
    def __init__(self):
        self.calls = []

    def __getattr__(self, name):
        def call(*args, **kwargs):
            self.calls.append((name, args, kwargs))
            return {"success": True, "result": []}
        return call


@pytest.mark.parametrize(
    "service_type,method,args",
    [
        (DNSService, "list_zones", ()),
        (CDNService, "get_zone", ("zone-1",)),
        (WorkersService, "list_scripts", ("account-1",)),
        (PagesService, "list_projects", ("account-1",)),
        (R2Service, "list_buckets", ("account-1",)),
        (D1Service, "list_databases", ("account-1",)),
        (ZeroTrustService, "list_access_apps", ("account-1",)),
        (SecurityService, "list_zone_rulesets", ("zone-1",)),
    ],
)
def test_service_delegates_to_client(service_type, method, args):
    fake = FakeClient()
    result = getattr(service_type(fake), method)(*args)
    assert result["success"] is True
    assert len(fake.calls) == 1


def test_observability_requires_time_window():
    with pytest.raises(ValueError, match="since and until"):
        ObservabilityService(FakeClient()).zone_analytics("zone-1", since="", until="")
