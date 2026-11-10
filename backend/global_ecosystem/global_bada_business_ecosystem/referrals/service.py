"""Referral URL utilities for user-supplied Bada Business destinations.

This module builds links only for the allowlisted Bada Business host. It does
not verify referral ownership, calculate commissions, or claim a conversion.
"""
from __future__ import annotations

from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ALLOWED_HOSTS = frozenset({"badabusiness.com", "www.badabusiness.com"})


def normalize_referral_url(url: str, referral_code: str) -> str:
    """Return an allowlisted URL with the supplied referral code in pp_code."""
    if not isinstance(url, str) or not isinstance(referral_code, str):
        raise ValueError("URL and referral code must be strings.")
    parts = urlsplit(url.strip())
    if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
        raise ValueError("Only HTTPS Bada Business URLs are accepted.")
    if parts.username or parts.password or parts.port not in (None, 443):
        raise ValueError("Credentials and non-standard ports are not allowed.")
    code = referral_code.strip()
    if not code or len(code) > 64 or any(ch.isspace() for ch in code):
        raise ValueError("Referral code must be 1 to 64 non-whitespace characters.")
    query = [(key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True) if key != "pp_code"]
    query.append(("pp_code", code))
    return urlunsplit((parts.scheme, parts.netloc, parts.path or "/", urlencode(query), ""))


def extract_referral_code(url: str) -> str | None:
    """Extract pp_code from an allowlisted HTTPS destination."""
    if not isinstance(url, str):
        return None
    parts = urlsplit(url.strip())
    if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
        return None
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        if key == "pp_code" and value:
            return value
    return None
