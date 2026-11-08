# GOOGLE GMAIL ENGINE

**Engine ID:** `GOOGLE-GMAIL-ENGINE`  
**Core module:** `GOOGLE-GMAIL-CORE-ECOSYSTEM`

## Responsibility

Gmail engine orchestration and provider operation facade. It delegates to the existing Gmail Core service and API adapter rather than reimplementing OAuth or Gmail API transport.

## Current operations

- Read sanitized configuration and connection status.
- Return authorization URL and state for a trusted, authenticated OAuth flow.
- Complete an authorization code flow with state validation.
- Send email only on an explicit caller action after mailbox authorization.

## Safety and status

The existing API adapter currently requests `gmail.send` only. A live mailbox connection is not asserted by this engine package. Existing single-mailbox token-file storage is a setup scaffold; multi-user production requires encrypted tenant-scoped token storage, authenticated callback binding, disconnect/revocation, audit logging and operational controls.
