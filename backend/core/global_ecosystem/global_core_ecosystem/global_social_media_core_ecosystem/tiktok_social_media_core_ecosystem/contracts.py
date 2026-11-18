"""Platform-specific aliases for shared Social Media Core contracts."""
from ..contracts import CoreResult, Readiness, TenantContext

PlatformCoreResult = CoreResult
PlatformTenantContext = TenantContext

__all__ = ["CoreResult", "Readiness", "TenantContext", "PlatformCoreResult", "PlatformTenantContext"]
