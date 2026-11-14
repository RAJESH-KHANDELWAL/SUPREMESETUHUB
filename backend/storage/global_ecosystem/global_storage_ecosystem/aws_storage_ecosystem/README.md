# Amazon S3 — STORAGE ECOSYSTEM

This is the canonical ecosystem-owned location for the Amazon S3 provider.

## Current state

- Provider service scaffold is placed in this ecosystem folder.
- The service currently reports `not_configured`; this is not a live connection.
- Live integration requires the provider's supported API/client, owner-authorized credentials, permissions, and end-to-end tests.

## Security

Store credentials only in backend runtime secrets/environment. Never commit API keys, passwords, OAuth refresh tokens, private keys, or FTP credentials.

## Completion criteria

Implement authenticated health checks, object listing, streaming upload/download, delete, checksum verification, and mocked offline tests before marking this provider connected.
