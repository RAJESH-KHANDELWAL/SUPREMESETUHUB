
import sqlite3
import uuid
import re
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, model_validator

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
            CREATE TABLE IF NOT EXISTS supreme_contacts_v2 (
                contact_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                label TEXT NOT NULL,
                country_code TEXT NOT NULL,
                contact_type TEXT NOT NULL,
                mobile_number TEXT,
                whatsapp_number TEXT,
                std_code TEXT,
                landline_number TEXT,
                is_public INTEGER NOT NULL DEFAULT 1,
                mobile_verified INTEGER NOT NULL DEFAULT 0,
                whatsapp_verified INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL
            )
        """)


init_db()


class ContactRequest(BaseModel):
    label: str = Field(min_length=1, max_length=100)
    country_code: str = Field(default="+91", max_length=6)
    contact_type: str = Field(default="personal", max_length=30)

    mobile_number: str | None = Field(default=None, max_length=20)
    whatsapp_number: str | None = Field(default=None, max_length=20)

    std_code: str | None = Field(default=None, max_length=10)
    landline_number: str | None = Field(default=None, max_length=20)

    is_public: bool = True

    @model_validator(mode="after")
    def validate_contact(self):
        if not any([
            self.mobile_number,
            self.whatsapp_number,
            self.landline_number,
        ]):
            raise ValueError(
                "At least one phone, WhatsApp, or landline number is required"
            )

        if self.landline_number and not self.std_code:
            raise ValueError(
                "STD code is required for a landline number"
            )

        return self


def digits_only(value: str | None) -> str | None:
    if value is None:
        return None
    digits = re.sub(r"\D", "", value)
    return digits or None


def normalize_country_code(value: str) -> str:
    digits = digits_only(value)
    if not digits or not 1 <= len(digits) <= 3:
        raise HTTPException(
            status_code=422,
            detail="Invalid country calling code",
        )
    return "+" + digits


def normalize_phone(value: str | None, country_code: str):
    digits = digits_only(value)
    if digits is None:
        return None

    if not 6 <= len(digits) <= 15:
        raise HTTPException(
            status_code=422,
            detail="Phone number must contain 6 to 15 digits",
        )

    country_digits = country_code.lstrip("+")

    if digits.startswith(country_digits):
        return digits

    return country_digits + digits.lstrip("0")


def normalize_std_code(value: str | None):
    if value is None:
        return None

    digits = digits_only(value)
    if not digits or len(digits) > 10:
        raise HTTPException(
            status_code=422,
            detail="Invalid STD code",
        )

    return digits


def normalize_landline(value: str | None):
    digits = digits_only(value)
    if digits is None:
        return None

    if not 4 <= len(digits) <= 12:
        raise HTTPException(
            status_code=422,
            detail="Invalid landline number",
        )

    return digits


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


def make_links(phone: str | None, whatsapp: str | None,
               landline: str | None):
    links = {}

    if phone:
        links["mobile_call"] = f"tel:+{phone}"
        links["mobile_sms"] = f"sms:+{phone}"

    if whatsapp:
        links["whatsapp"] = f"https://wa.me/{whatsapp}"

    if landline:
        links["landline_call"] = f"tel:+{landline}"

    return links


def contact_response(row):
    data = dict(row)

    data["is_public"] = bool(data["is_public"])
    data["mobile_verified"] = bool(data["mobile_verified"])
    data["whatsapp_verified"] = bool(data["whatsapp_verified"])

    data["verification_status"] = {
        "mobile": "verified" if data["mobile_verified"] else "not_verified",
        "whatsapp": "verified" if data["whatsapp_verified"] else "not_verified",
    }

    data["links"] = make_links(
        data["mobile_number"],
        data["whatsapp_number"],
        (
            data["country_code"].lstrip("+")
            + (data["std_code"] or "").lstrip("0")
            + (data["landline_number"] or "")
            if data["landline_number"]
            else None
        ),
    )

    return data


@router.post("/{user_id}")
def add_contact(user_id: str, payload: ContactRequest):
    get_user(user_id)

    label = payload.label.strip()
    if not label:
        raise HTTPException(
            status_code=422,
            detail="Contact label is required",
        )

    country_code = normalize_country_code(payload.country_code)

    mobile = normalize_phone(payload.mobile_number, country_code)
    whatsapp = normalize_phone(payload.whatsapp_number, country_code)

    std_code = normalize_std_code(payload.std_code)
    landline = normalize_landline(payload.landline_number)

    if landline and std_code:
        landline = std_code + landline

    contact_id = str(uuid.uuid4())
    created_at = datetime.now(timezone.utc).isoformat()

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO supreme_contacts_v2 (
                contact_id, user_id, label, country_code,
                contact_type, mobile_number, whatsapp_number,
                std_code, landline_number, is_public,
                mobile_verified, whatsapp_verified, created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 0, ?)
            """,
            (
                contact_id,
                user_id,
                label,
                country_code,
                payload.contact_type,
                mobile,
                whatsapp,
                std_code,
                landline,
                int(payload.is_public),
                created_at,
            ),
        )

    return {
        "success": True,
        "message": "Contact added. Verification is pending.",
        "contact_id": contact_id,
        "user_id": user_id,
        "label": label,
        "country_code": country_code,
        "mobile_number": mobile,
        "whatsapp_number": whatsapp,
        "std_code": std_code,
        "landline_number": landline,
        "mobile_verified": False,
        "whatsapp_verified": False,
        "links": make_links(mobile, whatsapp, landline),
    }


@router.get("/{user_id}")
def list_contacts(user_id: str):
    get_user(user_id)

    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT *
            FROM supreme_contacts_v2
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
            DELETE FROM supreme_contacts_v2
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
