"""Explainable contact-quality checks; format checks never claim real-world verification."""
from __future__ import annotations

import re
from typing import Any, Mapping


_PLACEHOLDERS = {"", "unknown", "n/a", "na", "none", "null", "test", "no name", "not available"}
_EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
_DIGITS = re.compile(r"\D")


def _text(record: Mapping[str, Any], key: str) -> str:
    return str(record.get(key) or "").strip()


def _valid_indian_mobile(value: str) -> bool:
    digits = _DIGITS.sub("", value)
    if digits.startswith("0091"):
        digits = digits[4:]
    elif digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    elif digits.startswith("0") and len(digits) == 11:
        digits = digits[1:]
    return len(digits) == 10 and digits[0] in "6789"


def assess_contact_quality(record: Mapping[str, Any]) -> dict[str, Any]:
    """Return transparent flags and a completeness score, not a truth guarantee."""
    flags: list[dict[str, str]] = []
    checks: list[bool] = []

    name = _text(record, "full_name")
    if name.casefold() in _PLACEHOLDERS:
        flags.append({"field": "full_name", "code": "NAME_MISSING_OR_PLACEHOLDER", "severity": "HIGH"})
        checks.append(False)
    else:
        checks.append(True)

    phone = _text(record, "phone")
    if not phone:
        flags.append({"field": "phone", "code": "PHONE_MISSING", "severity": "HIGH"})
        checks.append(False)
    elif not _valid_indian_mobile(phone):
        flags.append({"field": "phone", "code": "PHONE_FORMAT_INVALID", "severity": "HIGH"})
        checks.append(False)
    else:
        checks.append(True)

    email = _text(record, "email")
    if not email:
        flags.append({"field": "email", "code": "EMAIL_MISSING", "severity": "MEDIUM"})
        checks.append(False)
    elif not _EMAIL.fullmatch(email):
        flags.append({"field": "email", "code": "EMAIL_FORMAT_INVALID", "severity": "HIGH"})
        checks.append(False)
    else:
        checks.append(True)

    whatsapp = _text(record, "whatsapp_phone")
    if not whatsapp:
        flags.append({"field": "whatsapp_phone", "code": "WHATSAPP_NOT_PROVIDED", "severity": "LOW"})
        checks.append(False)
    elif not _valid_indian_mobile(whatsapp):
        flags.append({"field": "whatsapp_phone", "code": "WHATSAPP_FORMAT_INVALID", "severity": "HIGH"})
        checks.append(False)
    else:
        checks.append(True)

    for field, code in (("organization", "COMPANY_MISSING"), ("address", "ADDRESS_MISSING"), ("city", "CITY_MISSING")):
        if not _text(record, field):
            flags.append({"field": field, "code": code, "severity": "MEDIUM"})
            checks.append(False)
        else:
            checks.append(True)

    # Format/completeness score only. Real-world validity needs verification evidence.
    score = round(100 * sum(checks) / len(checks)) if checks else 0
    verification = str(record.get("verification_status") or "UNVERIFIED").upper()
    if verification not in {"UNVERIFIED", "PENDING", "VERIFIED", "INVALID", "DO_NOT_USE"}:
        verification = "UNVERIFIED"
    if verification in {"INVALID", "DO_NOT_USE"}:
        label = "REVIEW_REQUIRED"
    elif any(item["severity"] == "HIGH" for item in flags):
        label = "REVIEW_REQUIRED"
    elif flags:
        label = "INCOMPLETE"
    elif verification != "VERIFIED":
        label = "FORMAT_OK_UNVERIFIED"
    else:
        label = "VERIFIED"

    return {
        "quality_score": score,
        "quality_label": label,
        "verification_status": verification,
        "flags": flags,
        "flag_count": len(flags),
        "next_action": (
            "HUMAN_REVIEW_AND_VERIFY" if label == "REVIEW_REQUIRED"
            else "FILL_MISSING_FIELDS" if label == "INCOMPLETE"
            else "VERIFY_CONTACT_WITH_APPROVED_EVIDENCE" if label == "FORMAT_OK_UNVERIFIED"
            else "READY_FOR_NORMAL_CRM_WORKFLOW"
        ),
        "claims_real_world_validity": verification == "VERIFIED",
        "method": "RULE_BASED_FORMAT_AND_COMPLETENESS_CHECK",
    }
