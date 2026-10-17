# google ecosystem

The Google domain directory is `backend/google/`. The Google Ecosystem directory
is `backend/google/google_ecosystem/`.

## Requested file layout

```text
backend/
├── google.py
├── google.php
└── google/
    ├── google_ecosystem.py
    ├── google_ecosystem.php
    └── google_ecosystem/
        ├── __init__.py
        ├── service.py
        └── README.md
```

The Python facades expose `list_products()`, `get_product()`, and `get_status()`.
The PHP client calls the authenticated SUPREMESETUHUB catalog API. The canonical
catalog lives in `service.py`; avoid maintaining duplicate product lists in facades.

## Catalog coverage

The catalog now contains 129 entries across these product families:

- **Workspace and communication:** Gmail, Drive, Calendar, Docs, Sheets, Slides,
  Meet, Chat, Contacts, Tasks, Forms, Groups, Workspace Admin, Vault, Classroom,
  Assignments, AppSheet, Apps Script, and related services.
- **Cloud and infrastructure:** Google Cloud, Compute Engine, Cloud Run, Cloud
  Functions, Cloud SQL, Cloud Storage, Cloud DNS, Kubernetes Engine, IAM, Secret
  Manager, KMS, Logging, Monitoring, Build, Artifact Registry, networking, Dataflow,
  Dataproc, Composer, App Engine, and BigQuery.
- **AI and developer tools:** Gemini, Vertex AI, Vertex AI Search, AI Studio, Colab,
  Dialogflow, Natural Language, Speech-to-Text, Text-to-Speech, Vision, Document AI,
  Video Intelligence, and related APIs.
- **Firebase and app development:** Authentication, Firestore, Realtime Database,
  Hosting, App Distribution, Crashlytics, Remote Config, Performance Monitoring,
  Cloud Messaging, App Check, Play Console, Play Integrity, and Android Management.
- **Search, analytics, ads and commerce:** Search, Search Console, Analytics, Tag
  Manager, Google Ads, AdSense, AdMob, Ad Manager, Merchant Center, Shopping,
  Business Profile, Wallet, Pay, and Play services.
- **Maps, media, consumer and devices:** Maps, Places, Routes, Geocoding, Street View,
  Elevation, Time Zone, YouTube, YouTube Analytics, Photos, Books, News, Travel,
  Flights, Arts & Culture, Pixel, Nest, and other product families.

The exact catalog is the source of truth in `service.py`. “All products” here means
a broad catalog of major known products and API families, not a guarantee that every
regional, renamed, discontinued, private, or newly released Google offering is listed.
API access, quotas, scopes, billing, account eligibility, and product availability vary.

## API

- `GET /api/v1/google-ecosystem/status`
- `GET /api/v1/google-ecosystem/products`
- `GET /api/v1/google-ecosystem/products/{product_id}`

All endpoints require a SUPREMESETUHUB ADMIN/OWNER bearer session.

## Connection and security boundary

The catalog is metadata, not proof of a live Google account connection. OAuth callback
and state validation, encrypted per-user token storage, revocation, and provider API
adapters must be implemented and verified before live user-data operations are enabled.

The PHP client requires server-side `SUPREMESETUHUB_API_BASE_URL` and
`SUPREMESETUHUB_ADMIN_TOKEN` environment variables, HTTPS, and PHP cURL. Never expose
bearer tokens in browser code or commit credentials. Google Cloud credentials must use
a separate least-privilege Cloud identity rather than consumer Gmail permissions.
