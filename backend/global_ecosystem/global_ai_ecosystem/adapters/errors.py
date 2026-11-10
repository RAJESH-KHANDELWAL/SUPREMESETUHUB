"""Sanitized provider adapter exceptions."""

class ProviderAdapterError(RuntimeError):
    """Base error for adapter failures; never include credentials in messages."""


class ProviderConfigurationError(ProviderAdapterError):
    """Missing or invalid provider configuration."""


class ProviderAuthenticationError(ProviderAdapterError):
    """Provider rejected authentication."""


class ProviderRateLimitError(ProviderAdapterError):
    """Provider rate limit was reached."""


class ProviderRequestError(ProviderAdapterError):
    """Provider rejected a request or returned an invalid response."""


class ProviderTransportError(ProviderAdapterError):
    """Network or transport failure."""
