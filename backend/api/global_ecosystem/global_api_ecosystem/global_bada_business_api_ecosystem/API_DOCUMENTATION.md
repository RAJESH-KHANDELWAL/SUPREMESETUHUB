# Universal Work & Business Taxonomy API

Base path: `/api/v1/global-ecosystem/business/work-business-taxonomy`

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/status` | Version and integrity summary |
| GET | `/sectors` | A–Z sector catalogue |
| GET | `/sectors/{sector_id}` | Sector detail |
| GET | `/sectors/search?q=...` | Search sectors and subgroup labels |
| GET | `/facets` | Work models, audience groups and delivery modes |
| GET | `/integrity` | Structural catalogue checks |

Responses are taxonomy-only. No live listings, official code equivalence or legal coverage are asserted.
