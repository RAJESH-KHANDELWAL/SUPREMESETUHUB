"""Integration registry scaffold. No live external API is connected by this file."""
INTEGRATION_STATES = ("planned", "documentation_review", "approved", "connected", "suspended")
REQUIRED_BEFORE_CONNECTING = ("official_api_docs", "user_authorisation", "terms_review", "privacy_review", "security_review", "rate_limit_policy")
