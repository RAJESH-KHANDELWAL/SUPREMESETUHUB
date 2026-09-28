
import sqlite3
import uuid
import re
from pathlib import Path
from urllib.parse import quote

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/api/v1/contacts",
    tags=["Contacts"],
)

DB_PATH = Path(__file__).resolve().parents[1] / "supreme_identities.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS supreme_contacts (
                contact_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                label TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                country_code TEXT NOT NULL,
                contact_type TEXT NOT NULL,
                is_public INTEGER NOT NULL DEFAULT 1,
                mobile_verified INTEGER NOT NULL DEFAULT 0,
                whatsapp_verified INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                UNIQUE(user_id, phone_number)
            )
        """)


init_db()


class ContactRequest(BaseModel):
    label: str = Field(min_length=1, max_length=100)
    phone_number: str = Field(min_length=5, max_length=20)
    country_code: str = Field(default="+91", max_length=5)
    contact_type: str = Field(default="personal", max_length=30)
    is_public: bool = True


def normalize_phone(phone_number: str, country_code: str):
    digits = re.sub(r"\D", "", phone_number)
    country_digits = re.sub(r"\D", "", country_code)

    if not digits or not country_digits:
        raise HTTPException(
            status_code=422,
            detail="Valid phone number and country code are required",
        )

    if digits.startswith(country_digits):
        full_number = digits
    else:
        full_number = country_digits + digits.lstrip("0")

    if not 8 <= len(full_number) <= 15:
        raise HTTPException(
            status_code=422,
            detail="Phone number must contain 8 to 15 digits including country code",
        )

    return full_number


def contact_response(row):
    data = dict(row)
    phone = data["phone_number"]

    data["is_public"] = bool(data["is_public"])
    data["mobile_verified"] = bool(data["mobile_verified"])
    data["whatsapp_verified"] = bool(data["whatsapp_verified"])

    data["verification_status"] = {
        "mobile": "verified" if data["mobile_verified"] else "not_verified",
        "whatsapp": "verified" if data["whatsapp_verified"] else "not_verified",
    }

    data["links"] = {
        "call": f"tel:+{phone}",
        "sms": f"sms:+{phone}",
        "whatsapp": f"https://wa.me/{phone}",
    }

    return data


def get_user(user_id: str):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT user_id FROM supreme_identities WHERE user_id = ?",
            (user_id,),
        ).fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="User identity not found",
        )


@router.post("/{user_id}")
def add_contact(user_id: str, payload: ContactRequest):
    get_user(user_id)

    label = payload.label.strip()
    if not label:
        raise HTTPException(
            status_code=422,
            detail="Contact label is required",
        )

    full_number = normalize_phone(
        payload.phone_number,
        payload.country_code,
    )

    contact_id = str(uuid.uuid4())
    created_at = __import__("datetime").datetime.now(
        __import__("datetime").timezone.utc
    ).isoformat()

    try:
        with get_connection() as conn:
            conn.execute(
                """
                INSERT INTO supreme_contacts (
                    contact_id, user_id, label, phone_number,
                    country_code, contact_type, is_public,
                    mobile_verified, whatsapp_verified, created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, ?)
                """,
                (
                    contact_id,
                    user_id,
                    label,
                    full_number,
                    payload.country_code,
                    payload.contact_type,
                    int(payload.is_public),
                    created_at,
                ),
            )
    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="This phone number is already registered for this user",
        )

    return {
        "success": True,
        "message": "Contact added. Verification is pending.",
        "contact_id": contact_id,
        "user_id": user_id,
        "label": label,
        "phone_number": "+" + full_number,
        "mobile_verified": False,
        "whatsapp_verified": False,
        "links": {
            "call": f"tel:+{full_number}",
            "sms": f"sms:+{full_number}",
            "whatsapp": f"https://wa.me/{full_number}",
        },
    }


@router.get("/{user_id}")
def list_contacts(user_id: str):
    get_user(user_id)

    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT *
            FROM supreme_contacts
            WHERE user_id = ?
            ORDER BY created_at DESC
            """,
            (user_id,),
        ).fetchall()

    return {
        "success": True,
        "user_id": user_id,
        "total": len(rows),
        "contacts": [contact_response(row) for row in rows],
    }


@router.delete("/{user_id}/{contact_id}")
def delete_contact(user_id: str, contact_id: str):
    get_user(user_id)

    with get_connection() as conn:
        result = conn.execute(
            """
            DELETE FROM supreme_contacts
            WHERE user_id = ? AND contact_id = ?
            """,
            (user_id, contact_id),
        )

    if result.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Contact not found",
        )

    return {
        "success": True,
        "message": "Contact deleted successfully",
        "contact_id": contact_id,
    }
