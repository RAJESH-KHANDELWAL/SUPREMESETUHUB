"""Compatibility import for the canonical authentication router.

All authentication logic lives in backend.api.auth. Re-exporting the same
router prevents a second, divergent login implementation from being created.
"""

from backend.api.auth import router

__all__ = ["router"]
