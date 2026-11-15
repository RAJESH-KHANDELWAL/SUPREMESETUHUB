import sqlite3
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, EmailStr

from backend.database import DatabaseService

router = APIRouter(
    prefix="/api/v1/identities",
    tags=["Supreme Identities"],
)

# Use the platform's shared database service and SUPREME_DB_PATH.
# Do not open a separate SQLite connection or choose a separate default path here.
database = DatabaseService()


def init_db():
    database.execute(
        """
        CREATE TABLE IF NOT EXISTS supreme_identities (
            user_id TEXT PRIMARY KEY,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )


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
    full_name = data.full_name.strip()
    email = str(data.email).lower()
    created_at = datetime.now(timezone.utc).isoformat()

    try:
        database.execute(
            """
            INSERT INTO supreme_identities
            (user_id, full_name, email, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, full_name, email, created_at),
        )
    except sqlite3.IntegrityError as exc:
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        ) from exc

    return IdentityResponse(
        user_id=user_id,
        full_name=full_name,
        email=email,
        created_at=created_at,
    )


@router.get("/{user_id}", response_model=IdentityResponse)
def get_identity(user_id: str):
    row = database.fetchone(
        """
        SELECT user_id, full_name, email, created_at
        FROM supreme_identities
        WHERE user_id = ?
        """,
        (user_id,),
    )

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="USER_ID not found",
        )

    return dict(row)


@router.get("/")
def list_identities(limit: int = 20):
    limit = max(1, min(limit, 100))
    rows = database.fetchall(
        """
        SELECT user_id, full_name, email, created_at
        FROM supreme_identities
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (limit,),
    )

    return {
        "count": len(rows),
        "identities": [dict(row) for row in rows],
    }


@router.get("/health/status")
def identity_health():
    health = database.health()
    return {
        "status": "healthy" if health["healthy"] else "unhealthy",
        "service": "SUPREMESETUHUB IDENTITY API",
        "database": health,
    }
