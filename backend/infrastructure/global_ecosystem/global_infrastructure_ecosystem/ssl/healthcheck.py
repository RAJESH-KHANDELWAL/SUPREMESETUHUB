"""Read-only TLS certificate inspection for HTTPS services."""
from __future__ import annotations

import socket
import ssl
import time
from typing import Any


def check_tls_certificate(
    hostname: str,
    port: int = 443,
    *,
    timeout: float = 8.0,
    warning_days: int = 30,
) -> dict[str, Any]:
    """Inspect a server certificate using normal CA and hostname verification."""
    host = hostname.strip()
    if not host:
        raise ValueError("hostname is required.")
    if not 1 <= int(port) <= 65535:
        raise ValueError("port must be between 1 and 65535.")
    if not 0 < timeout <= 30:
        raise ValueError("timeout must be greater than 0 and at most 30 seconds.")
    if warning_days < 0:
        raise ValueError("warning_days cannot be negative.")

    started = time.monotonic()
    context = ssl.create_default_context()
    try:
        with socket.create_connection((host, int(port)), timeout=timeout) as raw_socket:
            with context.wrap_socket(raw_socket, server_hostname=host) as tls_socket:
                certificate = tls_socket.getpeercert()
                expiry_text = certificate.get("notAfter")
                if not expiry_text:
                    return {
                        "success": False,
                        "status": "CERTIFICATE_EXPIRY_UNAVAILABLE",
                        "hostname": host,
                        "port": int(port),
                        "mutations_performed": False,
                    }
                expiry_epoch = ssl.cert_time_to_seconds(expiry_text)
                days_remaining = int((expiry_epoch - time.time()) // 86400)
                if days_remaining < 0:
                    status = "EXPIRED"
                    success = False
                elif days_remaining <= warning_days:
                    status = "EXPIRING_SOON"
                    success = True
                else:
                    status = "VALID"
                    success = True
                return {
                    "success": success,
                    "status": status,
                    "hostname": host,
                    "port": int(port),
                    "days_remaining": days_remaining,
                    "not_after": expiry_text,
                    "tls_version": tls_socket.version(),
                    "elapsed_ms": round((time.monotonic() - started) * 1000, 2),
                    "certificate_chain_verified": True,
                    "mutations_performed": False,
                }
    except (OSError, ssl.SSLError, TimeoutError) as exc:
        return {
            "success": False,
            "status": "TLS_CHECK_FAILED",
            "hostname": host,
            "port": int(port),
            "error_type": type(exc).__name__,
            "elapsed_ms": round((time.monotonic() - started) * 1000, 2),
            "mutations_performed": False,
        }


__all__ = ["check_tls_certificate"]
