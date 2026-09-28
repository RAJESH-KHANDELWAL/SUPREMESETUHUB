
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field

router = APIRouter(
    prefix="/api/v1/identities",
    tags=["Identities"],
)

DB_PATH = Path(__file__).resolve().parents[1] / "supreme_identities.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS supreme_identities (
                user_id TEXT PRIMARY KEY,
                full_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                created_at TEXT NOT NULL
            )
        """)


init_db()


def generate_user_id():
    """Generate a unique 16-character ID in 4-4-4-4 format."""
    return str(uuid.uuid4().hex[:16].upper())


class RegisterRequest(BaseModel):
    full_name: str = Field(min_length=1, max_length=200)
    email: EmailStr


@router.post("/register")
def register_identity(payload: RegisterRequest):
    full_name = payload.full_name.strip()
    email = str(payload.email).strip().lower()

    if not full_name:
        raise HTTPException(
            status_code=422,
            detail="Full name is required",
        )

    user_id = generate_user_id()
    created_at = datetime.now(timezone.utc).isoformat()

    try:
        with get_connection() as conn:
            conn.execute(
                """
                INSERT INTO supreme_identities
                (user_id, full_name, email, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, full_name, email, created_at),
            )
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="This email is already registered",
        )

    return {
        "success": True,
        "message": "Identity registered successfully",
        "user_id": user_id,
        "full_name": full_name,
        "email": email,
        "created_at": created_at,
    }


@router.get("/{user_id}")
def get_identity(user_id: str):
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT user_id, full_name, email, created_at
            FROM supreme_identities
            WHERE user_id = ?
            """,
            (user_id,),
        ).fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Identity not found",
        )

    return {
        "success": True,
        "identity": dict(row),
    }


@router.get("/health/status")
def identity_health():
    return {
        "success": True,
        "status": "running",
    }
