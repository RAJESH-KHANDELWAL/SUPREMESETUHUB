# Retail, E-commerce, Consumer Goods & Electronics API Ecosystem

Stable ID: `retail_ecommerce_consumer_goods`.

India/global taxonomy across online, offline and hybrid channels. The package maintains 12 canonical categories and exposes 20 business domains, including a detailed consumer-electronics and home-appliances coverage.

## 20 business domains

1. General & Specialty Retail
2. E-commerce & Marketplaces
3. Wholesale & Distribution
4. Consumer Packaged Goods
5. Fashion, Apparel & Accessories
6. Consumer Electronics
7. Smartphones, Computers & Mobile Devices
8. Home & Kitchen Appliances
9. Smart Home & Connected Devices
10. Audio, Visual & Gaming Equipment
11. Cameras & Imaging Equipment
12. Beauty & Personal Care Goods
13. Grocery & Food Retail
14. Home, Furniture & Lifestyle Goods
15. Retail Technology & POS
16. E-commerce Fulfilment & Last Mile
17. Franchise & Store Networks
18. Electronics Repair & After-Sales Services
19. Refurbished & Second-Hand Electronics
20. Electronics Recycling & E-Waste

## Electronics coverage

The `electronics_appliances` category covers smartphones, computers, tablets, displays, audio equipment, cameras, gaming, major and small home appliances, wearables, smart-home devices, networking equipment, accessories, repair, refurbishment, trade-in and e-waste pathways.

## Ownership and scope boundaries

- This is the canonical discovery taxonomy for consumer electronics, home appliances and consumer-goods retail in this repository. No separate overlapping consumer-electronics ecosystem is created.
- Fashion and apparel discovery is linked at category level; detailed fashion/textile production and industry services remain owned by `fashion_textiles_apparel`.
- Beauty product and beauty-sector operations remain owned by `beauty_fashion_lifestyle`; this package only retains a retail-level consumer-goods category.
- Device repair and after-sales entries are discovery classifications, not proof of manufacturer authorization, warranty eligibility or service quality.
- Smart-home categories do not imply device interoperability, cybersecurity certification or live IoT connectivity.
- Refurbishment, recycling and e-waste entries do not certify product condition or authorize regulated waste handling.
- No live inventory, seller verification, product testing, payments or fulfilment integration is included.

## API endpoints

- `GET /industries/retail-ecommerce-consumer-goods/status`
- `GET /industries/retail-ecommerce-consumer-goods/categories`
- `GET /industries/retail-ecommerce-consumer-goods/categories?q=...`
- `GET /industries/retail-ecommerce-consumer-goods/categories/{category_id}`
- `GET /industries/retail-ecommerce-consumer-goods/domains`
- `GET /industries/retail-ecommerce-consumer-goods/domains?q=...`
- `GET /industries/retail-ecommerce-consumer-goods/domains/{domain_id}`

## Implementation status

`taxonomy_scaffold` — category and domain discovery endpoints only. Parent application router registration, integration tests, verified listings, inventory, payments and fulfilment workflows remain separate implementation tasks.
