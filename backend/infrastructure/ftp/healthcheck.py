"""Read-only explicit-FTPS connectivity checks for registered Hostinger sites.

This module verifies authentication and the account's starting directory only.
It never uploads, deletes, renames, or changes remote files.
Credentials are read from environment variables and are never returned.
"""
from __future__ import annotations

import argparse
import ftplib
import json
import os
import socket
import ssl
from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class FtpTarget:
    """Credentials and non-secret metadata for one FTP account."""

    host: str
    username: str
    password: str = field(repr=False)
    port: int = 21
    timeout: int = 15
    site: str = "unspecified"

    @classmethod
    def from_environment(
        cls,
        environ: Mapping[str, str] | None = None,
        *,
        site: str = "unspecified",
    ) -> "FtpTarget":
        values = os.environ if environ is None else environ
        host = values.get("FTP_SERVER", "").strip()
        username = values.get("FTP_USERNAME", "").strip()
        password = values.get("FTP_PASSWORD", "")
        try:
            port = int(values.get("FTP_PORT", "21"))
            timeout = int(values.get("FTP_TIMEOUT", "15"))
        except ValueError as exc:
            raise ValueError("FTP_PORT and FTP_TIMEOUT must be integers") from exc
        missing = [
            name for name, value in (
                ("FTP_SERVER", host),
                ("FTP_USERNAME", username),
                ("FTP_PASSWORD", password),
            ) if not value
        ]
        if missing:
            raise ValueError("Missing FTP settings: " + ", ".join(missing))
        if not 1 <= port <= 65535:
            raise ValueError("FTP_PORT must be between 1 and 65535")
        if not 1 <= timeout <= 120:
            raise ValueError("FTP_TIMEOUT must be between 1 and 120 seconds")
        return cls(host=host, username=username, password=password,
                   port=port, timeout=timeout, site=site)


def check_ftp_connection(target: FtpTarget) -> dict[str, object]:
    """Verify explicit FTPS login and current-directory access without mutation."""
    client: ftplib.FTP_TLS | None = None
    try:
        context = ssl.create_default_context()
        client = ftplib.FTP_TLS(context=context, timeout=target.timeout)
        client.connect(target.host, target.port, timeout=target.timeout)
        # FTP_TLS.login() performs AUTH TLS automatically after connect.
        client.login(user=target.username, passwd=target.password)
        client.prot_p()
        remote_directory = client.pwd()
        return {
            "success": True,
            "status": "CONNECTED",
            "site": target.site,
            "host": target.host,
            "port": target.port,
            "protocol": "explicit-ftps",
            "authenticated": True,
            "directory_access": True,
            "remote_directory": remote_directory,
            "mutations_performed": False,
            "credentials_returned": False,
        }
    except ftplib.error_perm as exc:
        message = str(exc).strip()
        auth_failed = message.startswith("530")
        return {
            "success": False,
            "status": "AUTHENTICATION_FAILED" if auth_failed else "FTP_PERMISSION_ERROR",
            "site": target.site,
            "host": target.host,
            "port": target.port,
            "protocol": "explicit-ftps",
            "error_code": message.split(" ", 1)[0] if message else "FTP_PERMISSION_ERROR",
            "mutations_performed": False,
            "credentials_returned": False,
        }
    except (socket.timeout, TimeoutError):
        return {
            "success": False, "status": "TIMEOUT", "site": target.site,
            "host": target.host, "port": target.port,
            "mutations_performed": False, "credentials_returned": False,
        }
    except socket.gaierror:
        return {
            "success": False, "status": "DNS_ERROR", "site": target.site,
            "host": target.host, "port": target.port,
            "mutations_performed": False, "credentials_returned": False,
        }
    except (OSError, EOFError, ssl.SSLError, ftplib.Error) as exc:
        return {
            "success": False, "status": "CONNECTION_ERROR", "site": target.site,
            "host": target.host, "port": target.port,
            "error_type": type(exc).__name__,
            "mutations_performed": False, "credentials_returned": False,
        }
    finally:
        if client is not None:
            try:
                client.quit()
            except Exception:
                try:
                    client.close()
                except Exception:
                    pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Hostinger explicit-FTPS health check")
    parser.add_argument("--site", default="unspecified", help="Non-secret site label")
    args = parser.parse_args()
    try:
        target = FtpTarget.from_environment(site=args.site)
    except ValueError as exc:
        print(json.dumps({"success": False, "status": "CONFIGURATION_ERROR", "error": str(exc)}))
        return 2
    result = check_ftp_connection(target)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
