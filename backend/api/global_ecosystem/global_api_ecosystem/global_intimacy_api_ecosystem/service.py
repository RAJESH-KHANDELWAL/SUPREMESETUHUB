"""Comprehensive global relationship, intimacy, sexual-wellness, and adult-industry catalog.

This module is a taxonomy and discovery index. A category/provider entry does not
mean the third party offers a public API, permits a given use case, or is connected.
Provider API availability and acceptable-use policies require case-by-case verification.
"""

from copy import deepcopy
from typing import Any

# The catalog deliberately separates relationship/wellness services from adult
# entertainment and adult-business infrastructure. Age, consent, rights, privacy,
# moderation, and jurisdiction requirements apply where relevant.
_CATEGORY_ROWS: tuple[tuple[str, str, str, str, bool], ...] = (
    ("RELATIONSHIPS", "Relationship Education and Support", "Communication, trust, conflict resolution, boundaries, healthy relationships, and educational resources.", "Education and support; do not imply clinical treatment.", False),
    ("DATING_MATCHMAKING", "Adult Dating and Matchmaking", "Dating discovery, matchmaking, profile management, adult social discovery, messaging, blocking, and reporting.", "Age rules, identity/privacy safeguards, moderation, and platform terms must be verified.", True),
    ("COUPLES_SERVICES", "Couples Support and Coaching", "Couples education, relationship coaching directories, appointment discovery, and referrals to qualified providers.", "Verify provider qualifications, confidentiality, and local rules.", False),
    ("MARRIAGE_FAMILY", "Marriage and Family Relationship Services", "Marriage education, family relationship support, communication courses, and referral directories.", "Credential and jurisdiction requirements vary.", False),
    ("RELATIONSHIP_THERAPY_DIRECTORY", "Relationship and Couples Therapy Directories", "Directories and appointment interfaces for qualified mental-health professionals and licensed couples therapists.", "Do not imply diagnosis or treatment by a catalog; validate credentials and clinical boundaries.", False),
    ("INTIMACY_WELLNESS", "Intimacy and Sexual Wellness", "Adult intimacy education, sexual wellbeing resources, relationship intimacy learning, and wellness products/services.", "Age-appropriate content, consent, privacy, and medical-claims review.", True),
    ("SEXUAL_HEALTH", "Sexual Health Information", "General sexual-health education, contraception awareness, STI information, and referrals to qualified services.", "Information only unless licensed clinical services are explicitly implemented.", False),
    ("REPRODUCTIVE_HEALTH", "Reproductive Health and Fertility", "Reproductive-health education, fertility service discovery, family-planning resources, and relevant appointment systems.", "Sensitive health data and medical/legal requirements need dedicated review.", False),
    ("CONSENT_AND_BOUNDARIES", "Consent, Boundaries, and Safety Education", "Consent education, personal boundaries, healthy communication, and safe relationship practices.", "Use appropriate, age-appropriate educational framing.", False),
    ("CONSENT_AND_SAFETY", "Consent, Privacy, and User Safety", "Consent records, reporting, blocking, anti-harassment processes, moderation, privacy controls, and abuse-prevention workflows.", "Safety-critical; data minimization and escalation paths are required.", False),
    ("AGE_ASSURANCE", "Age Assurance and Age-Restricted Access", "Age-assurance technologies and age-gating workflows for legally restricted products and services.", "Use lawful, proportionate methods; jurisdiction-specific requirements must be reviewed.", True),
    ("PRIVACY_IDENTITY", "Privacy, Identity, and Account Protection", "Identity verification, account security, privacy preferences, access controls, data retention, and deletion workflows.", "Handle identity and intimate data as sensitive personal information.", False),
    ("ADULT_INDUSTRY_BUSINESS", "Adult-Industry Business Platforms", "Business operations, creator administration, studio workflows, agency management, compliance, analytics, and reporting.", "Business metadata only; verify provider policy, payment eligibility, consent, rights, and jurisdiction.", True),
    ("ADULT_CREATOR_ECONOMY", "Adult Creator Platforms and Monetization", "Creator profiles, subscriptions, fan/member management, publishing workflows, payouts, and creator analytics.", "Only lawful adult creators and authorized accounts; verify platform rules and integration terms.", True),
    ("ADULT_CONTENT_HOSTING", "Adult-Content Hosting and Delivery", "Hosting, object storage, video delivery, CDN, access control, and publishing infrastructure where the provider expressly permits lawful adult content.", "Never infer adult-content permission from generic hosting availability.", True),
    ("ADULT_CONTENT_PUBLISHING", "Adult Content Publishing Platforms", "Publishing workflows, rights management, creator administration, moderation, and lawful content distribution.", "Consent, age/identity records, copyright, takedown, and local-law checks are required.", True),
    ("PORNOGRAPHY_VIDEO_PLATFORMS", "Adult Video and Pornography Platforms", "Catalog and platform metadata for lawful adult video/pornography publishers, streaming sites, and video-on-demand services.", "Restricted to lawful adult content involving consenting adults; confirm provider policies and current API availability.", True),
    ("ADULT_LIVE_STREAMING", "Adult Live Streaming and Cam Platforms", "Adult live-streaming platform directories, broadcaster operations, scheduling, moderation, and authorized business tools.", "Age assurance, consent, performer safety, recordkeeping, and jurisdiction checks are required.", True),
    ("ADULT_STUDIOS_PRODUCTION", "Adult Studios and Production Operations", "Studio operations, production scheduling, releases, rights administration, talent management, and production business systems.", "Require documented adult status, informed consent, rights, workplace safety, and release/recordkeeping procedures.", True),
    ("ADULT_PERFORMER_TALENT", "Adult Performer and Talent Management", "Professional directories, talent management, bookings, contracts, and approved business workflows for adult performers.", "Consent, identity protection, labor rules, and privacy protections are essential.", True),
    ("EROTIC_AUDIO", "Erotic Audio and Adult Podcasts", "Adult audio publishing, spoken-word catalogs, subscriptions, audio hosting, and creator operations.", "Age-rating, content policy, rights, and distribution restrictions must be checked.", True),
    ("EROTIC_LITERATURE", "Erotic Literature and Adult Publishing", "Adult fiction/e-books, publisher catalogs, writing platforms, rights management, and adult-audience distribution.", "Age rating, publisher rules, copyright, and distribution policy apply.", True),
    ("ADULT_PHOTOGRAPHY", "Adult Photography and Media Portfolios", "Authorized adult photo portfolios, creator media libraries, metadata, consent records, and rights management.", "Only consensual adult imagery; strict privacy and non-consensual-image safeguards required.", True),
    ("ADULT_COMMUNITIES", "Adult Communities and Membership Platforms", "Age-restricted adult community memberships, forums, creator communities, and moderated social spaces.", "Adult-only access where required, moderation, privacy, consent, and reporting.", True),
    ("ADULT_ECOMMERCE", "Adult Wellness and Intimate Products Commerce", "Lawful adult wellness/intimate product catalogs, e-commerce, inventory, subscriptions, and fulfillment APIs.", "Product legality, consumer safety, age limits, privacy, and payment rules vary by market.", True),
    ("ADULT_PAYMENTS_PAYOUTS", "Adult-Industry Payments and Payouts", "Payment acceptance, creator payouts, subscriptions, billing, and finance operations for eligible lawful adult businesses.", "Never assume a processor accepts adult businesses; obtain written eligibility and follow underwriting rules.", True),
    ("ADULT_ADVERTISING_AFFILIATES", "Adult Advertising, Affiliates, and Promotion", "Affiliate tracking, campaign analytics, advertising operations, attribution, and publisher reporting for lawful adult services.", "Observe network restrictions, consent/privacy rules, ad policies, and applicable marketing law.", True),
    ("ADULT_COMPLIANCE_RECORDS", "Adult-Industry Compliance and Records", "Age/identity record workflows, consent/release documentation, rights records, complaints, audits, and retention schedules.", "Legal requirements vary by jurisdiction; use qualified legal counsel and secure access controls.", True),
    ("CONTENT_MODERATION", "Adult Content Moderation and Trust & Safety", "Moderation queues, content classification, reporting, escalation, rights complaints, and content removal workflows.", "Do not permit exploitation, non-consensual intimate imagery, or sexual content involving minors.", True),
    ("COPYRIGHT_TAKEDOWN", "Copyright, Rights, and Takedown Management", "Copyright ownership, licenses, consent/release records, takedown requests, appeals, and evidence preservation.", "Provide clear reporting and takedown processes; verify rights before publication.", True),
    ("SEX_TOYS_WELLNESS_RETAIL", "Sexual Wellness Products and Retail", "Adult wellness product catalogs, retail operations, inventory, customer support, and product information.", "Follow local consumer, product-safety, payment, and advertising requirements.", True),
    ("SEX_EDUCATION", "Sex Education and Adult Learning", "Age-appropriate sex education, consent learning, relationship literacy, and adult learning resources.", "Keep content age-appropriate and medically responsible; consult qualified sources.", False),
    ("GLOBAL_PROVIDER_DIRECTORY", "Global Relationship and Intimacy Provider Directory", "Cross-category directory metadata for service providers, platforms, software vendors, and official documentation.", "A directory entry is not an endorsement, API guarantee, or proof of live integration.", False),
)

