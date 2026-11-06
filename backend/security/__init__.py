"""Security package exports for SUPREMESETUHUB.

Keep authentication dependencies importable while allowing the security
service facade to live in this package without a module/package name clash.
"""

from backend.security.dependencies import get_current_user, require_admin

__all__ = ["get_current_user", "require_admin"]
