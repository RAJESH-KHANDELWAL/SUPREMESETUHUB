# Integrations boundary

Provider-specific SDKs, HTTP clients, webhook verification, payload translation and retries belong in adapter/integration runtime packages—not in this CORE catalog. Keep credentials in an external secret manager and expose only opaque references. No live adapters are implemented by this foundation.
