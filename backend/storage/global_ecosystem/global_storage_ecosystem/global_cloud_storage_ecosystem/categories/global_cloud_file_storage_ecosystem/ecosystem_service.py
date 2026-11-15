"""Category-level metadata contract; no external operations."""
CATEGORY_ID = "FILE_STORAGE"

def describe() -> dict:
    return {"category_id": CATEGORY_ID, "connection_state": "NOT_CONFIGURED", "storage_operations_enabled": False}
