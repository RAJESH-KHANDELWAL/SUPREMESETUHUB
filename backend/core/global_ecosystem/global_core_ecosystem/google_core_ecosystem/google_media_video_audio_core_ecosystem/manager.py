"""Manager for the MEDIA_VIDEO_AND_AUDIO Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class MediaVideoAudioDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "MEDIA_VIDEO_AND_AUDIO"


def get_manager() -> MediaVideoAudioDomainManager:
    return MediaVideoAudioDomainManager()


__all__ = ["MediaVideoAudioDomainManager", "get_manager"]
