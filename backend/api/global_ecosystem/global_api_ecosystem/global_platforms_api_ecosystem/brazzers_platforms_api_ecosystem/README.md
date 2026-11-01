# BRAZZERS — PLATFORM PROVIDER PACKAGE

## Package role
Provider-specific discovery and classification metadata for the Global Platforms ecosystem. This package is a provider mapping, not proof of a verified platform profile or a live API connection.

## Classification
- Provider ID: `brazzers`
- Platform family: Lawful adult-industry platform family (18+)
- Adult-only: Yes — exclude from general discovery by default
- Current implementation boundary: catalog metadata only until source URLs, legal/operator identity, supported products and official API documentation are verified.

## Standard package contract
- Existing provider metadata module: `brazzers_platforms_api_ecosystem.py`
- `README.md`: scope and evidence boundary
- `__init__.py`: package marker

Do not represent a provider folder as a working integration. Do not infer ownership or legal-company details from the provider name. Link platform profiles to Company/Enterprise records through the shared entity-relationship registry.

Adult-industry records require jurisdiction-aware restrictions, age assurance, consent and safety controls. Adult catalogue visibility remains opt-in; this package does not implement age verification.
