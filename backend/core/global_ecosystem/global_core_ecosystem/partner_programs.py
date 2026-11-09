"""Curated partner-program registry for the SUPREME ecosystem."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

from .hostinger_referrals import (
    get_hostinger_referral_accounts,
    get_primary_hostinger_referral_url,
)

HOSTINGER_REFERRAL_PROGRAM: dict[str, Any] = {
    "program_id": "HOSTINGER-REFERRAL-RAJESHIBCGLOBAL",
    "provider_id": "HOSTINGER",
    "provider_name": "Hostinger",
    "program_type": "REFERRAL",
    "ecosystem_id": "GLOBAL-AFFILIATE-MARKETING-API-ECOSYSTEM",
    "owner_brand": "DR RAJESH KHANDELWAL IBC",
    "referral_url": get_primary_hostinger_referral_url(),
    "referral_accounts": get_hostinger_referral_accounts(),
    "provider_advertised_reward": "Up to USD 180 per eligible referral",
    "referred_friend_offer": "20% off the first plan (as displayed in the supplied account screenshot; re-check current terms)",
    "currency_context": "Account billing currency shown as INR; advertised referral reward shown in USD",
    "status": "CONFIGURED_NOT_VERIFIED_LIVE",
    "tracking_mode": "PROVIDER_ATTRIBUTION",
    "provider_dashboard_is_source_of_truth": True,
    "purchases_visible_to_supreme_without_provider_api": False,
    "capture_personal_data_without_consent": False,
    "last_reviewed_date": "2026-10-27",
    "notes": [
        "The primary referral URL is the currently supplied Hostinger dashboard link using RAJESHIBCGLOBAL.",
        "Four owner-managed referral links are registered; confirm each code remains active in its own Hostinger account before promotion.",
        "Preserve each exact provider referral URL; do not append unsupported tracking parameters.",
        "Hostinger determines eligible referral attribution and rewards under its current terms.",
        "A click is not proof of purchase; SUPREME cannot see referred-customer identity, plan, payment or commission status unless Hostinger supplies it through an authorized interface.",
    ],
}


def get_partner_program_catalog() -> list[dict[str, Any]]:
    """Return independent copies of configured public partner-program metadata."""
    return [deepcopy(HOSTINGER_REFERRAL_PROGRAM)]
