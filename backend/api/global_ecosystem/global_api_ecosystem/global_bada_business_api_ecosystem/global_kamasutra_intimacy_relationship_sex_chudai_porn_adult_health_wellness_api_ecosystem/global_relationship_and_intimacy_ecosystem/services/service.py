"""Detailed service taxonomy for global relationship, intimacy, and adult industries."""
from copy import deepcopy
from typing import Any

_ROWS: tuple[tuple[str, str, list[str], str, str], ...] = (
    ("relationship_education","Relationship Education and Communication",["RELATIONSHIPS"],"Courses and resources for communication, boundaries, trust, and conflict resolution.","general; content rating varies"),
    ("dating_matchmaking","Adult Dating and Matchmaking",["DATING_MATCHMAKING"],"Adult dating discovery, profiles, matchmaking, safety, reporting, and blocking.","adults where age-restricted"),
    ("marriage_family","Marriage and Family Relationship Education",["MARRIAGE_FAMILY"],"Relationship learning, family communication resources, and support referrals.","general; provider rules apply"),
    ("couples_support","Couples Coaching and Qualified Support",["COUPLES_SERVICES","RELATIONSHIP_THERAPY_DIRECTORY"],"Directory and scheduling for relationship-support and qualified couples professionals.","provider-specific credentials and eligibility"),
    ("intimacy_wellness","Intimacy and Sexual Wellness Education",["INTIMACY_WELLNESS"],"Consent-centred adult intimacy education and sexual-wellness resources.","age appropriate; adults for restricted content"),
    ("sexual_health","Sexual Health Information and Referrals",["SEXUAL_HEALTH"],"General information and referral to qualified sexual-health services.","educational; local rules apply"),
    ("reproductive_health","Reproductive Health and Fertility Services",["REPRODUCTIVE_HEALTH"],"Fertility, family planning, and reproductive-health service discovery.","sensitive health data protections apply"),
    ("consent_safety","Consent, Boundaries, and Safety Education",["CONSENT_AND_BOUNDARIES","CONSENT_AND_SAFETY"],"Consent literacy, personal safety education, reporting, and abuse-prevention resources.","age appropriate"),
    ("adult_creator","Adult Creator Economy and Memberships",["ADULT_CREATOR_ECONOMY"],"Creator profiles, memberships, subscriptions, publishing workflows, and analytics where permitted.","verified adults and authorized business accounts"),
    ("adult_video_porn","Adult Video and Pornography Services",["PORNOGRAPHY_VIDEO_PLATFORMS","ADULT_CONTENT_PUBLISHING"],"Catalog discovery for lawful adult-video publishers and distribution services.","consenting adults only; platform and legal restrictions"),
    ("adult_live","Adult Live Streaming and Cam Services",["ADULT_LIVE_STREAMING"],"Adult live-streaming provider discovery, broadcaster tools, moderation, and scheduling.","adults only where required; consent and safety controls"),
    ("adult_studio","Adult Studio and Production Operations",["ADULT_STUDIOS_PRODUCTION"],"Production planning, authorized performer management, releases, and rights administration.","verify adulthood, informed consent, workplace safety, and rights"),
    ("adult_talent","Adult Performer and Talent Management",["ADULT_PERFORMER_TALENT"],"Professional representation, bookings, contracts, and authorized talent operations.","adult professionals; privacy and labor protections"),
    ("adult_audio","Erotic Audio and Adult Podcast Publishing",["EROTIC_AUDIO"],"Adult audio catalogs, creator subscriptions, distribution, and podcast publishing.","age rating and publisher rules apply"),
    ("adult_literature","Erotic Literature and Adult Publishing",["EROTIC_LITERATURE"],"Adult fiction, e-books, publisher directories, rights, and distribution workflows.","age rating, copyright, and platform policy apply"),
    ("adult_photography","Adult Photography and Media Portfolios",["ADULT_PHOTOGRAPHY"],"Portfolio and media-library services for authorized, consensual adult imagery.","adult participants only; strict privacy and rights checks"),
    ("adult_communities","Adult Communities and Membership Platforms",["ADULT_COMMUNITIES"],"Age-restricted member communities, forums, creator communities, and moderation.","age gating and moderation requirements apply"),
    ("adult_wellness_retail","Adult Wellness and Intimate Products Retail",["ADULT_ECOMMERCE","SEX_TOYS_WELLNESS_RETAIL"],"Product discovery, inventory, e-commerce, fulfillment, and consumer information.","check product legality and consumer protections"),
    ("adult_payments","Adult-Industry Payments and Payouts",["ADULT_PAYMENTS_PAYOUTS"],"Merchant payments, subscriptions, payouts, billing, and financial reporting.","provider approval and underwriting required"),
    ("adult_affiliates","Adult Advertising and Affiliate Services",["ADULT_ADVERTISING_AFFILIATES"],"Affiliate directories, campaign attribution, reporting, and compliant promotion.","advertising, privacy, and network terms apply"),
    ("adult_compliance","Adult-Industry Compliance and Records",["ADULT_COMPLIANCE_RECORDS"],"Secure compliance records, consent/release documentation, rights, reporting, and audits.","legal requirements vary by jurisdiction"),
    ("adult_hosting","Adult-Content Hosting and Delivery",["ADULT_CONTENT_HOSTING"],"Hosting, storage, CDN, access control, publishing, and delivery discovery.","provider terms must explicitly permit the intended lawful adult use"),
    ("moderation_takedown","Adult Content Moderation and Takedown",["CONTENT_MODERATION","COPYRIGHT_TAKEDOWN"],"Reporting, moderation, abuse escalation, rights complaints, takedowns, and appeals.","no exploitation, non-consensual imagery, or content involving minors"),
    ("age_assurance","Age Assurance and Access Control",["AGE_ASSURANCE"],"Age assurance and compliant access-control service discovery.","proportionate privacy-preserving implementation required"),
    ("privacy_security","Privacy and Account Security",["PRIVACY_IDENTITY"],"Identity protection, privacy controls, account security, retention, and deletion workflows.","sensitive data safeguards required"),
)

_ENTRIES: tuple[dict[str, Any], ...] = tuple(
    {
        "service_id": service_id,
        "name": name,
        "category_ids": category_ids,
        "description": description,
        "audience": audience,
        "implementation_status": "CATALOG_ONLY",
        "requires_compliance_review": True,
    }
    for service_id, name, category_ids, description, audience in _ROWS
)

def list_entries(category_id: str | None = None) -> list[dict[str, Any]]:
    """Return detailed service entries, optionally filtered by category ID."""
    rows = list(_ENTRIES)
    if category_id:
        key = category_id.strip().upper()
        rows = [row for row in rows if key in row["category_ids"]]
    return deepcopy(rows)
