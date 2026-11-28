"""Confluence Cloud API catalog metadata; no live connector is implemented here."""

PROVIDER_ID = "atlassian"
API_FAMILY_ID = "CONFLUENCE"
NAME = "Confluence Cloud API"
SCOPE = "Spaces, pages, content, attachments, labels, comments and content search."
AUTHENTICATION = "Atlassian OAuth 2.0 (3LO) for user-authorized access where supported; space/page permissions and scopes are mandatory."
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
LIVE_CONNECTION_VERIFIED = False
