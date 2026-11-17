"""Provider-neutral storage capability taxonomy."""
CAPABILITIES = {
    "OBJECT_STORAGE": {"description": "Durable object and blob storage metadata."},
    "FILE_STORAGE": {"description": "Managed file shares and hierarchical file access."},
    "BLOCK_STORAGE": {"description": "Block-volume storage capability metadata."},
    "FILE_SYNC": {"description": "Cross-device file synchronization capability."},
    "DEVICE_BACKUP": {"description": "Device backup capability metadata."},
    "ARCHIVE": {"description": "Long-term and archival storage capability."},
    "LIFECYCLE": {"description": "Retention and lifecycle policy capability."},
    "REGIONAL_STORAGE": {"description": "Region and location selection metadata."},
    "CDN_INTEGRATION": {"description": "Optional content delivery integration metadata."},
}
__all__ = ["CAPABILITIES"]
