# GOOGLE GMAIL CORE ECOSYSTEM

**Ecosystem ID:** `GOOGLE-GMAIL-CORE-ECOSYSTEM`  
**Parent:** GOOGLE CORE ECOSYSTEM  
**Folder:** `backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_gmail_core_ecosystem/`

## Integration boundary

Google API catalog and adapter reference:

`backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_gmail_api_ecosystem/`

This package owns the provider-family Core identity, lifecycle boundary and capability metadata. API transport remains in the API layer; do not duplicate clients, OAuth token stores or API-key handling here.

## Status

`ADAPTER_SCAFFOLD_NOT_LIVE_VERIFIED`. Registry metadata is not proof of a live Google connection. Enable a service only after the correct Google Cloud project, API, consent/scopes or IAM policy, quota and deployment-level smoke tests have been verified.

## Gmail-specific boundary

The Core facade delegates to `../gmail_core.py`, which delegates to the existing Gmail API adapter. The current default OAuth scope is `gmail.send` only. Do not enable mailbox read scopes by default.

