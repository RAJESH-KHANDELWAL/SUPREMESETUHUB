# GOOGLE PHOTO & VIDEO STORAGE ECOSYSTEM

Storage-domain catalog for Google Photos libraries and photo/video asset metadata.

## Scope
- Photo and video asset metadata
- Albums and user-controlled sharing metadata
- Backup and synchronization state
- Archive, export, and takeout-related metadata
- Media size, format, timestamps, and lifecycle metadata

## Ownership boundary
This package owns media-storage taxonomy and metadata only. Google Photos API availability, OAuth authorization, library access, media download/export, and provider operations belong in the Google API/integration layer. Do not assume unrestricted access to a user's entire Photos library; API capabilities and access rules must be checked against current Google documentation.

## Safety and readiness
No Google Photos account is connected by this scaffold. Obtain explicit user authorization, apply least-privilege access, and protect personal images, videos, and metadata.
