"""Private-by-configuration SUPREME settings for the backend ecosystem.

Personal identifiers and contact details are loaded from deployment environment
variables. Do not commit real emails, credentials, access tokens, or secrets.
"""

import os
from datetime import datetime

# =========================================================
# 👑 RAJESH KHANDELWAL OFFICIAL — BRAND IDENTITY
# =========================================================

RAJESH_KHANDELWAL_OFFICIAL_BRAND = {
    "display_name": "👑 RAJESH KHANDELWAL OFFICIAL 👑",
    "username": "RAJESHKHANDELWALOFFICIAL",
    "domain_name": "RAJESHKHANDELWALOFFICIAL.COM",
    "gmail_id_name": "RAJESHKHANDELWALOFFICIAL@GMAIL.COM",
    "tagline": "🏡 REAL ESTATE COACH | ❤️ RELATIONSHIP & INTIMACY COACH",
}

# =========================================================
# 👑 SUPREMESETUHUB APPLICATION
# =========================================================

APP_NAME = "SUPREMESETUHUB"
APP_VERSION = "1.0.0"
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")
CREATED_AT = "2025-05-23"

# =========================================================
# 👑 UNIFIED SUPREME OWNER
# =========================================================

SUPREME_OWNER = {
    "person_id": os.getenv("SUPREME_OWNER_PERSON_ID", ""),
    "business_id": os.getenv("SUPREME_OWNER_BUSINESS_ID", ""),
    "company_id": os.getenv("SUPREME_OWNER_COMPANY_ID", ""),
    "supreme_id": os.getenv("SUPREME_ID", ""),
    "internal_user_id": os.getenv("SUPREME_OWNER_INTERNAL_USER_ID", ""),
    
    "status": "ACTIVE",
    "role": "SUPREME_OWNER",
    "level": 100,
    "verified": True,
    "official": True,
    "supreme": True,
    
    "display_names": [
        "👑 RAJESH KHANDELWAL 👑",
        "👑 RAJESH KHANDELWAL OFFICIAL 👑",
        "👑 DR RAJESH KHANDELWAL IBC 👑",
        "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑"
    ],
    
    "usernames": [
        "RAJESHKHANDELWAL",
        "RAJESHKHANDELWALOFFICIAL",
        "DRRAJESHKHANDELWALIBC",
        "DRRAJESHKHANDELWALIBCOFFICIAL"
    ],
    
    "primary_username": os.getenv("SUPREME_OWNER_USERNAME", "RAJESHKHANDELWALOFFICIAL"),
    "primary_display_name": os.getenv("SUPREME_OWNER_DISPLAY_NAME", "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑"),
    
    "title": "Digital Pioneer | AI Visionary | Supreme Owner",
    "bio": "Creator of SUPREMESETUHUB - Building the next generation of digital ecosystems. Master of Identity, Business, AI, Storage, Security and Digital Innovation.",
}

# =========================================================
# OWNER EMAILS — LOAD FROM DEPLOYMENT ENVIRONMENT
# Never commit personal email addresses or provider credentials.
# SUPREME_OWNER_EMAILS is a comma-separated private environment variable.
# =========================================================

EMAILS = [
    item.strip()
    for item in os.getenv("SUPREME_OWNER_EMAILS", "").split(",")
    if item.strip()
]
PRIMARY_EMAIL = os.getenv("SUPREME_OWNER_PRIMARY_EMAIL", "")
SECONDARY_EMAIL = os.getenv("SUPREME_OWNER_SECONDARY_EMAIL", "")
RECOVERY_EMAIL = os.getenv("SUPREME_OWNER_RECOVERY_EMAIL", "")

# Private owner/admin contact registry. Values must be set in deployment secrets;
# never expose this object from public status endpoints or commit real addresses.
OWNER_EMAIL_IDENTITIES = {
    "owner_admin_primary": PRIMARY_EMAIL,
    "owner_admin_secondary": SECONDARY_EMAIL,
    "security_recovery": RECOVERY_EMAIL,
}
OWNER_ADMIN_EMAILS = list(dict.fromkeys(
    email.strip().casefold()
    for email in (PRIMARY_EMAIL, SECONDARY_EMAIL)
    if email.strip()
))

# =========================================================
# 📛 ALL ALIAS NAMES & USERNAMES
# =========================================================

ALIAS_NAMES = [
    "RAJESH KHANDELWAL",
    "RAJESH KHANDELWAL OFFICIAL",
    "RAJESHKHANDELWAL",
    "RAJESHKHANDELWALOFFICIAL",
    "DR RAJESH KHANDELWAL IBC",
    "DR RAJESH KHANDELWAL IBC OFFICIAL",
    "DRRAJESHKHANDELWALIBC",
    "DRRAJESHKHANDELWALIBCOFFICIAL",
    "SUPREME RAJESH KHANDELWAL",
    "SUPREME DR RAJESH KHANDELWAL IBC"
]

