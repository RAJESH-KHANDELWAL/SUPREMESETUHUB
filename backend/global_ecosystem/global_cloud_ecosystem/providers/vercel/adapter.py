"""Injected Vercel deployment handlers; no implicit network calls."""
from typing import Any, Callable
from .config import VercelConfig

class VercelAdapter:
    provider_id = "vercel"
    def __init__(self, config: VercelConfig | None = None, handlers: dict[str, Callable[..., Any]] | None = None):
        self.config = config or VercelConfig.from_env()
        self._handlers = dict(handlers or {})
    def supports(self, operation: str) -> bool:
        return operation in self._handlers
    def execute(self, operation: str, **kwargs: Any) -> Any:
        handler = self._handlers.get(operation)
        if handler is None:
            raise NotImplementedError(f"Vercel operation is not configured: {operation}")
        return handler(config=self.config, **kwargs)
