"""First-party SUPREMESETUHUB WordPress update server.

Release packages are stored outside the source tree. Configure persistent storage,
SUPREME_UPDATE_ADMIN_TOKEN, and SUPREME_UPDATE_SIGNING_SECRET in production.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import re
import secrets
import time
import zipfile
from pathlib import Path
from typing import Any
from urllib.parse import quote

from fastapi import APIRouter, File, Form, Header, HTTPException, UploadFile
from fastapi.responses import FileResponse

router = APIRouter(prefix="/api/v1/supreme-updates", tags=["SUPREME UPDATE SERVER"])

PLUGINS = {
    "supremesetuhub": {
        "name": "SUPREMESETUHUB",
        "main_file": "supremesetuhub/supremesetuhub.php",
        "slug": "supremesetuhub",
    },
    "dr-rajesh-khandelwal-ibc": {
        "name": "DR RAJESH KHANDELWAL IBC",
        "main_file": "dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php",
        "slug": "dr-rajesh-khandelwal-ibc",
    },
}
MAX_PACKAGE_BYTES = 50 * 1024 * 1024
VERSION_RE = re.compile(r"^\\d+\\.\\d+\\.\\d+(?:[-+][0-9A-Za-z.-]+)?$")
STORAGE_ROOT = Path(os.getenv("SUPREME_UPDATE_STORAGE_DIR", "/var/data/supreme-updates")).resolve()


def _release_path(slug: str) -> Path:
    return STORAGE_ROOT / slug / "release.json"


def _load_release(slug: str) -> dict[str, Any] | None:
    path = _release_path(slug)
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        raise HTTPException(status_code=503, detail="UPDATE_REGISTRY_UNAVAILABLE")
    if not isinstance(data, dict) or data.get("slug") != slug:
        raise HTTPException(status_code=503, detail="UPDATE_REGISTRY_INVALID")
    return data


def _admin_authorized(authorization: str | None) -> None:
    expected = os.getenv("SUPREME_UPDATE_ADMIN_TOKEN", "")
    if not expected:
        raise HTTPException(status_code=503, detail="UPDATE_ADMIN_NOT_CONFIGURED")
    supplied = (authorization or "").removeprefix("Bearer ").strip()
    if not supplied or not hmac.compare_digest(supplied, expected):
        raise HTTPException(status_code=401, detail="UPDATE_ADMIN_UNAUTHORIZED")


def _signing_secret() -> bytes:
    secret = os.getenv("SUPREME_UPDATE_SIGNING_SECRET", "")
    if len(secret) < 32:
        raise HTTPException(status_code=503, detail="UPDATE_SIGNING_SECRET_NOT_CONFIGURED")
    return secret.encode("utf-8")


def _download_token(slug: str, version: str, expires: int) -> str:
    payload = f"{slug}:{version}:{expires}".encode("utf-8")
    return hmac.new(_signing_secret(), payload, hashlib.sha256).hexdigest()


def _verify_download_token(slug: str, version: str, expires: int, token: str) -> bool:
    if expires < int(time.time()) or expires > int(time.time()) + 3600:
        return False
    expected = _download_token(slug, version, expires)
    return hmac.compare_digest(expected, token)


def _safe_zip(archive_path: Path, expected_main_file: str) -> None:
    try:
        with zipfile.ZipFile(archive_path) as archive:
            names = archive.namelist()
            if expected_main_file not in names:
                raise HTTPException(status_code=422, detail="PLUGIN_MAIN_FILE_MISSING_FROM_PACKAGE")
            for name in names:
                candidate = Path(name)
                if candidate.is_absolute() or ".." in candidate.parts:
                    raise HTTPException(status_code=422, detail="UNSAFE_PACKAGE_PATH")
            bad_member = archive.testzip()
            if bad_member:
                raise HTTPException(status_code=422, detail="PACKAGE_ZIP_CORRUPTED")
    except zipfile.BadZipFile:
        raise HTTPException(status_code=422, detail="INVALID_ZIP_PACKAGE")


@router.get("/health")
def update_server_health():
    configured = bool(
        os.getenv("SUPREME_UPDATE_ADMIN_TOKEN")
        and len(os.getenv("SUPREME_UPDATE_SIGNING_SECRET", "")) >= 32
    )
    return {
        "service": "SUPREME UPDATE SERVER",
        "status": "ready" if configured else "configuration_required",
        "registered_plugins": list(PLUGINS),
        "storage_directory_configured": bool(os.getenv("SUPREME_UPDATE_STORAGE_DIR")),
        "persistent_storage_required": True,
        "secrets_configured": configured,
    }


@router.get("/check/{slug}")
def check_for_update(slug: str, installed_version: str) -> dict[str, Any]:
    if slug not in PLUGINS:
        raise HTTPException(status_code=404, detail="UNKNOWN_PLUGIN")
    if not VERSION_RE.fullmatch(installed_version):
        raise HTTPException(status_code=400, detail="INVALID_INSTALLED_VERSION")
    release = _load_release(slug)
    if not release:
        return {"success": True, "plugin": slug, "update_available": False}
    latest = str(release.get("version", ""))
    if not VERSION_RE.fullmatch(latest):
        raise HTTPException(status_code=503, detail="INVALID_RELEASE_VERSION")
    # WordPress/PHP version_compare semantics are used by the plugin client;
    # the server returns metadata and lets the client compare versions.
    expires = int(time.time()) + 900
    token = _download_token(slug, latest, expires)
    return {
        "success": True,
        "plugin": slug,
        "name": PLUGINS[slug]["name"],
        "installed_version": installed_version,
        "latest_version": latest,
        "update_available": latest != installed_version,
        "requires": release.get("requires", "5.8"),
        "requires_php": release.get("requires_php", "7.4"),
        "tested": release.get("tested", ""),
        "homepage": release.get("homepage", ""),
        "notes": release.get("notes", ""),
        "package": f"/api/v1/supreme-updates/download/{slug}/{quote(latest)}?expires={expires}&token={token}",
        "sha256": release.get("sha256"),
        "package_size": release.get("package_size"),
        "published_at": release.get("published_at"),
    }


@router.get("/download/{slug}/{version}")
def download_package(slug: str, version: str, expires: int, token: str):
    if slug not in PLUGINS:
        raise HTTPException(status_code=404, detail="UNKNOWN_PLUGIN")
    if not VERSION_RE.fullmatch(version) or not _verify_download_token(slug, version, expires, token):
        raise HTTPException(status_code=403, detail="DOWNLOAD_TOKEN_INVALID_OR_EXPIRED")
    release = _load_release(slug)
    if not release or release.get("version") != version:
        raise HTTPException(status_code=404, detail="PACKAGE_NOT_FOUND")
    package_path = (STORAGE_ROOT / slug / str(release.get("package_file", ""))).resolve()
    if STORAGE_ROOT not in package_path.parents or not package_path.is_file():
        raise HTTPException(status_code=404, detail="PACKAGE_NOT_FOUND")
    response = FileResponse(
        package_path,
        media_type="application/zip",
        filename=f"{slug}-{version}.zip",
        headers={"Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff"},
    )
    return response


@router.post("/admin/publish/{slug}")
async def publish_release(
    slug: str,
    version: str = Form(...),
    notes: str = Form(""),
    requires: str = Form("5.8"),
    requires_php: str = Form("7.4"),
    tested: str = Form(""),
    homepage: str = Form(""),
    package: UploadFile = File(...),
    authorization: str | None = Header(default=None),
):
    _admin_authorized(authorization)
    if slug not in PLUGINS:
        raise HTTPException(status_code=404, detail="UNKNOWN_PLUGIN")
    if not VERSION_RE.fullmatch(version):
        raise HTTPException(status_code=422, detail="INVALID_RELEASE_VERSION")
    if not package.filename or not package.filename.lower().endswith(".zip"):
        raise HTTPException(status_code=415, detail="ZIP_PACKAGE_REQUIRED")

    payload = await package.read(MAX_PACKAGE_BYTES + 1)
    if not payload or len(payload) > MAX_PACKAGE_BYTES:
        raise HTTPException(status_code=413, detail="PACKAGE_SIZE_LIMIT_EXCEEDED")

    plugin_dir = STORAGE_ROOT / slug
    plugin_dir.mkdir(parents=True, exist_ok=True)
    safe_version = re.sub(r"[^0-9A-Za-z.+-]", "", version)
    package_name = f"{slug}-{safe_version}.zip"
    final_path = plugin_dir / package_name
    temporary_path = plugin_dir / f".{package_name}.{secrets.token_hex(6)}.tmp"
    try:
        temporary_path.write_bytes(payload)
        _safe_zip(temporary_path, PLUGINS[slug]["main_file"])
        digest = hashlib.sha256(payload).hexdigest()
        os.replace(temporary_path, final_path)
        release = {
            "slug": slug,
            "name": PLUGINS[slug]["name"],
            "version": version,
            "package_file": package_name,
            "package_size": len(payload),
            "sha256": digest,
            "notes": notes[:20000],
            "requires": requires[:32],
            "requires_php": requires_php[:32],
            "tested": tested[:32],
            "homepage": homepage[:500],
            "published_at": int(time.time()),
        }
        registry_tmp = plugin_dir / ".release.json.tmp"
        registry_tmp.write_text(json.dumps(release, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(registry_tmp, _release_path(slug))
    finally:
        if temporary_path.exists():
            temporary_path.unlink(missing_ok=True)

    return {
        "success": True,
        "message": "RELEASE_PUBLISHED",
        "plugin": slug,
        "version": version,
        "sha256": digest,
        "package_size": len(payload),
    }
