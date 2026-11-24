# Classification Standards Business API Ecosystem

This package separates official economic-activity classifications from the platform's discovery taxonomies. It is the standards layer for India + Global business discovery.

## Included standards and coverage

- **India NIC 2025** — MoSPI's current national industrial classification; 22 sections, 87 divisions, 257 groups, 463 classes and 1,887 subclasses as stated in the MoSPI/PIB release dated 18 November 2025. Six-digit national subclass structure; aligned with ISIC Revision 5 through the four-digit class level.
- **UN ISIC Revision 5** — international reference classification, published by the United Nations Statistics Division.
- **North American NAICS 2022** — country/region-specific classification for Canada, Mexico and the United States, with national variants.
- **NACE Rev. 2.1** — European Union economic activity classification.
- **Other national systems** — a versioned registry for national classifications (for example UK SIC, ANZSIC, JSIC and other country systems); entries are metadata until source datasets and licensing are verified.

## Data integrity rules

1. Preserve source codes and official labels verbatim in imported source tables.
2. Store source organisation, edition, release date, source URL, retrieval date, checksum and licence/terms.
3. Never assume a one-to-one mapping between different classification systems.
4. Store crosswalks as many-to-many, directional, version-specific relationships with mapping method and confidence.
5. Keep economic activities separate from occupations, products, services, legal entity types, business listings and job vacancies.
6. Do not represent an un-ingested classification as a complete dataset. Registry metadata is not the full code list.

## NIC 2025 source ingestion

Official source landing page: https://www.mospi.gov.in/classification
Official NIC 2025 workbook: https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763618655097_29a4a622-fa4c-47e9-abba-b549e27a1bbb_NIC_2025.xlsx
Official NIC 2025 publication PDF: https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf
Official MoSPI/PIB release: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2191142

The official workbook has not been copied into this repository in this commit. The importer validates a locally supplied workbook and produces normalized JSON; it does not fabricate the 1,887 rows. See `importers/nic2025.py`.

## API

Mounted below the existing Bada Business API:

- GET `/api/v1/global-ecosystem/business/classifications`
- GET `/api/v1/global-ecosystem/business/classifications/{classification_id}`
- GET `/api/v1/global-ecosystem/business/classifications/integrity`
- GET `/api/v1/global-ecosystem/business/classifications/countries`

These endpoints currently expose source-backed registry metadata, not the full NIC/ISIC/NAICS code records.
