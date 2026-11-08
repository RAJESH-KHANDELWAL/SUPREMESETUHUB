"""DEPLOYMENT DOMAINS DOMAIN ECOSYSTEM reference catalog."""

DEPLOYMENT_DOMAINS_DOMAIN_ECOSYSTEM = {
    "category": "deployment_and_custom_domains",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "providers": [
        {"id": "aws", "name": "Amazon Route 53", "scope": "DNS hosting and domain registration transfer support", "official_docs_url": "https://docs.aws.amazon.com/Route53/latest/APIReference/Welcome.html", "status": "REFERENCE_ONLY"},
        {"id": "cloudflare", "name": "Cloudflare", "scope": "DNS zones, registrar domains, DNS records", "official_docs_url": "https://developers.cloudflare.com/api/", "status": "REFERENCE_ONLY"},
        {"id": "digitalocean", "name": "DigitalOcean", "scope": "DNS records and domain zones", "official_docs_url": "https://docs.digitalocean.com/reference/api/", "status": "REFERENCE_ONLY"},
        {"id": "vercel", "name": "Vercel", "scope": "Project domain configuration", "official_docs_url": "https://vercel.com/docs/rest-api", "status": "REFERENCE_ONLY"},
        {"id": "netlify", "name": "Netlify", "scope": "Custom domain management", "official_docs_url": "https://docs.netlify.com/api/get-started/", "status": "REFERENCE_ONLY"},
        {"id": "render", "name": "Render", "scope": "Custom domains for services", "official_docs_url": "https://docs.render.com/api", "status": "REFERENCE_ONLY"},
        {"id": "flyio", "name": "Fly.io", "scope": "Application domain and certificate management", "official_docs_url": "https://fly.io/docs/machines/api/", "status": "REFERENCE_ONLY"},
    ],
}
