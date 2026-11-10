"""Injected Azure operation handlers; this module performs no network calls."""
from typing import Any, Callable
from .config import AzureConfig

class AzureAdapter:
    provider_id = "microsoft_azure"
    def __init__(self, config: AzureConfig | None = None, handlers: dict[str, Callable[..., Any]] | None = None):
        self.config = config or AzureConfig.from_env()
        self._handlers = dict(handlers or {})
    def supports(self, operation: str) -> bool:
        return operation in self._handlers
    def execute(self, operation: str, **kwargs: Any) -> Any:
        handler = self._handlers.get(operation)
        if handler is None:
            raise NotImplementedError(f"Azure operation is not configured: {operation}")
        return handler(config=self.config, **kwargs)
