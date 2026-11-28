# Beauty, Fashion & Lifestyle API Ecosystem

Stable package ID: `beauty_fashion_lifestyle`

This canonical package currently provides a beauty-products and beauty-sector discovery taxonomy for Bharat (India) and global markets. It exposes 20 business domains mapped to 17 API categories.

## Business-domain coverage

1. Beauty & Cosmetics
2. Skincare Products
3. Haircare Products
4. Makeup Products & Professional Supplies
5. Fragrance & Perfume
6. Nail Beauty Products
7. Beauty Tools & Devices
8. Beauty Ingredients & Formulation
9. Beauty Manufacturing & Private Label
10. Beauty Packaging & Components
11. Beauty Product Testing & Compliance Information
12. Beauty Wholesale & Bulk Supply
13. Beauty Distribution & Import/Export
14. Beauty Retail & Stores
15. Beauty E-commerce & Marketplaces
16. Clean, Ethical & Sustainable Beauty
17. Beauty Technology & Digital Platforms
18. Beauty Education & Product Training
19. Beauty Brands, Marketing & Brand Services
20. Professional Beauty & Salon Supplies

## Scope boundaries and canonical ownership

- Fashion design, clothing/apparel, textiles, footwear, leather goods and fashion retail remain owned by the separate `fashion_textiles_apparel` ecosystem. This package does not create a second fashion catalog.
- General salon, barber, spa, massage and personal-care service discovery remains in `personal_lifestyle_wellness`. This package covers beauty products, professional supplies, sector education and related business operations.
- Clinical dermatology, diagnosis, prescription treatment and medical procedures belong to Healthcare & Life Sciences. Skincare product discovery here is nonclinical.
- Product testing, ingredient and regulatory entries are informational taxonomy only. They do not certify safety, validate claims, grant licenses or establish regulatory compliance.
- Brand, supplier, manufacturer and marketplace entries are not independently verified by this taxonomy.

## API endpoints

- `GET /industries/beauty-fashion-lifestyle/status`
- `GET /industries/beauty-fashion-lifestyle/categories`
- `GET /industries/beauty-fashion-lifestyle/categories?q=...`
- `GET /industries/beauty-fashion-lifestyle/categories/{category_id}`
- `GET /industries/beauty-fashion-lifestyle/domains`
- `GET /industries/beauty-fashion-lifestyle/domains?q=...`
- `GET /industries/beauty-fashion-lifestyle/domains/{domain_id}`

## Implementation status

`taxonomy_scaffold` — category/domain discovery endpoints only. Parent-application router registration, integration tests, live listings, provider verification, product validation and regulatory workflows are not implied.
