# Arts, Culture, Heritage & Creative Economy API Ecosystem

**Stable ID:** `arts_culture_heritage_creative_economy`  
**Canonical package:** `industry_api_ecosystems/arts_culture_heritage_creative_economy/`  
**Coverage target:** India + Global  
**Channels:** Online, Offline and Hybrid  
**Implementation status:** Taxonomy/API scaffold

A dedicated taxonomy for arts, living culture, tangible and intangible heritage, cultural institutions, traditional crafts, cultural education and creative-economy enterprises.

## Scope

The ecosystem covers visual and fine arts; theatre and performing arts; music, dance and traditional performance; museums, galleries, libraries and archives; monuments, archaeological sites and heritage landscapes; conservation and restoration; handicrafts and artisan enterprises; folk, indigenous and community arts; cultural institutions; festivals and exhibitions; languages, literature and oral traditions; arts education and apprenticeships; digital cultural preservation; cultural entrepreneurship; and cultural policy and impact research.

## API endpoints

Mounted through the existing industry API router:

- `GET /industries/arts-culture-heritage/status`
- `GET /industries/arts-culture-heritage/categories` — optional `q` and `channel` filters.
- `GET /industries/arts-culture-heritage/categories/{category_id}`

## Boundaries with adjacent ecosystems

- Marketing, advertising, commercial film/video, broadcasting, creator services, music distribution, gaming and entertainment production remain in `marketing_media_entertainment`.
- Travel booking, accommodation, tour operators and visitor logistics remain in `travel_tourism_hospitality`. This ecosystem classifies cultural assets and heritage interpretation, not travel inventory.
- Fashion retail and commercial apparel brands remain in `fashion_textiles_apparel`; traditional craft heritage and artisan production are classified here where cultural preservation is central.
- Formal general education delivery remains in `education_learning_training`; this package covers arts-specific learning, heritage skills and cultural apprenticeships.
- Sports and recreation remain in `sports_recreation_community`.

## Data and verification limits

This is a taxonomy/API scaffold, not a verified directory of museums, monuments, artists, artisans, cultural organisations, events, grants or heritage properties. It does not confirm ownership, legal protection, condition, authenticity, provenance, conservation status, event schedules, funding availability or practitioner credentials. Cultural rights, community consent, Indigenous knowledge protections and applicable heritage laws require source-specific review before records are published.
