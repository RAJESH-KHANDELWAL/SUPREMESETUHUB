"""Anthropic Files Core package."""
from .ecosystem_config import PRODUCT_ID, PRODUCT_NAME, CATEGORY, API_NAME, AVAILABILITY
from .service import AnthropicFilesCoreService

def _manifest():
    return {
        "schema_version":"1.0.0","provider":"anthropic","product_id":PRODUCT_ID,
        "product_name":PRODUCT_NAME,"category":CATEGORY,"api":API_NAME,
        "availability":AVAILABILITY,"live_connection":False,
    }

__all__=["AnthropicFilesCoreService","PRODUCT_ID","PRODUCT_NAME","CATEGORY","API_NAME","AVAILABILITY"]

# Google Core-style domain manager entry point.
from .manager import get_manager
