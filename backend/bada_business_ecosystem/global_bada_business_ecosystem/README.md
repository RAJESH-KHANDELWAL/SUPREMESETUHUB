# GLOBAL BADA BUSINESS ECOSYSTEM

Canonical Bada Business ecosystem package under backend/bada_business_ecosystem/.

This folder is the requested child ecosystem package. It owns the provider-specific Bada Business platform resource catalog, resource metadata and program snapshots.

## Package structure

- platform_resources/catalog.py — platform links, provider profile and program catalog
- platform_resources/programs/lfp_digital.py — LFP Digital record
- platform_resources/programs/bb_impact.py — BB Impact record
- platform_resources/programs/idea_to_ipo.py — Idea to IPO record

## API integration

The broad GLOBAL BADA BUSINESS API implementation remains in the API layer at backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/. Its router is exposed at backend/bada_business_ecosystem/api_ecosystem/. This separation preserves the API transport layer and existing router imports; no physical API mega-tree move is claimed here.

## Data verification

Links and program snapshots are resource metadata from existing repository references and user-supplied content. They do not establish official API access, commercial partnership, current price, event availability or live integration.
