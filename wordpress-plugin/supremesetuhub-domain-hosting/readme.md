# SUPREMESETUHUB Domain & Hosting

A small WordPress plugin that displays the SUPREMESETUHUB public domain and hosting service catalog from the Python/FastAPI backend.

## Requirements

- WordPress 6.2 or later
- PHP 7.4 or later
- A deployed SUPREMESETUHUB backend reachable over HTTPS

## Install

1. Upload and activate the `supremesetuhub-domain-hosting` plugin folder.
2. In WordPress Admin, open **Settings → SUPREMESETUHUB Domain & Hosting**.
3. Enter the backend's HTTPS base URL, without a trailing slash or endpoint path.
4. Add `[supremesetuhub_domain_hosting]` to a WordPress page.

## Important launch boundary

The catalog is **inquiry-only**. It does not claim live domain availability, live prices, payment processing, domain registration, or hosting provisioning. Those capabilities require an approved registrar/hosting provider integration, verified pricing and taxes, secure order ownership, payment webhooks, refunds, and operational support.

The plugin makes read-only HTTPS GET requests. It does not collect provider credentials or expose secret tokens in page markup.
