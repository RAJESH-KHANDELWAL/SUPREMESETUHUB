"""Public contact profile for DR RAJESH KHANDELWAL IBC."""

from __future__ import annotations

from fastapi import APIRouter

from backend.supreme.supreme_owner_admin.service import SupremeOwnerAdminService
from backend.supreme.keyword_foundation import keyword_foundation

router = APIRouter(
    prefix="/api/v1/global-business-coach",
    tags=["GLOBAL BUSINESS COACH"],
)


def public_business_coach_profile() -> dict:
    """Return only intended public contact and business information."""
    profile = SupremeOwnerAdminService().global_business_coach_profile()
    channels = profile["contact_channels"]
    social = profile["social_identity"]
    return {
        "success": True,
        "brand": profile["brand"],
        "role": profile["role"],
        "audience": profile["audience"],
        "services": profile["scope"],
        "website": profile["website"],
        "contact": {
            "email": channels["email"]["address"],
            "mailto_url": channels["email"]["mailto_url"],
            "whatsapp_url": channels["whatsapp"]["url"],
            "website_form_url": channels["website_form"]["url"],
        },
        "social": {
            "intended_username": social["intended_username"],
            "handle": social["handle"],
            "platforms_requested": social["platforms_requested"],
            "profile_urls_verified": social["profile_urls_verified"],
            "username_availability_verified": social["username_availability_verified"],
        },
        "status": "CONTACT_PROFILE_PUBLISHED_CONNECTIONS_NOT_VERIFIED",
        "note": (
            "Social username is the requested consistent handle, not proof that "
            "every platform account exists or that the username is available. "
            "Website form and message delivery must be configured and tested separately."
        ),
    }


@router.get("/profile")
def global_business_coach_profile():
    """Public business contact card for Bharat and global inquiries."""
    return public_business_coach_profile()


@router.get("/keywords")
def global_business_coach_keywords():
    """Return concise keyword groups for Bharat and global content planning."""
    return keyword_foundation()
