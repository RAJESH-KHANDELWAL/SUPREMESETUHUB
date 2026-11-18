# Lawful Adult Media & Pornography Platforms (18+)

This module documents the **Lawful Adult Media & Pornography Platforms (18+)** domain in the Global People, Work & Life ecosystem.

## Scope
- India/Bharat and global classification where applicable
- Domain discovery and catalog metadata
- Online, offline and hybrid service models where relevant
- Normal, Standard, Advanced, Premium, Enterprise and Supreme capability tiers

## API source of truth
The canonical domain record and discovery behavior are maintained in the parent `catalog.py`, `service.py` and `routes.py` files. This folder is supporting documentation, not a separate API implementation.

## Safety and implementation
Any real service requires verified providers, appropriate professional qualifications where applicable, privacy and security controls, testing and jurisdiction-specific compliance.

## Adult-only safeguards (18+)
Lawful adult-only services must use verified adults who meet the applicable local age threshold, freely given and ongoing consent, performer rights, privacy by design, moderation, reporting and takedown processes. No minors, coercion, trafficking, exploitation, non-consensual intimate imagery or unlawful content.

## Classification contract

The API catalog references the canonical People Life CORE taxonomy at:
`backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/adult_media_pornography_18_plus/classification_taxonomy.json`.

Orientation labels are optional content metadata and require self-declared or authorised provenance. The API must not infer or store viewer orientation. Participant configuration is a separate field. Age assurance, informed consent, distribution rights, moderation and jurisdiction checks remain independent mandatory gates.
