"""Provider directory. Entries are descriptive until independently verified."""
from .schemas import CatalogRecord

PROVIDERS = (
    CatalogRecord("aws", "Amazon Web Services", "cloud", "Cloud infrastructure provider.", "NOT_CONFIGURED"),
    CatalogRecord("azure", "Microsoft Azure", "cloud", "Cloud infrastructure provider.", "NOT_CONFIGURED"),
    CatalogRecord("google_cloud", "Google Cloud", "cloud", "Cloud infrastructure provider.", "NOT_CONFIGURED"),
    CatalogRecord("cloudflare", "Cloudflare", "edge_network", "DNS, CDN, security and edge services.", "NOT_CONFIGURED"),
    CatalogRecord("digitalocean", "DigitalOcean", "cloud", "Cloud compute and managed services.", "NOT_CONFIGURED"),
    CatalogRecord("hostinger", "Hostinger", "hosting", "Web hosting, domains and VPS services.", "CATALOG_ONLY"),
    CatalogRecord("abelohost", "AbeloHost", "hosting", "Hosting and server services.", "NOT_CONFIGURED"),
    CatalogRecord("vps_vicetemple", "ViceTemple", "hosting", "Hosting and VPS services.", "NOT_CONFIGURED"),
    CatalogRecord("proton", "Proton", "cloud_storage", "Privacy-focused cloud and collaboration services.", "NOT_CONFIGURED"),
    CatalogRecord("mega", "MEGA", "cloud_storage", "Cloud storage and transfer services.", "NOT_CONFIGURED"),
    CatalogRecord("microsoft", "Microsoft", "platform", "Identity, productivity and cloud platform services.", "NOT_CONFIGURED"),
)
