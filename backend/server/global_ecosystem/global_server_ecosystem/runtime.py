"""Read-only runtime diagnostics for the independent SERVER layer.

This module reports the process hosting this application. It does not provision
cloud resources, open provider connections, or expose environment secrets.
"""
from __future__ import annotations

import os
import platform
import socket
import sys
import time
from datetime import datetime, timezone

_STARTED_AT = time.monotonic()
_STARTED_UTC = datetime.now(timezone.utc).isoformat()


def runtime_status() -> dict:
    """Return safe diagnostics for the current application server process."""
    port_value = os.getenv("PORT", "8000")
    try:
        port = int(port_value)
    except (TypeError, ValueError):
        port = None

    return {
        "service": "MAIN BASE FOUNDATION SERVER",
        "status": "PROCESS_RUNNING",
        "host": "0.0.0.0",
        "port": port,
        "hostname": socket.gethostname(),
        "process_id": os.getpid(),
        "python_version": platform.python_version(),
        "platform": sys.platform,
        "started_at": _STARTED_UTC,
        "uptime_seconds": max(0, int(time.monotonic() - _STARTED_AT)),
        "deployment_environment": os.getenv("RENDER_SERVICE_NAME")
        and "RENDER"
        or ("DOCKER" if os.path.exists("/.dockerenv") else "SELF_HOSTED"),
        "external_provider_connections": "NOT_ATTEMPTED",
    }


__all__ = ["runtime_status"]
