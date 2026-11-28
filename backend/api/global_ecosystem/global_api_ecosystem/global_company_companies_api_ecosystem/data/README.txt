GLOBAL COMPANY REGISTRY DATA POLICY

Add only records supported by a traceable source URL. Never invent registration
numbers, legal status, headquarters, websites, or verification claims.

Each record must include:
- company_id: stable unique internal identifier
- name: registered or commonly used organization name
- entity_type: one of the entity classes in company_taxonomy.json
- verification_status: unverified, source_checked, registry_verified,
  identity_verified, or suspended
- source_urls: list of evidence URLs (required for source_checked and above)

Recommended provenance:
- Prefer official government company registries for legal identity and status.
- Prefer official company websites for names, products, and public contact details.
- Record last_verified_at as an ISO 8601 timestamp when a human or trusted
  ingestion process last checked the source.
- Treat a directory listing or search snippet as discovery evidence, not legal
  verification.
- Keep country-specific registration identifiers in country-specific extensions;
  do not assume one global registration-number format.

The JSON registry is currently intentionally empty. An empty dataset is not
evidence that no companies exist.


COUNTRY SOURCE DIRECTORY

The adjacent country_sources.json file is a curated directory of official or
regulator-operated company-data sources. It records source scope, access method,
authentication expectations, limitations and adapter status. It does not mean
that SUPREMESETUHUB has connected to those sources or has permission to bulk
retrieve their data.

Before implementing an adapter, confirm the current source terms, API
credentials, fair-use/rate limits, permitted fields and update schedule. Keep
source metadata separate from company records. Only add a company record after
retrieval and validation from an authorised source, preserving the source URL
and retrieval/verification timestamp.