CATEGORIES: tuple[dict[str, Any], ...] = tuple(
    {
        "category_id": category_id,
        "name": name,
        "description": description,
        "scope": scope,
        "implementation_status": "CATALOG_ONLY",
        "age_restricted": age_restricted,
        "requires_compliance_review": True,
    }
    for category_id, name, description, scope, age_restricted in _CATEGORY_ROWS
)

# Research leads have official websites where known. API documentation URLs are
# only set when a verified, usable developer document is identified. Several adult
# content platforms do not publish a public developer API; do not substitute a
# third-party/private endpoint and call it official.
_PROVIDERS: tuple[dict[str, Any], ...] = (
    ("hinge", "Hinge", ["DATING_MATCHMAKING"], "https://hinge.co/", None, "Dating platform; public developer API not asserted."),
    ("bumble", "Bumble", ["DATING_MATCHMAKING"], "https://bumble.com/", None, "Dating platform; public developer API not asserted."),
    ("match_group", "Match Group", ["DATING_MATCHMAKING"], "https://mtch.com/", None, "Company portfolio includes dating services; each product's terms/API require separate review."),
    ("eharmony", "eharmony", ["DATING_MATCHMAKING", "MARRIAGE_FAMILY"], "https://www.eharmony.com/", None, "Dating/relationship service; no public API asserted."),
    ("okcupid", "OkCupid", ["DATING_MATCHMAKING"], "https://www.okcupid.com/", None, "Dating service; no public API asserted."),
    ("planned_couples_therapy_directory", "Qualified Couples Therapy Provider Directory", ["RELATIONSHIP_THERAPY_DIRECTORY", "COUPLES_SERVICES"], None, None, "Directory category; individual providers and credentials must be verified."),
    ("planned_sexual_health_directory", "Sexual Health Services Directory", ["SEXUAL_HEALTH", "REPRODUCTIVE_HEALTH"], None, None, "Directory category; individual health organizations must be verified."),
    ("onlyfans", "OnlyFans", ["ADULT_CREATOR_ECONOMY", "ADULT_CONTENT_PUBLISHING", "ADULT_INDUSTRY_BUSINESS"], "https://onlyfans.com/", None, "Public official developer API has not been verified; third-party API products are not official."),
    ("fansly", "Fansly", ["ADULT_CREATOR_ECONOMY", "ADULT_CONTENT_PUBLISHING"], "https://fansly.com/", None, "Public official developer API has not been verified."),
    ("fanvue", "Fanvue", ["ADULT_CREATOR_ECONOMY", "ADULT_CONTENT_PUBLISHING"], "https://www.fanvue.com/", None, "Verify official API access and platform terms before implementation."),
    ("manyvids", "ManyVids", ["ADULT_CREATOR_ECONOMY", "ADULT_CONTENT_PUBLISHING", "PORNOGRAPHY_VIDEO_PLATFORMS"], "https://www.manyvids.com/", None, "Adult content marketplace; API access must be individually verified."),
    ("xvideos", "XVideos", ["PORNOGRAPHY_VIDEO_PLATFORMS", "PORNOGRAPHY_VIDEO_PLATFORMS"], "https://www.xvideos.com/", None, "Adult video platform; public official API not asserted."),
    ("xhamster", "xHamster", ["PORNOGRAPHY_VIDEO_PLATFORMS", "PORNOGRAPHY_VIDEO_PLATFORMS"], "https://xhamster.com/", None, "Adult video platform; public official API not asserted."),
    ("redtube", "RedTube", ["PORNOGRAPHY_VIDEO_PLATFORMS", "PORNOGRAPHY_VIDEO_PLATFORMS"], "https://www.redtube.com/", None, "Adult video platform; public official API not asserted."),
    ("brazzers", "Brazzers", ["ADULT_STUDIOS_PRODUCTION", "PORNOGRAPHY_VIDEO_PLATFORMS"], "https://www.brazzers.com/", None, "Adult studio/content brand; public official API not asserted."),
    ("reality_kings", "Reality Kings", ["ADULT_STUDIOS_PRODUCTION", "PORNOGRAPHY_VIDEO_PLATFORMS"], "https://www.realitykings.com/", None, "Adult studio/content brand; public official API not asserted."),
    ("mofos", "MOFOS", ["ADULT_STUDIOS_PRODUCTION", "PORNOGRAPHY_VIDEO_PLATFORMS"], "https://www.mofos.com/", None, "Adult studio/content brand; public official API not asserted."),
    ("adult_time", "Adult Time", ["ADULT_STUDIOS_PRODUCTION", "PORNOGRAPHY_VIDEO_PLATFORMS"], "https://www.adulttime.com/", None, "Adult studio/content platform; public official API not asserted."),
    ("manyvids_creators", "ManyVids Creator Services", ["ADULT_CREATOR_ECONOMY", "ADULT_INDUSTRY_BUSINESS"], "https://www.manyvids.com/", None, "Use only official creator-facing integration channels that are documented and authorized."),
    ("segpay", "Segpay", ["ADULT_PAYMENTS_PAYOUTS"], "https://segpay.com/", None, "Payment provider often associated with high-risk verticals; eligibility and APIs require direct verification."),
    ("ccbill", "CCBill", ["ADULT_PAYMENTS_PAYOUTS"], "https://ccbill.com/", None, "Payment services; adult-merchant eligibility and supported integration APIs require direct verification."),
    ("verotel", "Verotel", ["ADULT_PAYMENTS_PAYOUTS"], "https://www.verotel.com/", None, "Payment services; merchant underwriting and API availability require direct verification."),
    ("cloudflare", "Cloudflare", ["ADULT_CONTENT_HOSTING", "ADULT_CONTENT_PUBLISHING"], "https://www.cloudflare.com/", "https://developers.cloudflare.com/api/", "General infrastructure vendor; verify current acceptable-use policy before any adult-content use."),
    ("aws", "Amazon Web Services", ["ADULT_CONTENT_HOSTING"], "https://aws.amazon.com/", "https://docs.aws.amazon.com/", "General cloud vendor; verify current service-specific terms and content restrictions."),
    ("digitalocean", "DigitalOcean", ["ADULT_CONTENT_HOSTING"], "https://www.digitalocean.com/", "https://docs.digitalocean.com/reference/api/", "General cloud vendor; verify current acceptable-use and service-specific terms."),
    ("hostkey", "HOSTKEY", ["ADULT_CONTENT_HOSTING"], "https://hostkey.com/", None, "Hosting provider directory lead; verify current adult-content policy and official API availability."),
    ("shinjiru", "Shinjiru", ["ADULT_CONTENT_HOSTING"], "https://www.shinjiru.com/", None, "Hosting provider directory lead; verify current adult-content policy and official API availability."),
    ("flokinet", "FlokiNET", ["ADULT_CONTENT_HOSTING"], "https://flokinet.is/", None, "Hosting provider directory lead; verify current adult-content policy and official API availability."),
    ("planned_adult_live_streaming", "Adult Live Streaming Provider Directory", ["ADULT_LIVE_STREAMING"], None, None, "Provider names and terms require an individual verification pass."),
    ("planned_adult_audio_publishing", "Adult Audio Publishing Provider Directory", ["EROTIC_AUDIO"], None, None, "Provider names, publisher rules, and API access require verification."),
    ("planned_erotic_literature", "Adult Literature Publishing Provider Directory", ["EROTIC_LITERATURE"], None, None, "Provider names, publisher rules, and API access require verification."),
    ("planned_age_assurance", "Age Assurance Provider Directory", ["AGE_ASSURANCE", "CONSENT_AND_SAFETY"], None, None, "Select vendors only after comparing lawful coverage, privacy, retention, and false-positive risks."),
    ("planned_moderation", "Content Moderation Provider Directory", ["CONTENT_MODERATION", "COPYRIGHT_TAKEDOWN"], None, None, "Select vendors only after capability, policy, and data-processing review."),
)

