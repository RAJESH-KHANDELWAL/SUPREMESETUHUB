"""Read-only TCP reachability checks for registered infrastructure servers."""
from __future__ import annotations

import socket
import time
from typing import Any


def check_tcp_port(host: str, port: int, *, timeout: float = 5.0) -> dict[str, Any]:
    """Check whether a TCP port accepts a connection; no login or commands are sent."""
    hostname = host.strip()
    if not hostname:
        raise ValueError("host is required.")
    if not 1 <= int(port) <= 65535:
        raise ValueError("port must be between 1 and 65535.")
    if not 0 < timeout <= 30:
        raise ValueError("timeout must be greater than 0 and at most 30 seconds.")

    started = time.monotonic()
    try:
        with socket.create_connection((hostname, int(port)), timeout=timeout):
            return {
                "success": True,
                "status": "REACHABLE",
                "host": hostname,
                "port": int(port),
                "elapsed_ms": round((time.monotonic() - started) * 1000, 2),
                "authentication_attempted": False,
                "commands_executed": False,
                "mutations_performed": False,
            }
    except (socket.timeout, TimeoutError):
        status = "TIMEOUT"
    except OSError as exc:
        status = "CONNECTION_ERROR"
        error_type = type(exc).__name__
    result = {
        "success": False,
        "status": status,
        "host": hostname,
        "port": int(port),
        "elapsed_ms": round((time.monotonic() - started) * 1000, 2),
        "authentication_attempted": False,
        "commands_executed": False,
        "mutations_performed": False,
    }
    if status == "CONNECTION_ERROR":
        result["error_type"] = error_type
    return result


__all__ = ["check_tcp_port"]
