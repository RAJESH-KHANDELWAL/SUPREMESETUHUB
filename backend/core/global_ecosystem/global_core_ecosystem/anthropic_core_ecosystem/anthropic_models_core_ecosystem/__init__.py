"""Anthropic Models Core package."""
from .ecosystem_config import PRODUCT_ID, PRODUCT_NAME, CATEGORY, API_NAME, AVAILABILITY
from .service import AnthropicModelsCoreService

def _manifest():
    return {
        "schema_version":"1.0.0","provider":"anthropic","product_id":PRODUCT_ID,
        "product_name":PRODUCT_NAME,"category":CATEGORY,"api":API_NAME,
        "availability":AVAILABILITY,"live_connection":False,
    }

__all__=["AnthropicModelsCoreService","PRODUCT_ID","PRODUCT_NAME","CATEGORY","API_NAME","AVAILABILITY"]
