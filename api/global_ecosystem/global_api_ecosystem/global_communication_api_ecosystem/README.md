# Global Communication API Ecosystem

A country-aware catalog and integration scaffold for communication providers and adjacent adult-only platform categories in SUPREMESETUHUB.

## Scope

- Core communication: messaging, email, SMS/OTP, voice, video meetings, social/community messaging, customer support, notifications.
- Adjacent services: dating and relationships, sexual-wellness education, adult-platform directory, adult-creator business tooling.
- Platform foundations: age verification, consent, moderation, privacy, security and identity.
- Coverage metadata is designed for India (IN) and global regions. Provider availability and legal permissions must be verified per country.

## API routes

When the router is mounted by the parent FastAPI application:

- `GET /global-communication/status`
- `GET /global-communication/categories`
- `GET /global-communication/categories/{category_id}`
- `GET /global-communication/providers`

## Integration truthfulness

All providers are initially `not_configured`; `connected_provider_count` is 0 and `live_messaging_enabled` is false. A provider appearing in this catalog does not mean an API connection exists. Before enabling an adapter, verify official API access, terms, regional availability, OAuth scopes, webhook signatures, rate limits, data retention, and end-to-end tests. Keep secrets in a server-side secret manager; never commit credentials.

## Adult-category safeguards

Adult categories are catalog metadata only and disabled by default. Any future implementation must enforce verified 18+ access, consent, lawful content, regional restrictions, privacy-by-design, reporting and appeals. No minors, non-consensual material, exploitation, or illegal content is permitted. Do not expose adult routes or content until legal and security review is complete.

## Current limitation

This commit provides catalog/status endpoints and safety policy metadata. It does not send messages, process payments, verify identities, host content, or connect provider APIs. Those capabilities require separate provider-specific adapters, credentials, permissions, webhook configuration, and tests.
