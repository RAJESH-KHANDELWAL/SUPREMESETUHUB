# Domain catalog and capability taxonomy

## Classification model

Use a consistent hierarchy: **domain → subdomain → offering → provider/creator → resource → customer journey**. Assign stable IDs only when a governed registry exists. Do not invent provider records or treat illustrative examples as actual listings.

## 1. Heritage, culture and responsible tourism
- Heritage interpretation: context-rich tours, trails, visitor guides, museum and site interpretation.
- Community-led experiences: locally hosted activities with consent, fair compensation and visitor limits.
- Cultural itinerary services: planning, accessibility information, local transport coordination through authorized providers.
- Heritage hospitality: stays and food experiences with accurate cultural descriptions and transparent terms.
- Safeguards: site rules, community capacity, conservation limits, photography permissions and respectful conduct.

## 2. Arts, crafts, handloom and creative industries
- Artisan and maker discovery directories.
- Craft categories: textiles, handloom, pottery, metalwork, woodwork, painting, sculpture, jewelry, folk and contemporary art.
- Commissioning, custom orders, exhibitions and verified product catalogs.
- Creator profiles, portfolios, workshops and learning experiences.
- Safeguards: creator attribution, authenticity and provenance, fair pricing, design/IP protection, no misleading handmade or origin claims.

## 3. Education, language and lifelong learning
- Courses on history, philosophy, arts, literature, culture and regional knowledge.
- Language learning, translation, interpretation and literacy resources.
- Workshops, mentorship, seminars and teacher/learner directories.
- Curriculum and learning materials with source citations and qualified review.
- Safeguards: distinguish educational content from religious instruction or professional certification; state prerequisites and credentials accurately.

## 4. Research, archives and knowledge stewardship
- Oral history and community documentation projects.
- Digital cataloging of texts, images, recordings and artifacts where rights permit.
- Research collaboration, translation, bibliography and publication support.
- Metadata, provenance, preservation copies and access conditions.
- Safeguards: informed consent, community access restrictions, sensitive knowledge controls, attribution and correction mechanisms.

## 5. Events, festivals and cultural exchange
- Festivals, fairs, exhibitions, conferences, talks and performances.
- Artist, speaker, venue and organizer discovery.
- Ticketing and registration requirements as future integrations owned by appropriate platform layers.
- Cross-cultural exchange and visiting-program coordination.
- Safeguards: permissions, accessibility, crowd safety, cancellation/refund clarity, child safeguarding and local regulations.

## 6. Publishing, media and digital content
- Books, magazines, educational material, documentaries, podcasts and digital courses.
- Editorial services, translation, subtitling, distribution and creator monetization.
- Media libraries and curated discovery.
- Safeguards: copyright clearance, releases, fact checking, defamation review, source transparency and moderation.

## 7. Ethical products and responsible commerce
- Verified local products, sustainable goods, books, crafts and cultural learning materials.
- Product discovery, catalog metadata, fulfillment partnerships and customer support concepts.
- Supplier due diligence and transparent sourcing claims.
- Safeguards: product safety, labeling, consumer protection, returns, taxes, import/export and restricted-goods compliance.

## 8. Community enterprise and social impact
- Community-owned and cooperative business models.
- Local supplier networks, skills development and market access.
- Social enterprise programs and measurable livelihood initiatives.
- Grants/sponsorship discovery as information only unless eligibility and award are verified.
- Safeguards: community decision rights, benefit sharing, impact measurement and prevention of exploitative intermediaries.

## 9. Hospitality, food heritage and experience design
- Responsible accommodation and local host directories.
- Food heritage education and culinary experiences.
- Accessible visitor services and itinerary support.
- Safeguards: food safety, allergen disclosure, licensing, labor standards, cultural accuracy and visitor safety.

## 10. Partnerships and institutional collaboration
- Academic, museum, archive, nonprofit, artisan collective and commercial collaborations.
- Joint research, exhibitions, education and market access.
- Sponsorship and grant relationships with documented terms.
- Safeguards: due diligence, written scope, conflicts disclosure, logo/brand permission and no implied endorsement.

## Cross-domain capabilities (requirements only)
Discovery and search; multilingual content; provider verification; consent and rights records; catalog management; inquiries and referrals; customer support; reviews and corrections; analytics; payments; identity; security; storage; notifications; and workflow orchestration. Technical implementation belongs to separately owned platform layers.

## Catalog record minimum fields
- Record ID and record type.
- Public name and concise description.
- Domain and subdomain classification.
- Responsible owner/provider and verified contact channel.
- Geographic scope and service language(s).
- Evidence for claims, provenance and origin.
- Rights holder, license, consent status and permitted uses where relevant.
- Price, fees, taxes, refund/cancellation conditions when applicable.
- Accessibility, safety and capacity information where relevant.
- Verification status, reviewer, review date and expiry/recheck date.
- Status: proposed, under review, verified, published, paused, rejected or archived.

Never publish private personal information or sensitive community knowledge in a public catalog.


## 11. Dedicated domain packages

The detailed vertical packages are maintained under `domains/`:
- `heritage_tourism_business_ecosystem/`
- `arts_crafts_handloom_business_ecosystem/`
- `cultural_education_language_business_ecosystem/`
- `research_archives_knowledge_business_ecosystem/`
- `events_festivals_exhibitions_business_ecosystem/`
- `publishing_media_content_business_ecosystem/`
- `ethical_products_responsible_commerce_business_ecosystem/`
- `community_enterprise_social_impact_business_ecosystem/`
- `hospitality_food_heritage_experience_business_ecosystem/`
- `global_cultural_exchange_partnerships_business_ecosystem/`

The root `catalog.py` is the static taxonomy index. Each entry remains `proposed` until evidence-backed onboarding and review are completed.
