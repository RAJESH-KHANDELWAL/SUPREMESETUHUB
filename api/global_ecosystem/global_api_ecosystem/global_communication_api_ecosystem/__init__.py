"""Global Communication API Ecosystem package.

Mount `router` from this package in the parent FastAPI application.
The package currently exposes a catalog/status API; provider adapters remain
disabled until official credentials, permissions, webhooks, and tests exist.
"""

from .routes import router

__all__ = ["router"]
