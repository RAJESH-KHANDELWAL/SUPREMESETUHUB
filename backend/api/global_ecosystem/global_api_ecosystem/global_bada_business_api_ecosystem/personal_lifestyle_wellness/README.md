# Personal, Couple, Family, Relatives, Friends, Relationships, Adult Intimacy, Health, Wellness & Lifestyle API Ecosystem

Canonical ID: `personal_lifestyle_wellness`. One unified taxonomy covering personal life, couples, family, relatives, friends, relationships, adult intimacy, sexual health, personal health, wellness and lifestyle. Adult-only categories remain separately restricted.

- Total categories: 23
- Default public discovery: 21 general categories
- Restricted categories: 2, classified as `18_plus_restricted`
- Coverage labels: India and global
- Channels: online, offline, hybrid
- Status: `taxonomy_scaffold`

## API endpoints

- `GET /industries/personal-lifestyle-wellness/status`
- `GET /industries/personal-lifestyle-wellness/categories`
- `GET /industries/personal-lifestyle-wellness/categories?q=...`
- `GET /industries/personal-lifestyle-wellness/categories?include_adult=true`
- `GET /industries/personal-lifestyle-wellness/categories/{category_id}?include_adult=true`

## Adult-content and safety boundary

Adult intimacy/sexual-wellness and adult-content publishing categories are separately marked `18_plus_restricted` and excluded from default discovery. Any future access layer must implement reliable age assurance, jurisdiction checks, lawful operation, performer age verification, informed consent, content-rights clearance, privacy and reporting controls. The query flag is only a taxonomy inclusion switch; it is not age verification or legal authorization.

No minors, non-consensual material, coercion, trafficking, exploitation, or unlawful sexual services are included. This taxonomy does not host explicit content or verify providers, licences, clinical credentials or legal compliance. Counselling and healthcare services require appropriately qualified professionals.
