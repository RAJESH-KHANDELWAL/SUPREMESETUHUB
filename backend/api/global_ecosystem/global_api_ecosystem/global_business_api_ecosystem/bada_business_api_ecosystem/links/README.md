# Bada Business Link Registry

Add public Bada Business links supplied by the owner. Do not invent URLs.

Supported link types:
- `official_website`
- `course`
- `product`
- `service`
- `referral`
- `affiliate`
- `partner`
- `support`
- `api_documentation`
- `developer_portal`
- `other`

Each record should contain: `id`, `title`, `link_type`, `url`, `status`, `source`, `last_checked_at` and optional `campaign`.

Use `pending_review` for newly submitted URLs. Promote to `verified_official` only after checking the destination and ownership.
