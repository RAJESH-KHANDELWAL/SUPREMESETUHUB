"""Capability catalog for platform-wide connection management."""

GLOBAL_CONNECTION_CAPABILITIES = {
    "registration": "Register connection metadata for providers, services, and servers.",
    "authorization_state": "Track authorization state without storing credentials.",
    "adapter_dispatch": "Delegate actual connection operations to explicitly injected adapters.",
    "lifecycle": "Manage connect, disconnect, enable, and disable requests.",
    "health": "Report aggregate connection and adapter health.",
    "secret_safety": "Avoid logging credentials, tokens, or sensitive connection payloads.",
    "namespaces": "Support isolated connection namespaces for platform ecosystems.",
}


def get_global_connection_catalog():
    return {
        "name": "GLOBAL CONNECTION ECOSYSTEM",
        "version": "1.0",
        "capabilities": dict(GLOBAL_CONNECTION_CAPABILITIES),
    }
