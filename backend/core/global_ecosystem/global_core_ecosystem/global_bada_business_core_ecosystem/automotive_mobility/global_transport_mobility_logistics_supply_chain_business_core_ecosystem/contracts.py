"""Stable contracts for transport, logistics and supply-chain business Core."""
def validate_identifier(value):
    if not isinstance(value, str) or not value.strip(): raise ValueError("IDENTIFIER_REQUIRED")
    return value.strip().upper()

def core_result(*, success, ecosystem_id, status, data=None):
    return {"success": success, "ecosystem_id": ecosystem_id, "status": status, "data": data or {}, "live_connection_verified": False}
