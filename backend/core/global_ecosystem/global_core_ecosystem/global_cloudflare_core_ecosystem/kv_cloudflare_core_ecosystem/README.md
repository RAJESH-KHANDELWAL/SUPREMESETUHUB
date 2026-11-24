# Cloudflare Product Core Package

This is a product-specific Core metadata package. The authoritative product ID, name, category and capability list are in `ecosystem_manifest.json`.

## Core ownership
Product identity, capability metadata, lifecycle/readiness contracts and policy boundaries belong here. Cloudflare REST transport, token handling and endpoint adapters remain in the API/provider adapter layer.

## Current status
`CORE_CATALOG_ONLY`. This package does not establish an authenticated Cloudflare account connection or prove entitlement to any product/API.

## Required before implementation
Verify official product/API documentation, account eligibility, least-privilege permissions, region/plan constraints and safe operation semantics. Add reviewed API-layer adapters and offline contract tests before controlled live tests.
