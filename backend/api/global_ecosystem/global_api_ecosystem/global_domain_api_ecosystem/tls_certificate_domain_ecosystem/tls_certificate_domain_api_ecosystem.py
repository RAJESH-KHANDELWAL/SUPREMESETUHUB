"""TLS CERTIFICATE DOMAIN ECOSYSTEM reference catalog."""

TLS_CERTIFICATE_DOMAIN_ECOSYSTEM = {
    "category": "tls_and_certificate_automation",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "providers": [
        {"id": "aws", "name": "Amazon Route 53", "scope": "DNS hosting and domain registration transfer support", "official_docs_url": "https://docs.aws.amazon.com/Route53/latest/APIReference/Welcome.html", "status": "REFERENCE_ONLY"},
        {"id": "cloudflare", "name": "Cloudflare", "scope": "DNS zones, registrar domains, DNS records", "official_docs_url": "https://developers.cloudflare.com/api/", "status": "REFERENCE_ONLY"},
        {"id": "letsencrypt", "name": "Let's Encrypt", "scope": "Automated TLS certificate issuance for domains", "official_docs_url": "https://letsencrypt.org/docs/", "status": "REFERENCE_ONLY"},
        {"id": "certbot", "name": "Certbot", "scope": "ACME TLS certificate automation tool", "official_docs_url": "https://certbot.eff.org/", "status": "REFERENCE_ONLY"},
        {"id": "acme", "name": "ACME protocol", "scope": "Automated certificate management protocol", "official_docs_url": "https://datatracker.ietf.org/doc/html/rfc8555", "status": "REFERENCE_ONLY"},
    ],
}
