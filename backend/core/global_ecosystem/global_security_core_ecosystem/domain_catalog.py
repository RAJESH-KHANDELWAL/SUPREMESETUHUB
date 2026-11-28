"""Backward-compatible import path; security registry is owned by manager.py."""
from .manager import domain_summary, get_domain, get_domains

__all__ = ["get_domains", "get_domain", "domain_summary"]
