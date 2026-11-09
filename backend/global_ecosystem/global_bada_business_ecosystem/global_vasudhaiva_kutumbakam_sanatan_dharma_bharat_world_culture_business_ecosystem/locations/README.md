# Geography and Place Registry

**Namespace:** `locations/`

Country, region, state, city, venue, heritage site and service-area metadata. Publish only verified public details; respect restricted sites.

## Required controls
- Stable record ID and accountable owner.
- Source evidence, provenance and verification status where relevant.
- Created, updated and review timestamps with lifecycle status.
- Permission, license, consent and retention notes where relevant.
- Public/private field separation and access requirements.
- Correction, suspension, archival and audit procedures.

## Architecture boundary
Business-domain records and requirements only. API, CORE, ENGINE, AI, DATABASE, STORAGE, authentication, payments and APP implementation remain in their respective layers. Never store secrets or sensitive personal data here.
