"""OCI API Request Signature Version 1 signing helpers."""
from __future__ import annotations

import base64
import hashlib
from datetime import datetime, timezone
from email.utils import format_datetime
from urllib.parse import urlsplit

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

from .config import OCIConfig


def sign_request(
    config: OCIConfig,
    method: str,
    url: str,
    body: bytes | None = None,
    headers: dict[str, str] | None = None,
) -> dict[str, str]:
    """Return OCI-signed headers. Caller remains responsible for HTTPS transport."""
    missing = config.validate()
    if missing:
        raise ValueError("OCI configuration missing: " + ", ".join(missing))

    parsed = urlsplit(url)
    if parsed.scheme.lower() != "https" or not parsed.netloc:
        raise ValueError("OCI API requests must use an absolute HTTPS URL")

    request_headers = {k.lower(): v for k, v in (headers or {}).items()}
    request_headers["host"] = parsed.netloc
    request_headers["date"] = format_datetime(datetime.now(timezone.utc), usegmt=True)

    signing_headers = ["(request-target)", "host", "date"]
    signing_lines = [
        f"(request-target): {method.lower()} {parsed.path or '/'}"
        + (f"?{parsed.query}" if parsed.query else ""),
        f"host: {request_headers['host']}",
        f"date: {request_headers['date']}",
    ]

    if body is not None:
        body_hash = base64.b64encode(hashlib.sha256(body).digest()).decode("ascii")
        request_headers["x-content-sha256"] = body_hash
        request_headers["content-type"] = request_headers.get(
            "content-type", "application/json"
        )
        request_headers["content-length"] = str(len(body))
        for name in ("x-content-sha256", "content-type", "content-length"):
            signing_headers.append(name)
            signing_lines.append(f"{name}: {request_headers[name]}")

    private_key = serialization.load_pem_private_key(
        config.load_private_key_pem(),
        password=config.passphrase.encode("utf-8") if config.passphrase else None,
    )
    signature = private_key.sign(
        "\n".join(signing_lines).encode("ascii"),
        padding.PKCS1v15(),
        hashes.SHA256(),
    )
    encoded_signature = base64.b64encode(signature).decode("ascii")
    request_headers["authorization"] = (
        'Signature version="1",'
        f'keyId="{config.key_id}",'
        'algorithm="rsa-sha256",'
        f'headers="{" ".join(signing_headers)}",'
        f'signature="{encoded_signature}"'
    )
    return request_headers
