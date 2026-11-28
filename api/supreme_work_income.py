"""SUPREME ECOSYSTEM work and income directory.

This API lists official marketplace entry points and generates a user-initiated
WhatsApp click-to-chat link. It does not claim that a job is live or guaranteed,
and it does not send WhatsApp messages automatically.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote

from fastapi import APIRouter, HTTPException, Query

router = APIRouter(
    prefix="/api/v1/supreme-ecosystem/work-income",
    tags=["SUPREME ECOSYSTEM - WORK AND INCOME"],
)

CATALOG_PATH = (
    Path(__file__).resolve().parents[1]
    / "supreme"
    / "ecosystem"
    / "work_income"
    / "catalog.json"
)


def _load_catalog() -> dict:
    try:
        with CATALOG_PATH.open("r", encoding="utf-8") as catalog_file:
            data = json.load(catalog_file)
    except (OSError, json.JSONDecodeError) as exc:
        raise HTTPException(
            status_code=503,
            detail="WORK_INCOME_CATALOG_UNAVAILABLE",
        ) from exc

    if not isinstance(data.get("sources"), list):
        raise HTTPException(
            status_code=503,
            detail="WORK_INCOME_CATALOG_INVALID",
        )
    return data


@router.get("/sources")
def list_work_income_sources(
    skill: str | None = Query(default=None, max_length=80),
):
    """Return official marketplace entry points, optionally filtered by skill."""
    catalog = _load_catalog()
    sources = catalog["sources"]

    if skill:
        needle = skill.strip().casefold()
        sources = [
            source
            for source in sources
            if needle in source["name"].casefold()
            or any(needle in item.casefold() for item in source.get("best_for", []))
        ]

    return {
        "success": True,
        "directory_type": "OFFICIAL_MARKETPLACE_ENTRY_POINTS",
        "warning": (
            "These are marketplace/search links, not verified individual live jobs. "
            "Check each listing and employer before applying."
        ),
        "focus_skills": catalog.get("focus_skills", []),
        "count": len(sources),
        "sources": sources,
    }


@router.get("/whatsapp-link")
def create_whatsapp_click_to_chat(
    topic: str = Query(default="freelance work", max_length=120),
):
    """Create a click-to-chat link; the user must open WhatsApp and press Send."""
    catalog = _load_catalog()
    whatsapp = catalog.get("whatsapp_workflow", {})
    phone_link = whatsapp.get("contact_link", "https://wa.me/917611967229")
    template = whatsapp.get("message_template", "")
    message = f"{template}\n\nMy current priority: {topic.strip() or 'freelance work'}."
    separator = "&" if "?" in phone_link else "?"
    return {
        "success": True,
        "status": "CLICK_TO_CHAT_READY",
        "whatsapp_url": f"{phone_link}{separator}text={quote(message)}",
        "automatic_message_sent": False,
        "whatsapp_business_api_connected": False,
        "note": (
            "This opens a WhatsApp draft only. It does not send a message or "
            "enable AI replies; official WhatsApp Business API setup and webhook "
            "verification are still required for automation."
        ),
    }


@router.get("/status")
def work_income_status():
    catalog = _load_catalog()
    return {
        "success": True,
        "module": "SUPREME ECOSYSTEM WORK AND INCOME",
        "status": "DIRECTORY_READY",
        "catalog_count": len(catalog.get("sources", [])),
        "live_job_verification": "NOT_PERFORMED_BY_THIS_DIRECTORY",
        "whatsapp": "MANUAL_CLICK_TO_CHAT_ONLY",
        "income_guarantee": False,
    }
