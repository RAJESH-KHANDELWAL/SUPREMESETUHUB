import os
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, EmailStr

router = APIRouter(
    prefix="/api/v1/identities",
    tags=["Supreme Identities"],
)

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = Path(
    os.getenv("SUPREME_DB_PATH", str(BASE_DIR / "supreme.db"))
)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS supreme_identities (
                user_id TEXT PRIMARY KEY,
                full_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at TEXT NOT NULL
            )
        """)


init_db()


class IdentityCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    email: EmailStr


class IdentityResponse(BaseModel):
    user_id: str
    full_name: str
    email: EmailStr
    created_at: str


@router.post(
    "/register",
    response_model=IdentityResponse,
    status_code=201,
)
def register_identity(data: IdentityCreate):
    user_id = "SUP-" + uuid.uuid4().hex.upper()
    created_at = datetime.now(timezone.utc).isoformat()

    try:
        with get_connection() as conn:
            conn.execute(
                """
                INSERT INTO supreme_identities
                (user_id, full_name, email, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (
                    user_id,
                    data.full_name.strip(),
                    str(data.email).lower(),
                    created_at,
                ),
            )
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        )

    return IdentityResponse(
        user_id=user_id,
        full_name=data.full_name.strip(),
        email=data.email,
        created_at=created_at,
    )


@router.get("/{user_id}", response_model=IdentityResponse)
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
            detail="USER_ID not found",
        )

    return dict(row)


@router.get("/")
def list_identities(limit: int = 20):
    limit = max(1, min(limit, 100))

    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT user_id, full_name, email, created_at
            FROM supreme_identities
            ORDER BY created_at DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return {
        "count": len(rows),
        "identities": [dict(row) for row in rows],
    }


@router.get("/health/status")
def identity_health():
    return {
        "status": "healthy",
        "service": "SUPREMESETUHUB IDENTITY API",
    }
