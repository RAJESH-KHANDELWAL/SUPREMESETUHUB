# GLOBAL CONNECTION ECOSYSTEM

Central connection orchestration for SUPREMESETUHUB.

## Responsibilities
- Register provider, service, and server connection metadata.
- Track authorization and connection lifecycle state.
- Delegate actual connect/disconnect I/O to explicitly injected adapters.
- Report aggregate diagnostics without exposing credentials.

## Architecture boundary
The existing `backend/connection/manager.py` remains the base connection state manager. This ecosystem coordinates it and dispatches provider I/O through adapters. It does not implement provider SDKs or claim a live connection when no adapter is configured.

## Safety
Authorization requires an explicit approval flag. Credentials must be supplied to provider adapters through a secure runtime secret mechanism and must never be committed to Git or logged.
