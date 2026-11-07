# Professional Services API Ecosystem

Canonical package ID: `professional_legal_business_services` (stable technical identifier retained for backward compatibility).

A unified discovery taxonomy for non-legal professional services, including accounting, taxation support, audit and assurance, management consulting, HR, architecture and design consultancy, engineering/project consultancy, translation, BPO, virtual administration, professional documentation, and business research/analytics.

- Coverage labels: India and global
- Channels: online, offline and hybrid
- Categories: 12
- Status: `taxonomy_scaffold`

## Endpoints

- `GET /industries/professional-legal-business-services/status` (legacy-compatible route)
- `GET /industries/professional-legal-business-services/categories`
- `GET /industries/professional-legal-business-services/categories?q=...`
- `GET /industries/professional-legal-business-services/categories/{category_id}`

## Scope boundaries

Legal advice, lawyers, litigation, legal documentation, company-law practice and legal representation belong to the separate Legal API Ecosystem and are excluded here. Marketing and advertising belong to Marketing, IT/software implementation belongs to Technology, procurement and sourcing belong to Supply Chain, and product testing/certification belongs to the relevant industrial or quality domain.

This package is a discovery taxonomy only. It does not claim live listings, provider verification, professional licensing, regulatory approval, or quality certification. Regulated work must be delivered by appropriately qualified and authorized professionals.