PROVIDERS: tuple[dict[str, Any], ...] = tuple(
    {
        "provider_id": provider_id,
        "name": name,
        "category_ids": category_ids,
        "official_url": official_url,
        "official_api_docs_url": api_docs_url,
        "implementation_status": "CATALOG_ONLY",
        "live_connection_verified": False,
        "notes": notes,
    }
    for provider_id, name, category_ids, official_url, api_docs_url, notes in _PROVIDERS
)

SAFETY_SCOPE = [
    "Age-restricted services are intended only for adults who meet applicable legal age requirements",
    "Consent, rights, and adult-status checks for adult content and production workflows",
    "No sexual content involving minors, exploitation, or trafficking",
    "No non-consensual intimate imagery; provide report, appeal, and takedown paths",
    "Privacy, data minimization, access control, encryption, retention, and deletion controls",
    "Official provider API documentation and current acceptable-use terms must be verified",
    "Catalog inclusion does not imply endorsement, permitted use, public API access, or a live connection",
]


def list_categories() -> list[dict[str, Any]]:
    """Return a copy of the global category taxonomy."""
    return deepcopy(list(CATEGORIES))


def get_category(category_id: str) -> dict[str, Any] | None:
    """Return one category by identifier."""
    key = category_id.strip().upper()
    return next((deepcopy(item) for item in CATEGORIES if item["category_id"] == key), None)


def list_providers(category_id: str | None = None) -> list[dict[str, Any]]:
    """Return provider research leads, optionally filtered by a category."""
    providers = list(PROVIDERS)
    if category_id:
        key = category_id.strip().upper()
        providers = [provider for provider in providers if key in provider["category_ids"]]
    return deepcopy(providers)


def get_ecosystem_status() -> dict[str, Any]:
    """Return catalog coverage and honest live-integration status."""
    # Import within the function to avoid coupling category definitions to
    # subsystem modules during package import.
    from .integrations.service import list_entries as list_integrations
    from .services.service import list_entries as list_services
    from .tools.service import list_entries as list_tools

    return {
        "success": True,
        "system": "GLOBAL RELATIONSHIP AND INTIMACY API ECOSYSTEM",
        "catalog_only": True,
        "live_connections_verified": False,
        "category_count": len(CATEGORIES),
        "provider_count": len(PROVIDERS),
        "integration_count": len(list_integrations()),
        "service_count": len(list_services()),
        "tool_count": len(list_tools()),
        "safety_scope": list(SAFETY_SCOPE),
    }
