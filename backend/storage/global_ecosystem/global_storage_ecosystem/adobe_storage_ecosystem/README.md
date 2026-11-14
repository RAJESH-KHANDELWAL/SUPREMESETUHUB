# Adobe Storage Ecosystem

This package describes **Adobe-specific storage products, storage capabilities, asset types, and integration boundaries**. It is a provider ecosystem under the Global Storage Ecosystem; it is not the home for universal Bharat-to-Global domain taxonomies.

## Scope

Geographic coverage and maturity levels describe where Adobe storage capabilities may be used and the operational maturity of our own integration. They do not turn unrelated business, education, culture, healthcare, or adult-industry domains into Adobe products.

- `geography/`: Bharat, regional, and global applicability of Adobe storage services.
- `maturity_levels/`: Normal, Professional, Advanced, Enterprise, and Supreme implementation stages.
- `products/`: Adobe storage products and product-backed storage surfaces.
- `services/`: storage-related Adobe services and capabilities.
- `platforms/`: Adobe product platforms that expose or consume storage.
- `storage_capabilities/`: storage constructs such as projects, folders, files, cloud documents, libraries, brands, and assets.
- `domains/`: Adobe-relevant asset and workflow domains only.

## Adobe storage catalog

The catalog may include:
- Adobe Cloud Storage and Collaboration constructs: projects, folders, files, cloud documents, Creative Cloud Libraries, and brands.
- Creative Cloud cloud documents and libraries.
- Lightroom cloud photo and video storage.
- Adobe Express projects and brand assets.
- Frame.io media storage and collaboration (tracked separately from general Adobe Cloud Storage quota where applicable).
- Experience Manager Assets as an enterprise digital asset management capability.
- Workfront asset workflows and Adobe cloud-storage integrations.
- Document Cloud document storage.
- Adobe Cloud Drive as a desktop mount/sync client, not as a separate storage backend.

Product availability, API access, entitlements, quotas, and regional behavior must be verified against the relevant Adobe product documentation and customer plan before enabling a connector.

## Universal taxonomy boundary

Universal categories such as business, education, healthcare, culture, relationships, adult industry, and lawful adult media belong in their corresponding **Global Category Storage Ecosystems** at the parent level:
`backend/storage/global_ecosystem/global_storage_ecosystem/`.

They must not be represented as Adobe product domains merely because Adobe can store a file of that subject. The existing Global Adult/Intimacy/Health/Wellness Storage Ecosystem remains the category-level home for that subject matter.

## Integration status

This repository folder is a catalog and implementation scaffold. Adobe connectivity remains `NOT_CONFIGURED` until authorized credentials, product entitlements, scopes, organization permissions, live health checks, and required end-to-end read/write tests have succeeded. Never commit credentials or personal data.

## Separation of responsibilities

- API ecosystem owns Adobe API clients, OAuth, endpoints, scopes, and API operations.
- Storage ecosystem owns storage metadata, object/file models, storage lifecycle, provider storage adapters, and storage health state.
- Shared integration references may connect the two layers; their implementations must not be duplicated.