# =========================================================
# 🔗 CONNECTED REPOSITORIES
# =========================================================

CONNECTED_REPOS = {
    # The central foundation repository. This entry identifies the source of truth;
    # it does not claim that every external runtime has already been connected.
    "SUPREMESETUHUB": {
        "name": "SUPREMESETUHUB",
        "owner": "RAJESH-KHANDELWAL",
        "url": "https://github.com/RAJESH-KHANDELWAL/SUPREMESETUHUB",
        "homepage": "https://rajesh-khandelwal.github.io/SUPREMESETUHUB/",
        "type": "MAIN_BASE_FOUNDATION",
        "status": "PRIMARY",
        "integration_mode": "CENTRAL_REGISTRY",
        "runtime_connection": "LOCAL_FOUNDATION"
    },
    "RAJESHKHANDELWAL": {
        "name": "RAJESHKHANDELWAL",
        "owner": "RAJESH-KHANDELWAL",
        "url": "https://github.com/RAJESH-KHANDELWAL/RAJESHKHANDELWAL",
        "homepage": "https://rajesh-khandelwal.github.io/RAJESHKHANDELWAL/",
        "type": "AI_ENGINE",
        "status": "REGISTERED",
        "integration_mode": "GITHUB_REPOSITORY_REGISTRY",
        "runtime_connection": "NOT_CONFIGURED"
    },
    "RAJESHKHANDELWALOFFICIAL": {
        "name": "RAJESHKHANDELWALOFFICIAL",
        "owner": "RAJESH-KHANDELWAL-OFFICIAL",
        "url": "https://github.com/RAJESH-KHANDELWAL-OFFICIAL/RAJESHKHANDELWALOFFICIAL",
        "homepage": "https://rajesh-khandelwal-official.github.io/RAJESHKHANDELWALOFFICIAL/",
        "type": "OFFICIAL_BRAND",
        "status": "REGISTERED",
        "integration_mode": "GITHUB_REPOSITORY_REGISTRY",
        "runtime_connection": "NOT_CONFIGURED"
    },
    "DRRAJESHKHANDELWALIBC": {
        "name": "DRRAJESHKHANDELWALIBC",
        "owner": "DR-RAJESH-KHANDELWAL-IBC",
        "url": "https://github.com/DR-RAJESH-KHANDELWAL-IBC/DRRAJESHKHANDELWALIBC",
        "homepage": "https://dr-rajesh-khandelwal-ibc.github.io/DRRAJESHKHANDELWALIBC/",
        "type": "SUPREME_IDENTITY",
        "status": "REGISTERED",
        "integration_mode": "GITHUB_REPOSITORY_REGISTRY",
        "runtime_connection": "NOT_CONFIGURED"
    }
}

# =========================================================
# 🎯 SUPREME PERMISSIONS
# =========================================================

PERMISSIONS = [
    "MANAGE_IDENTITY",
    "MANAGE_USERS",
    "MANAGE_BUSINESS",
    "MANAGE_STORAGE",
    "MANAGE_SECURITY",
    "MANAGE_AI",
    "MANAGE_API",
    "MANAGE_DASHBOARD",
    "MANAGE_ANALYTICS",
    "MANAGE_SOCIAL",
    "MANAGE_NOTIFICATIONS",
    "MANAGE_INTEGRATIONS",
    "MANAGE_MUKTI_MAHAL",
    "SYSTEM_ADMIN",
    "SUPER_ADMIN"
]

# =========================================================
# 🌐 CORE MODULES
# =========================================================

CORE_MODULES = [
    "Master Identity System",
    "Brand Management",
    "Business Management",
    "Storage & Files",
    "Security & Authentication",
    "API Gateway",
    "AI Services",
    "Backup & Restore",
    "Dashboard",
    "Notifications",
    "Social Integration",
    "Mukti Mahal Ecosystem"
]

# =========================================================
# 🎨 PLATFORM BRANDING
# =========================================================

BRANDING = {
    "primary_color": "#1F41BB",
    "secondary_color": "#E7245D",
    "accent_color": "#FFB800",
    "dark_bg": "#0A0E27",
    "card_bg": "#1a1f3a",
    "light_text": "#E0E0E0",
    "border_color": "#2a2f4a",
    "logo": "SUPREMESETUHUB",
    "tagline": "All-in-One Digital Ecosystem",
    "mission": "Unified Platform for Identity, Business, AI & Digital Innovation"
}

