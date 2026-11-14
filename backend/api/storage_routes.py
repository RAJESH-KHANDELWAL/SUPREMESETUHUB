"""Authenticated HTTP APIs for the foundation engines and physical storage."""
from __future__ import annotations

import json
from pathlib import Path
import re
from urllib.parse import quote
from starlette.background import BackgroundTask

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from backend.core.readiness import CoreReadinessService
from backend.database.service import DatabaseService
from backend.engine.storage import StorageEngine
from backend.security.dependencies import get_current_user
from backend.storage.global_ecosystem.global_storage_ecosystem.provider_runtime import StorageProviderRuntime

router = APIRouter(tags=["MAIN BASE FOUNDATION APIs"])
MAX_UPLOAD_BYTES = 10 * 1024 * 1024


def _actor_id(current_user: dict) -> str:
    value = str(current_user.get("user_id", "")).strip()
    if not value:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")
    return value


def _runtime(provider_id: str | None = None) -> StorageProviderRuntime:
    try:
        return StorageProviderRuntime(provider_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="UNSUPPORTED_STORAGE_PROVIDER") from exc


@router.get("/api/v1/engines/status")
def engines_status(current_user: dict = Depends(get_current_user)):
    snapshot = CoreReadinessService().snapshot()
    storage = StorageEngine()
    runtime = _runtime().status()
    return {
        "success": True, "core": snapshot["core"], "overall": snapshot["overall"],
        "database": snapshot["components"]["database"],
        "storage": snapshot["components"]["storage"],
        "engines": {
            "database": "READY" if snapshot["components"]["database"]["status"] == "READY" else "UNAVAILABLE",
            "storage": storage.status()["status"],
        },
        "physical_storage": runtime,
    }


@router.get("/api/v1/database/health")
def database_health(current_user: dict = Depends(get_current_user)):
    health = DatabaseService().health()
    return {
        "success": True, "database": health.get("database", "SQLITE"),
        "healthy": bool(health.get("healthy")), "connected": bool(health.get("connected")),
    }


@router.get("/api/v1/storage/health")
def storage_health(current_user: dict = Depends(get_current_user)):
    engine = StorageEngine()
    engine.connect()
    return {"success": True, **engine.health(), "physical_storage": _runtime().status()}


@router.get("/api/v1/storage/configuration")
def storage_configuration(current_user: dict = Depends(get_current_user)):
    return {
        "success": True, **StorageEngine().configuration(),
        "physical_storage": _runtime().status(),
        "available_physical_providers": StorageProviderRuntime.available_providers(),
    }


@router.get("/api/v1/storage/ecosystem/providers")
def storage_ecosystem_providers(current_user: dict = Depends(get_current_user)):
    return {
        "success": True,
        "count": len(StorageProviderRuntime.available_providers()),
        "selected_provider": _runtime().status(),
        "providers": StorageProviderRuntime.available_providers(),
        "note": "Only Local Filesystem and AWS S3 have executable physical adapters in this runtime. Other catalog providers remain unimplemented.",
    }


@router.get("/api/v1/storage/ecosystem/status")
def storage_ecosystem_status(current_user: dict = Depends(get_current_user)):
    engine = StorageEngine()
    runtime = _runtime().status()
    return {
        "success": True,
        "ecosystem": "GLOBAL STORAGE ECOSYSTEM",
        "status": "WRITE_READY" if runtime["write_verified"] else "DEGRADED",
        "metadata_engine": engine.health(),
        "physical_provider": runtime,
        "provider_count_implemented": len(StorageProviderRuntime.available_providers()),
        "provider_count_catalog_only": True,
    }


