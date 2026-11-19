"""DIGITALOCEAN Storage Core provider package."""
PROVIDER = "digitalocean"
ECOSYSTEM_ID = "DIGITALOCEAN-STORAGE-CORE-ECOSYSTEM"

from .service import DigitalOceanStorageCoreService

__all__ = ["PROVIDER", "ECOSYSTEM_ID", "DigitalOceanStorageCoreService"]