# =========================================================
# 📊 SUPREME OWNER STATISTICS
# =========================================================
# These values are unknown until backed by live platform data.
# Keep them unset rather than presenting unverified numbers as facts.

STATISTICS = {
    "followers": None,
    "following": None,
    "posts": None,
    "platform_users": None,
    "daily_active_users": None,
    "communities": None,
    "verified_users": None,
}

# =========================================================
# 🌟 PROFILE METADATA
# =========================================================

PROFILE = {
    "title": "Digital Pioneer | AI Visionary | Supreme Owner",
    "bio": "Creator of SUPREMESETUHUB. Building the next generation of digital ecosystems.",
    "avatar_type": "PREMIUM",
    "badge_supreme": True,
    "badge_verified": True,
    "badge_official": True,
    "profile_visibility": "OWNER_ONLY",
    "two_factor_enabled": True,
    "dashboard_name": "🔱 🕉️ SUPREME SHIV SHAKTI SYSTEM 🕉️ 🔱",
    "dashboard_theme": "SUPREME",
    "system_version": "1.0.0"
}

# =========================================================
# 🏠 HOMEPAGE CONFIGURATION
# =========================================================

HOMEPAGE = {
    "style": "SUPREME_SOCIAL",
    "layout": "COMBINED_FEED",
    "supreme_owner_featured": True,
    "show_all_names": True,
    "show_connected_repos": True,
    "multi_identity_display": True,
    
    "features": [
        "HOME_FEED",
        "EXPLORE",
        "STORIES",
        "MESSAGES",
        "NOTIFICATIONS",
        "PROFILE",
        "COMMUNITIES",
        "THREADS"
    ],
    
    "social_platforms": [
        "FACEBOOK_STYLE",
        "INSTAGRAM_STYLE",
        "WHATSAPP_STYLE",
        "LINKEDIN_STYLE",
        "REDDIT_STYLE",
        "TELEGRAM_STYLE",
        "THREADS_STYLE"
    ],
    
    "theme": "PREMIUM_DARK"
}

# =========================================================
# 🔐 SECURITY CONFIGURATION
# =========================================================

SECURITY = {
    "password_hash_method": "PBKDF2-SHA256",
    "session_timeout_minutes": 3600,
    "max_login_attempts": 5,
    "account_lockout_duration_minutes": 30,
    "password_expiry_days": 90,
    "require_email_verification": True,
    "require_phone_verification": True,
    "two_factor_enabled": True
}

# =========================================================
# 🚀 INITIALIZATION
# =========================================================

STARTUP_TASKS = {
    "initialize_database": True,
    "create_supreme_owner": True,
    "create_default_modules": True,
    "load_connected_repos": True,
    "enable_social_integration": True,
    "enable_ai_services": True,
    "setup_homepage": True,
    "configure_branding": True,
    "sync_all_repos": False,  # Keep cross-repository sync disabled until verified
}

# =========================================================
# 📝 SYSTEM STATUS
# =========================================================

SYSTEM_INFO = {
    "app_name": APP_NAME,
    "version": APP_VERSION,
    "phase": "Foundation Architecture",
    "status": "Active Development",
    "created_at": CREATED_AT,
    "last_updated": datetime.now().isoformat(),
    "supreme_owner": SUPREME_OWNER["primary_display_name"],
    "connected_repos": len(CONNECTED_REPOS),
    "alias_names": len(SUPREME_OWNER["display_names"]),
    "mode": "UNIFIED_SUPREME"
}

# =========================================================
# 📡 AUTO-SYNC CONFIGURATION
# =========================================================

REPO_SYNC = {
    "auto_sync_enabled": False,  # Registry-only mode; no credentials or sync worker are assumed.
    "sync_interval_minutes": 60,
    "repos_to_sync": [],  # Explicit opt-in after per-repository sync permissions are configured.
    "sync_content": [
        "README",
        "CONFIG",
        "PROFILE_DATA",
        "STATISTICS"
    ]
}
import os

PORT = int(os.environ.get("PORT", 8000))
# Backward-compatible ID aliases
SUPREME_ID = SUPREME_OWNER["supreme_id"]
BUSINESS_ID = SUPREME_OWNER["business_id"]
COMPANY_ID = SUPREME_OWNER["company_id"]
PERSON_ID = SUPREME_OWNER["person_id"]
INTERNAL_USER_ID = SUPREME_OWNER["internal_user_id"]
USERNAME = SUPREME_OWNER["primary_username"]
DISPLAY_NAME = SUPREME_OWNER["primary_display_name"]
