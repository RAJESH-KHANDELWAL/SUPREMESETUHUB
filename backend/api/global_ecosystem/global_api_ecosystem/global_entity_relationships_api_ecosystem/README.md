# GLOBAL ENTITY RELATIONSHIPS API ECOSYSTEM

A shared, source-aware relationship registry connecting entities across India and global ecosystems without duplicating canonical identities.

## Existing relationship types
`owns`, `operates`, `publishes`, `distributes`, `parent_of`, `subsidiary_of`, `brand_of`, `founded_by`, `partner_of`, `resells`.

## Extended developer and adult-industry relationship types
- `provides_api_to` — provider supplies an authorized API to a platform
- `hosts_content_for` — hosting provider hosts a platform's lawful content
- `licenses_content_to` — rights-holder licenses content to a platform
- `age_verifies_for` — age-assurance provider verifies eligibility for a service
- `verifies_consent_for` — consent/rights workflow provider supports a platform
- `moderates_for` — trust-and-safety provider moderates a platform
- `processes_payments_for` — authorized payment provider processes payments
- `handles_payouts_for` — authorized payout provider handles creator/business payouts
- `provides_safety_support_to` — safety/reporting provider supports a platform
- `supplies_technology_to` — technology vendor supplies software/services
- `affiliated_with` — documented affiliation, not an ownership claim

## Entity domains covered
- India and international companies, corporate groups, brands and digital platforms.
- Developer/API providers, cloud/AI/data vendors, payment providers and identity vendors.
- Dating and relationship services for adults.
- Sexual-wellness education providers.
- Lawful 18+ platform directories and adult-creator business service providers.
- Age-assurance, consent, moderation, reporting and safety vendors.

## Capability tiers
- **Normal:** basic entity records and relationship lookup.
- **Standard:** source links, provider classifications and status metadata.
- **Advanced:** cross-platform relationship mapping and verification workflows.
- **Enterprise:** audit history, role-based review, regional policy and governance.
- **Supreme:** provenance tracking, change history, multi-region policy controls and high-availability registry design.

## India and global compliance
Store the jurisdiction(s) where an entity operates and the applicable legal review status. Do not assume a provider is available in India or globally without checking its official terms and local law. Adult-related services must be lawful, restricted to adults aged 18+, and based on consent. Exclude minors, non-consensual intimate imagery, exploitation, trafficking and illegal sexual content.

## Data integrity
Each edge requires a stable relationship ID, source and target entity IDs, relationship type and verification status. Verified edges require source URLs. Never infer ownership, affiliation, consent, licensing or API access from a name or directory listing. The registry remains read-only and starts empty; no relationship is asserted until evidence is supplied and reviewed.

## Endpoints
- `GET /api/v1/global-api-ecosystem/global/entity-relationships/status`
- `GET /api/v1/global-api-ecosystem/global/entity-relationships?entity_id=...&relationship_type=...`

This registry catalogs relationships; it does not itself host adult content, verify age, process payments, or connect external APIs. Those functions require separate authorized integrations and tests.
