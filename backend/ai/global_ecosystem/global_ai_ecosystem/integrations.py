"""Integration descriptors. A catalog entry does not imply a live connection."""
from .schemas import CatalogRecord

INTEGRATIONS = tuple(
    CatalogRecord(key, name, "integration_type", description)
    for key, name, description in (
        ("provider_adapters", "Provider adapters", "Translate internal requests to provider-specific contracts."),
        ("tool_adapters", "Tool adapters", "Expose approved external tools to agent workflows."),
        ("file_sources", "File sources", "Connect approved file and document repositories."),
        ("business_systems", "Business systems", "Connect CRM, ERP and productivity systems."),
        ("observability", "Observability integrations", "Export traces, metrics and logs."),
        ("identity_systems", "Identity integrations", "Delegate authentication and authorization."),
    )
)
