# Adobe Catalog Audit

## Source snapshot

Reviewed on 2026-11-16:
- [Adobe global product catalog](https://www.adobe.com/products/catalog.html): page reports 100 results and Adobe states it offers nearly 100 products.
- [Adobe for Business product catalog](https://business.adobe.com/products.html): page reports 43 results.

The machine-readable `adobe_product_inventory.json` merges named entries visible in both pages and de-duplicates names. It marks versioned, legacy, uncertain-lifecycle and partner entries separately. Catalog counts are source-page result counts, not counts of unique standalone software products; bundles, editions, services, platforms and capabilities can all appear as catalog entries.

## What this audit does and does not establish

- Establishes a broad named inventory from the two official Adobe catalog pages.
- Does not assert that every listing is independently purchasable or has a public API.
- Does not infer lifecycle state from a product name alone.
- Does not include every capability, plan, SKU, beta, retired product, acquired brand, regional variation or undocumented internal service.
- Requires periodic re-crawl and per-product lifecycle/API verification to maintain completeness.

## Core package coverage

All 32 canonical Core domains have a package scaffold with the ten standard directories. A scaffold is not a production implementation and does not imply live Adobe connectivity.
