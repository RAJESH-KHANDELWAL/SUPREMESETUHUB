"""Paytm provider metadata; not proof of partnership or live API access."""
PROVIDER = {
    "id": "paytm", "name": "Paytm", "origin": "india",
    "scope": "Payments, wallet and merchant services; credentials depend on approved merchant products", "credential_env": "PAYTM_MERCHANT_KEY",
    "integration_status": "scaffold", "live_connection_verified": False,
}
__all__ = ["PROVIDER"]
