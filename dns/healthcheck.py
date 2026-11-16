"""Read-only system-resolver checks for domain names."""
from __future__ import annotations

import socket
from typing import Any


def resolve_domain(hostname: str) -> dict[str, Any]:
    """Resolve a hostname using the operating system resolver.

    This confirms resolver visibility only; it does not inspect or modify the
    authoritative DNS zone at the registrar or DNS provider.
    """
    name = hostname.strip().rstrip(".")
    if not name or any(char.isspace() for char in name):
        raise ValueError("A valid hostname is required.")
    try:
        results = socket.getaddrinfo(name, None, type=socket.SOCK_STREAM)
        addresses = sorted({item[4][0] for item in results})
        return {
            "success": bool(addresses),
            "status": "RESOLVED" if addresses else "NO_RECORDS",
            "hostname": name,
            "addresses": addresses,
            "resolver": "SYSTEM",
            "authoritative_dns_verified": False,
            "mutations_performed": False,
        }
    except socket.gaierror as exc:
        return {
            "success": False,
            "status": "RESOLUTION_FAILED",
            "hostname": name,
            "error_type": type(exc).__name__,
            "resolver": "SYSTEM",
            "authoritative_dns_verified": False,
            "mutations_performed": False,
        }


__all__ = ["resolve_domain"]
