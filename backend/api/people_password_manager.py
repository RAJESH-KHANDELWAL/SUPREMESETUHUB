"""People-facing password manager API.

Security model:
- Each vault belongs to the authenticated platform user.
- The server stores only a validated encrypted vault envelope, never plaintext entries.
- Client-side encryption/decryption must happen before data reaches these routes.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict, Field, field_validator

from backend.database.service import DatabaseService
from backend.security.dependencies import get_current_user

router = APIRouter(prefix="/api/v1/people-password-manager", tags=["People Password Manager"])
_db = DatabaseService()
_MAX_ENVELOPE_BYTES = 2 * 1024 * 1024

PLATFORM_CATALOG = [
    {"id": "linksetu", "name": "LinkSetu", "purpose": "links, profiles and social identities"},
    {"id": "websetu", "name": "WebSetu", "purpose": "websites, domains and web accounts"},
    {"id": "codesetu", "name": "CodeSetu", "purpose": "developer accounts, repositories and code services"},
    {"id": "linkhub", "name": "LinkHub", "purpose": "link collections and link profiles"},
    {"id": "webhub", "name": "WebHub", "purpose": "website and web-service account records"},
    {"id": "codehub", "name": "CodeHub", "purpose": "code-hosting and developer account records"},
    {"id": "webpress", "name": "WebPress", "purpose": "publishing and CMS accounts, including WordPress"},
    {"id": "codepress", "name": "CodePress", "purpose": "code publishing and project credentials"},
    {"id": "linkpress", "name": "LinkPress", "purpose": "link publishing and link management"},
]

def _ensure_table() -> None:
    _db.execute("""CREATE TABLE IF NOT EXISTS people_password_vaults (
        user_id TEXT PRIMARY KEY, encrypted_envelope TEXT NOT NULL,
        created_at TEXT NOT NULL, updated_at TEXT NOT NULL)""")

class EncryptedVaultEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid")
    format: str = Field(min_length=1, max_length=64)
    version: int = Field(ge=1, le=10)
    kdf: str = Field(min_length=1, max_length=80)
    cipher: str = Field(min_length=1, max_length=80)
    salt: str = Field(min_length=1, max_length=256)
    iv: str = Field(min_length=1, max_length=256)
    ciphertext: str = Field(min_length=1, max_length=_MAX_ENVELOPE_BYTES)

    @field_validator("format")
    @classmethod
    def validate_format(cls, value: str) -> str:
        if value != "SUPREME-ENCRYPTED-VAULT":
            raise ValueError("UNSUPPORTED_VAULT_FORMAT")
        return value

    @field_validator("kdf")
    @classmethod
    def validate_kdf(cls, value: str) -> str:
        if value != "PBKDF2-SHA256-600000":
            raise ValueError("UNSUPPORTED_KEY_DERIVATION")
        return value

    @field_validator("cipher")
    @classmethod
    def validate_cipher(cls, value: str) -> str:
        if value != "AES-256-GCM":
            raise ValueError("UNSUPPORTED_VAULT_CIPHER")
        return value

class SaveVaultRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    envelope: EncryptedVaultEnvelope

def _user_id(current_user: dict[str, Any]) -> str:
    value = str(current_user.get("user_id") or "").strip()
    if not value:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")
    return value

@router.get("/status")
def password_manager_status(current_user: dict[str, Any] = Depends(get_current_user)):
    _user_id(current_user)
    return {"success": True, "service": "PEOPLE_PASSWORD_MANAGER",
            "status": "AUTHENTICATED_ENCRYPTED_VAULT_API",
            "storage": "PER_USER_ENCRYPTED_ENVELOPE_ONLY",
            "server_can_decrypt": False, "plaintext_credentials_stored": False,
            "platforms": [item["id"] for item in PLATFORM_CATALOG]}

@router.get("/platforms")
def password_manager_platforms(current_user: dict[str, Any] = Depends(get_current_user)):
    _user_id(current_user)
    return {"success": True, "platforms": PLATFORM_CATALOG}

@router.get("/vault")
def get_vault(current_user: dict[str, Any] = Depends(get_current_user)):
    user_id = _user_id(current_user)
    _ensure_table()
    row = _db.fetchone("SELECT encrypted_envelope, created_at, updated_at FROM people_password_vaults WHERE user_id = ?", (user_id,))
    if row is None:
        return {"success": True, "exists": False, "envelope": None}
    try:
        envelope = json.loads(row["encrypted_envelope"])
    except (TypeError, json.JSONDecodeError):
        raise HTTPException(status_code=500, detail="VAULT_ENVELOPE_CORRUPT") from None
    return {"success": True, "exists": True, "envelope": envelope,
            "created_at": row["created_at"], "updated_at": row["updated_at"]}

@router.put("/vault")
def save_vault(request: SaveVaultRequest, current_user: dict[str, Any] = Depends(get_current_user)):
    user_id = _user_id(current_user)
    _ensure_table()
    serialized = json.dumps(request.envelope.model_dump(), separators=(",", ":"), ensure_ascii=True)
    if len(serialized.encode("utf-8")) > _MAX_ENVELOPE_BYTES:
        raise HTTPException(status_code=413, detail="ENCRYPTED_VAULT_TOO_LARGE")
    now = datetime.now(timezone.utc).isoformat()
    row = _db.fetchone("SELECT created_at FROM people_password_vaults WHERE user_id = ?", (user_id,))
    created_at = str(row["created_at"]) if row else now
    _db.execute("""INSERT INTO people_password_vaults (user_id, encrypted_envelope, created_at, updated_at)
        VALUES (?, ?, ?, ?) ON CONFLICT(user_id) DO UPDATE SET
        encrypted_envelope = excluded.encrypted_envelope, updated_at = excluded.updated_at""",
        (user_id, serialized, created_at, now))
    return {"success": True, "saved": True, "created_at": created_at, "updated_at": now,
            "storage": "ENCRYPTED_ENVELOPE_ONLY", "server_can_decrypt": False}

@router.delete("/vault")
def delete_vault(current_user: dict[str, Any] = Depends(get_current_user)):
    user_id = _user_id(current_user)
    _ensure_table()
    cursor = _db.execute("DELETE FROM people_password_vaults WHERE user_id = ?", (user_id,))
    return {"success": True, "deleted": cursor.rowcount > 0}
