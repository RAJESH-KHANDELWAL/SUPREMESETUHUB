"""SECURITY-owned provider and defensive capability catalogs."""
from dataclasses import dataclass

@dataclass(frozen=True)
class SecurityProviderDescriptor:
    provider_id: str
    display_name: str
    package: str
    capabilities: tuple[str, ...]
    status: str = "NOT_CONFIGURED"

_PROVIDERS = (
    SecurityProviderDescriptor("apple", "Apple Security", "apple_security_ecosystem", ("identity", "device-security")),
    SecurityProviderDescriptor("aws", "AWS Security", "aws_security_ecosystem", ("identity", "key-management", "posture")),
    SecurityProviderDescriptor("cloudflare", "Cloudflare Security", "cloudflare_security_ecosystem", ("edge-security", "web-application-security")),
    SecurityProviderDescriptor("github", "GitHub Security", "github_security_ecosystem", ("code-security", "dependency-security", "secret-scanning")),
    SecurityProviderDescriptor("google", "Google Security", "google_security_ecosystem", ("identity", "cloud-security", "key-management")),
    SecurityProviderDescriptor("ibm", "IBM Security", "ibm_security_ecosystem", ("identity", "threat-management", "key-management")),
    SecurityProviderDescriptor("microsoft", "Microsoft Security", "microsoft_security_ecosystem", ("identity", "endpoint-security", "cloud-security")),
)

@dataclass(frozen=True)
class SecurityCapability:
    key: str
    description: str
    access: str = "READ_ONLY"

_CAPABILITIES = (
    SecurityCapability("POSTURE.READ", "Read configured security posture and findings"),
    SecurityCapability("AUDIT.READ", "Read authorized audit-event metadata"),
    SecurityCapability("POLICY.VALIDATE", "Validate policy configuration without applying changes"),
    SecurityCapability("PROVIDER.HEALTH", "Inspect an explicitly configured provider health probe"),
)

def list_providers():
    return tuple({"provider_id": p.provider_id, "display_name": p.display_name, "package": p.package, "capabilities": list(p.capabilities), "status": p.status} for p in _PROVIDERS)

def get_provider(provider_id: str):
    key = str(provider_id or "").strip().lower()
    for provider in _PROVIDERS:
        if provider.provider_id == key:
            return provider
    raise KeyError(f"Unknown SECURITY provider: {provider_id}")

def list_capabilities():
    return tuple(_CAPABILITIES)

def get_capability(key: str):
    normalized = str(key or "").strip().upper()
    return next((item for item in _CAPABILITIES if item.key == normalized), None)

__all__ = ["SecurityProviderDescriptor", "SecurityCapability", "list_providers", "get_provider", "list_capabilities", "get_capability"]
