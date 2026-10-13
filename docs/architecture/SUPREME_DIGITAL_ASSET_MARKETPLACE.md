# SUPREME Digital Asset Marketplace

This is a digital-download-only marketplace foundation. It is not a print-on-demand storefront and does not depend on printers, physical inventory, shipping, or fulfillment.

## Catalog capabilities

- Flexible categories and asset types (images, illustrations, wallpapers, templates, icon packs, clipart, patterns, 3D assets, documents, fonts, audio, video, bundles, and future types).
- Preview URL, title, description, tags, file format, license label, and owner-managed publication status.
- Separate India (INR) and Global (USD) price rows, stored as minor currency units (paise/cents).
- Public catalog search, category filter, pagination, and public preview metadata.
- Private file keys are never included in public catalog responses.
- Existing databases are migrated additively; no existing rows are intentionally deleted.

## API

- `GET /api/v1/digital-marketplace/catalog?market=IN&category=digital-art&search=cosmic&limit=24&offset=0`
- `GET /api/v1/digital-marketplace/catalog?market=GLOBAL`
- `POST /api/v1/digital-marketplace/designs` — owner-only through the application's private-by-default middleware.

Example owner-managed listing payload:

```json
{
  "title": "Bharat Cosmic Art Pack",
  "description": "Original digital art bundle",
  "category": "digital-art",
  "asset_type": "BUNDLE",
  "file_format": "ZIP",
  "preview_url": "https://your-cdn.example/previews/cosmic.webp",
  "private_storage_key": "private/digital/cosmic-art-pack.zip",
  "license_label": "Personal digital use",
  "tags": ["space", "abstract", "bharat"],
  "prices": {"IN": 19900, "GLOBAL": 499},
  "status": "DRAFT"
}
```

Prices are integer minor units: `19900` means INR 199.00; `499` means USD 4.99. Use a real HTTPS preview asset URL and a storage key that points to private storage. Never place a paid master file at a public URL. Change `status` to `PUBLISHED` only after confirming asset rights, preview quality, file integrity, and license terms.

## Explicitly not enabled yet

- AI image-generation provider/API and image upload pipeline.
- Real product image/preview files or a CDN bucket.
- Customer checkout/payment gateway.
- Signed/expiring downloads granted only after verified payment.
- Receipts, refunds, tax calculation, purchase library, download limits, and end-to-end order tests.
- Live deployment on Render or WordPress/Hostinger.

Payment must be confirmed server-side using a provider-verified webhook before granting download access. A browser redirect or a client-supplied `paid=true` flag must never unlock a file. Webhook signature verification and idempotent order processing are required before production sales.
