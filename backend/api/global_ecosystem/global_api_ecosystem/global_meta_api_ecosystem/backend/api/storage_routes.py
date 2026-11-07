"""Authenticated HTTP APIs for the foundation engines and persistent file storage."""
from __future__ import annotations

from pathlib import Path
import re

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse

from backend.core.readiness import CoreReadinessService
from backend.database.service import DatabaseService
from backend.engines.storage import StorageEngine
from backend.security.dependencies import get_current_user
from backend.storage.filesystem import LocalFileStorage

router = APIRouter(tags=["MAIN BASE FOUNDATION APIs"])
MAX_UPLOAD_BYTES = 10 * 1024 * 1024


def _actor_id(current_user: dict) -> str:
    value = str(current_user.get("user_id", "")).strip()
    if not value:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")
    return value


@router.get("/api/v1/engines/status")
def engines_status(current_user: dict = Depends(get_current_user)):
    snapshot = CoreReadinessService().snapshot()
    storage = StorageEngine()
    return {
        "success": True,
        "core": snapshot["core"],
        "overall": snapshot["overall"],
        "database": snapshot["components"]["database"],
        "storage": snapshot["components"]["storage"],
        "engines": {
            "database": "READY" if snapshot["components"]["database"]["status"] == "READY" else "UNAVAILABLE",
            "storage": storage.status()["status"],
        },
    }


@router.get("/api/v1/database/health")
def database_health(current_user: dict = Depends(get_current_user)):
    health = DatabaseService().health()
    return {
        "success": True,
        "database": health.get("database", "SQLITE"),
        "healthy": bool(health.get("healthy")),
        "connected": bool(health.get("connected")),
    }


@router.get("/api/v1/storage/health")
def storage_health(current_user: dict = Depends(get_current_user)):
    engine = StorageEngine()
    engine.connect()
    return {"success": True, **engine.health()}


@router.get("/api/v1/storage/configuration")
def storage_configuration(current_user: dict = Depends(get_current_user)):
    return {"success": True, **StorageEngine().configuration()}


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
    storage = LocalFileStorage()
    if not storage.health()["writable"]:
        raise HTTPException(status_code=503, detail="STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")

    content = await file.read(MAX_UPLOAD_BYTES + 1)
    await file.close()
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="MAX_UPLOAD_SIZE_IS_10_MB")
    if not content:
        raise HTTPException(status_code=422, detail="EMPTY_FILE_NOT_ALLOWED")

    storage_key = None
    try:
        storage_key = storage.save_bytes(content, filename)
        asset = StorageEngine().register_asset(
            owner_id=actor,
            area_id=area,
            title=filename,
            asset_type="FILE",
            mime_type=file.content_type or "application/octet-stream",
            storage_key=storage_key,
            metadata={"size_bytes": len(content), "storage_backend": "LOCAL_FILESYSTEM"},
        )
    except RuntimeError as exc:
        if storage_key:
            storage.delete(storage_key)
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        if storage_key:
            storage.delete(storage_key)
        raise HTTPException(status_code=500, detail="STORAGE_REGISTRATION_FAILED") from exc

    return {
        "success": True,
        "data": {
            "asset_id": asset["asset_id"],
            "title": asset["title"],
            "size_bytes": len(content),
            "storage_backend": "LOCAL_FILESYSTEM",
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
    storage = LocalFileStorage()
    try:
        path = storage.resolve(storage_key)
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(status_code=503, detail="STORAGE_BACKEND_NOT_CONFIGURED") from exc
    if not path.is_file():
        raise HTTPException(status_code=404, detail="PHYSICAL_FILE_NOT_FOUND")
    filename = Path(str(asset.get("title") or "download.bin")).name
    return FileResponse(
        path=path,
        filename=filename,
        media_type="application/octet-stream",
        headers={"X-Content-Type-Options": "nosniff", "Cache-Control": "private, no-store"},
    )
