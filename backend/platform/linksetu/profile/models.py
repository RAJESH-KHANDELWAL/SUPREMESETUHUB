"""
LINKSETU PROFILE MODEL
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class LinkSetuProfile:
    user_id: str
    username: str
    display_name: str
    bio: str = ""
    avatar_url: Optional[str] = None
    website: Optional[str] = None
    is_verified: bool = False
    is_active: bool = True
