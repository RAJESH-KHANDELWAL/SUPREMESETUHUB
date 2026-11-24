"""Injected Netlify deployment handlers; no implicit network calls."""
from typing import Any, Callable
from .config import NetlifyConfig

class NetlifyAdapter:
    provider_id = "netlify"
    def __init__(self, config: NetlifyConfig | None = None, handlers: dict[str, Callable[..., Any]] | None = None):
        self.config = config or NetlifyConfig.from_env()
        self._handlers = dict(handlers or {})
    def supports(self, operation: str) -> bool:
        return operation in self._handlers
    def execute(self, operation: str, **kwargs: Any) -> Any:
        handler = self._handlers.get(operation)
        if handler is None:
            raise NotImplementedError(f"Netlify operation is not configured: {operation}")
        return handler(config=self.config, **kwargs)