@router.post("/api/v1/storage/files", status_code=201)
async def upload_storage_file(
    file: UploadFile = File(...),
    area_id: str = Form(default="personal"),
    current_user: dict = Depends(get_current_user),
):
    actor = _actor_id(current_user)
    area = str(area_id or "").strip()
    if not area or len(area) > 80:
        raise HTTPException(status_code=422, detail="AREA_ID_MUST_BE_1_TO_80_CHARACTERS")

    filename = Path(str(file.filename or "upload.bin")).name
    filename = re.sub(r"[^A-Za-z0-9._ -]", "_", filename).strip(" .")[:180] or "upload.bin"
    content = await file.read(MAX_UPLOAD_BYTES + 1)
    await file.close()
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="MAX_UPLOAD_SIZE_IS_10_MB")
    if not content:
        raise HTTPException(status_code=422, detail="EMPTY_FILE_NOT_ALLOWED")

    runtime = _runtime()
    stored = None
    try:
        from io import BytesIO
        stored = runtime.store_stream(
            BytesIO(content), owner_id=actor, area_id=area,
            filename=filename, max_bytes=MAX_UPLOAD_BYTES,
        )
        asset = StorageEngine().register_asset(
            owner_id=actor, area_id=area, title=filename, asset_type="FILE",
            mime_type=file.content_type or "application/octet-stream",
            storage_key=stored["storage_key"],
            metadata={
                "size_bytes": stored["size_bytes"], "checksum_sha256": stored["checksum"],
                "storage_backend": stored["storage_backend"],
                "storage_provider": stored["storage_provider"],
            },
        )
    except ValueError as exc:
        if stored:
            runtime.delete_key(stored["storage_key"])
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except RuntimeError as exc:
        if stored:
            runtime.delete_key(stored["storage_key"])
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        if stored:
            runtime.delete_key(stored["storage_key"])
        raise HTTPException(status_code=500, detail="STORAGE_REGISTRATION_FAILED") from exc

    return {
        "success": True,
        "data": {
            "asset_id": asset["asset_id"], "title": asset["title"],
            "size_bytes": stored["size_bytes"], "checksum_sha256": stored["checksum"],
            "storage_backend": stored["storage_backend"],
            "storage_provider": stored["storage_provider"],
            "download_endpoint": f"/api/v1/storage/files/{asset['asset_id']}",
        },
    }


@router.get("/api/v1/storage/assets/{asset_id}")
def get_storage_asset(asset_id: str, current_user: dict = Depends(get_current_user)):
    actor = _actor_id(current_user)
    try:
        asset = StorageEngine().get_asset(asset_id, actor_id=actor, action="VIEW")
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail="ASSET_ACCESS_DENIED") from exc
    if asset is None:
        raise HTTPException(status_code=404, detail="ASSET_NOT_FOUND")
    safe = {key: value for key, value in asset.items() if key not in {"storage_key", "file_url"}}
    return {"success": True, "data": safe}


@router.get("/api/v1/storage/files/{asset_id}")
def download_storage_file(asset_id: str, current_user: dict = Depends(get_current_user)):
    actor = _actor_id(current_user)
    try:
        asset = StorageEngine().get_asset(asset_id, actor_id=actor, action="DOWNLOAD")
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail="ASSET_ACCESS_DENIED") from exc
    if asset is None:
        raise HTTPException(status_code=404, detail="ASSET_NOT_FOUND")
    storage_key = asset.get("storage_key")
    if not storage_key:
        raise HTTPException(status_code=404, detail="PHYSICAL_FILE_NOT_FOUND")

    metadata = asset.get("metadata") or {}
    if isinstance(metadata, str):
        try:
            metadata = json.loads(metadata)
        except (TypeError, ValueError):
            metadata = {}
    backend_name = metadata.get("storage_backend", "LOCAL_FILESYSTEM") if isinstance(metadata, dict) else "LOCAL_FILESYSTEM"
    runtime = _runtime(backend_name)
    try:
        if not runtime.exists_key(storage_key):
            raise HTTPException(status_code=404, detail="PHYSICAL_FILE_NOT_FOUND")
        handle = runtime.open_key(storage_key)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="PHYSICAL_FILE_NOT_FOUND") from exc
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(status_code=503, detail="STORAGE_BACKEND_UNAVAILABLE") from exc

    filename = Path(str(asset.get("title") or "download.bin")).name
    headers = {
        "Content-Disposition": "attachment; filename*=UTF-8''" + quote(filename),
        "X-Content-Type-Options": "nosniff",
        "Cache-Control": "private, no-store",
    }
    return StreamingResponse(
        iter(lambda: handle.read(1024 * 1024), b""),
        media_type="application/octet-stream", headers=headers,
        background=BackgroundTask(handle.close),
    )
