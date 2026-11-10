"""Typed errors for provider adapter boundaries."""
class AppIntegrationError(RuntimeError):
    """Base error for app integration failures."""
class ProviderNotRegisteredError(AppIntegrationError):
    """Raised when a provider adapter has not been registered."""
class ProviderNotConfiguredError(AppIntegrationError):
    """Raised when required credentials or handlers are unavailable."""
class ProviderRequestError(AppIntegrationError):
    """Raised when a provider request fails."""
__all__ = ["AppIntegrationError", "ProviderNotRegisteredError", "ProviderNotConfiguredError", "ProviderRequestError"]
