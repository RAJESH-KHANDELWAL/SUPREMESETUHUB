# GOOGLE GMAIL CORE ECOSYSTEM

**Parent:** GOOGLE CORE ECOSYSTEM  
**Folder:** `google_core_ecosystem/gmail/`  
**Ecosystem ID:** `GOOGLE-GMAIL-CORE-ECOSYSTEM`

## Core contract

The Gmail Core module is the core-layer facade and lifecycle boundary for an explicitly authorized Google mailbox. The actual Gmail API client remains in:

`backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_gmail_api_ecosystem/service.py`

This avoids duplicate OAuth and Gmail API implementations.

## Capabilities

- OAuth authorization URL and state-validated callback handoff
- Gmail mailbox connection status
- Explicit user-requested email sending
- Gmail message and thread ID receipt
- Least-privilege scope policy, initially `gmail.send`
- Token refresh boundary and secure-storage integration boundary

## Setup

Use the existing Gmail API README for Google Cloud Console configuration and deployment environment variables. Tokens must be stored outside Git in an encrypted, tenant-scoped production secret store. The current adapter uses a single-mailbox file path and is therefore a setup scaffold, not a multi-tenant production token vault.

## Current status

Core facade implemented. Live OAuth connection and email delivery are not verified until the deployment completes OAuth consent and a controlled smoke test.
