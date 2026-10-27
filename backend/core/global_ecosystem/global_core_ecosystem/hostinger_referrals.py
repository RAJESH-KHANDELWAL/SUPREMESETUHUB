"""Owner-managed Hostinger referral links registered for the SUPREME ecosystem.

These are referral URLs supplied/confirmed by the owner. They are not API
credentials. Hostinger remains the source of truth for attribution and rewards.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

HOSTINGER_REFERRAL_ACCOUNTS: list[dict[str, Any]] = [
    {
        "identity_id": "DRRAJESHKHANDELWALIBC",
        "display_name": "DR RAJESH KHANDELWAL IBC",
        "referral_code": "RAJESHIBCGLOBAL",
        "referral_url": "https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGLOBAL",
        "primary": True,
    },
    {
        "identity_id": "DRRAJESHKHANDELWALIBCOFFICIAL",
        "display_name": "DR RAJESH KHANDELWAL IBC OFFICIAL",
        "referral_code": "RAJESHIBCGROWTH",
        "referral_url": "https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGROWTH",
        "primary": False,
    },
    {
        "identity_id": "RAJESHKHANDELWALOFFICIAL",
        "display_name": "RAJESH KHANDELWAL OFFICIAL",
        "referral_code": "RAJESHGROWTH",
        "referral_url": "https://www.hostinger.com/in?REFERRALCODE=RAJESHGROWTH",
        "primary": False,
    },
    {
        "identity_id": "RAJESHKHANDELWAL",
        "display_name": "RAJESH KHANDELWAL",
        "referral_code": "RAJESHGLOBAL",
        "referral_url": "https://www.hostinger.com/in?REFERRALCODE=RAJESHGLOBAL",
        "primary": False,
    },
]


def get_hostinger_referral_accounts() -> list[dict[str, Any]]:
    """Return defensive copies of the owner's configured Hostinger referral links."""
    return deepcopy(HOSTINGER_REFERRAL_ACCOUNTS)


def get_primary_hostinger_referral_url() -> str:
    """Return the currently supplied primary referral URL."""
    return next(item["referral_url"] for item in HOSTINGER_REFERRAL_ACCOUNTS if item["primary"])
