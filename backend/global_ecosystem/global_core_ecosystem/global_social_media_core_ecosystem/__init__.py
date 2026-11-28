"""Global Social Media Core package."""
LAYER="CORE"
CATEGORY="SOCIAL_MEDIA"
ECOSYSTEM_ID="GLOBAL-SOCIAL-MEDIA-CORE-ECOSYSTEM"
ECOSYSTEM_NAME="GLOBAL SOCIAL MEDIA CORE ECOSYSTEM"
from .manager import SocialMediaCoreManager,get_manager
__all__=["LAYER","CATEGORY","ECOSYSTEM_ID","ECOSYSTEM_NAME","SocialMediaCoreManager","get_manager"]
