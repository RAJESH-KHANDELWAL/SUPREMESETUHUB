"""Capability catalog for platform-wide configuration management."""

GLOBAL_CONFIG_CAPABILITIES = {
    "application_metadata": "Application identity, version, and lifecycle metadata.",
    "environment_settings": "Environment-aware configuration defaults and overrides.",
    "configuration_sources": "Explicit mapping and environment-variable configuration sources.",
    "validation": "Required-key and value validation before configuration is consumed.",
    "secret_protection": "Redaction of secret-like values from diagnostic snapshots.",
    "namespaces": "Isolated configuration namespaces for platform ecosystems.",
    "diagnostics": "Safe configuration status and source diagnostics.",
}


def get_global_config_catalog():
    return {"name": "GLOBAL CONFIG ECOSYSTEM", "version": "1.0", "capabilities": dict(GLOBAL_CONFIG_CAPABILITIES)}
