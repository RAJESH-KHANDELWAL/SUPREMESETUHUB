"""Bitbucket Cloud API catalog metadata; no live connector is implemented here."""

PROVIDER_ID = "atlassian"
API_FAMILY_ID = "BITBUCKET"
NAME = "Bitbucket Cloud API"
SCOPE = "Workspaces, repositories, source, pull requests, commits, pipelines and deployment metadata."
AUTHENTICATION = "Bitbucket OAuth or supported workspace/repository access token; scope and workspace permissions apply."
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
LIVE_CONNECTION_VERIFIED = False
