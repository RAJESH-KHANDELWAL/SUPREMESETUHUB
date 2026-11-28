"""Twilio provider API ecosystem metadata; catalog only, not a live connector."""

PROVIDER_API_ECOSYSTEM = {
    "provider_id": "twilio",
    "name": "TWILIO API ECOSYSTEM",
    "vendor": "Twilio",
    "families": ["COMMUNICATION", "TOOLS"],
    "capabilities": [
        "messaging",
        "voice",
        "verification",
        "programmable_communications",
    ],
    "scope": (
        "Catalog of Twilio communication capabilities. Actual product access depends "
        "on the Twilio account, enabled products, sender registration, and applicable regions."
    ),
    "implementation_status": "CATALOG_ONLY",
    "api_documentation_verified": False,
    "credentials_configured": False,
    "adapter_implemented": False,
    "adapter_tests_passed": False,
    "live_connection_verified": False,
}
