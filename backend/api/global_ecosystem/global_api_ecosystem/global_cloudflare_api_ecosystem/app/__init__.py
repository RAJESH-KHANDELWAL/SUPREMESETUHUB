"""Cloudflare APP provider-owned ecosystem scaffold; catalog-only."""
from .service import get_capabilities, get_status

__all__ = ["get_capabilities", "get_status"]
