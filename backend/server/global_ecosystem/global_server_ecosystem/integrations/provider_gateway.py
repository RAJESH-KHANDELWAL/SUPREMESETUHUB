"""SERVER-owned gateway for configured provider adapters."""
class ServerProviderGateway:
    def __init__(self, provider_registry):
        self._providers = provider_registry

    def describe(self, provider_id: str):
        provider = self._providers.get(provider_id)
        if provider is None:
            raise RuntimeError(f"SERVER provider is not configured: {provider_id}")
        return provider.describe()

    def health(self, provider_id: str):
        provider = self._providers.get(provider_id)
        if provider is None:
            return {"provider_id": str(provider_id), "status": "NOT_CONFIGURED"}
        method = getattr(provider, "health", None)
        if not callable(method):
            raise TypeError("SERVER provider adapter must implement health()")
        result = method()
        if not isinstance(result, dict):
            raise TypeError("SERVER provider health() must return a dictionary")
        return result

    def execute(self, provider_id: str, operation: str, payload=None):
        provider = self._providers.get(provider_id)
        if provider is None:
            raise RuntimeError(f"SERVER provider is not configured: {provider_id}")
        method = getattr(provider, "execute", None)
        if not callable(method):
            raise TypeError("SERVER provider adapter must implement execute()")
        result = method(operation, dict(payload or {}))
        if result is not None and not isinstance(result, dict):
            raise TypeError("SERVER provider execute() must return a dictionary or None")
        return dict(result or {})

__all__ = ["ServerProviderGateway"]
