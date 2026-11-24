"""Framework-neutral catalog response; no DeepSeek API calls."""
from .ecosystem_taxonomy import list_categories
def get_catalog() -> dict:
    categories = list_categories()
    return {"ecosystem_id":"DEEPSEEK_STORAGE_ECOSYSTEM","count":len(categories),"connection_state":"NOT_CONFIGURED","categories":categories}
