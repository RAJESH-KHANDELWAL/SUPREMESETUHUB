"""Provider-agnostic payee detail pre-checks.

Important: format validation is NOT bank-account ownership verification.
A provider adapter must be configured and return an authenticated result before
an account holder can be marked VERIFIED. This module never fabricates a green
verification result.
"""
from __future__ import annotations

import re
from urllib.parse import parse_qs, urlparse


UPI_ID_RE = re.compile(r"^[A-Za-z0-9._-]{2,200}@[A-Za-z][A-Za-z0-9.-]{1,62}$")
IFSC_RE = re.compile(r"^[A-Z]{4}0[A-Z0-9]{6}$")
ACCOUNT_RE = re.compile(r"^[0-9]{6,34}$")


def parse_upi_qr(payload: str) -> dict[str, str]:
    """Parse a UPI payment URI without treating its contents as verified."""
    value = payload.strip()
    parsed = urlparse(value)
    if parsed.scheme.lower() != "upi" or parsed.netloc.lower() != "pay":
        raise ValueError("UNSUPPORTED_QR_FORMAT")
    params = parse_qs(parsed.query, keep_blank_values=False)
    payee_vpa = params.get("pa", [""])[0].strip()
    payee_name = params.get("pn", [""])[0].strip()
    amount = params.get("am", [""])[0].strip()
    if not payee_vpa or not UPI_ID_RE.fullmatch(payee_vpa):
        raise ValueError("INVALID_OR_MISSING_UPI_ID")
    return {
        "payment_method": "UPI",
        "payee_upi_id": payee_vpa,
        "qr_payee_name": payee_name[:200],
        "amount": amount,
        "format_valid": "true",
        "verification_status": "NOT_VERIFIED",
        "verification_source": "QR_PAYLOAD_ONLY",
        "message": "QR data was parsed; payee identity has not been verified by a payment provider.",
    }


def precheck_payee_details(
    payment_method: str,
    *,
    upi_id: str = "",
    account_number: str = "",
    ifsc: str = "",
    qr_payload: str = "",
) -> dict[str, object]:
    """Validate input shape and explicitly defer identity verification to a provider."""
    method = payment_method.strip().upper()
    if method == "UPI_QR":
        parsed = parse_upi_qr(qr_payload)
        return {
            **parsed,
            "account_holder_name": None,
            "verified": False,
            "next_step": "CONNECT_AUTHORIZED_PROVIDER_FOR_PAYEE_NAME_VERIFICATION",
        }
    if method == "UPI_ID":
        value = upi_id.strip()
        valid = bool(UPI_ID_RE.fullmatch(value))
        return {
            "payment_method": method,
            "format_valid": valid,
            "verification_status": "NOT_VERIFIED" if valid else "INVALID_FORMAT",
            "account_holder_name": None,
            "verified": False,
            "masked_identifier": _mask_upi(value) if valid else None,
            "verification_source": None,
            "message": (
                "UPI ID format looks valid; holder name still requires provider verification."
                if valid else "UPI ID format is invalid."
            ),
            "next_step": "CONNECT_AUTHORIZED_PROVIDER_FOR_PAYEE_NAME_VERIFICATION" if valid else "CORRECT_DETAILS",
        }
    if method == "BANK_ACCOUNT":
        account = account_number.strip()
        bank_ifsc = ifsc.strip().upper()
        valid_account = bool(ACCOUNT_RE.fullmatch(account))
        valid_ifsc = bool(IFSC_RE.fullmatch(bank_ifsc))
        valid = valid_account and valid_ifsc
        return {
            "payment_method": method,
            "format_valid": valid,
            "account_number_format_valid": valid_account,
            "ifsc_format_valid": valid_ifsc,
            "verification_status": "NOT_VERIFIED" if valid else "INVALID_FORMAT",
            "account_holder_name": None,
            "verified": False,
            "masked_account_number": _mask_account(account) if valid_account else None,
            "ifsc": bank_ifsc if valid_ifsc else None,
            "verification_source": None,
            "message": (
                "Bank details format looks valid; account holder name requires an authorized bank verification service."
                if valid else "Account number or IFSC format is invalid."
            ),
            "next_step": "CONNECT_AUTHORIZED_PROVIDER_FOR_ACCOUNT_NAME_VERIFICATION" if valid else "CORRECT_DETAILS",
        }
    raise ValueError("UNSUPPORTED_PAYMENT_METHOD")


def _mask_upi(value: str) -> str:
    local, domain = value.split("@", 1)
    visible = local[:2]
    return f"{visible}{'*' * max(2, len(local) - len(visible))}@{domain}"


def _mask_account(value: str) -> str:
    return "*" * max(0, len(value) - 4) + value[-4:]
