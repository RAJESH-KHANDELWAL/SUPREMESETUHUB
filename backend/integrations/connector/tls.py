from __future__ import annotations

import ssl


class TLSConfiguration:
    """
    Secure TLS configuration for external connections.
    """

    def __init__(
        self,
        minimum_version: ssl.TLSVersion = ssl.TLSVersion.TLSv1_2,
        check_hostname: bool = True,
        verify_mode: ssl.VerifyMode = ssl.CERT_REQUIRED,
    ) -> None:

        self.minimum_version = minimum_version
        self.check_hostname = check_hostname
        self.verify_mode = verify_mode

    def create_context(self) -> ssl.SSLContext:

        context = ssl.create_default_context()

        context.minimum_version = self.minimum_version
        context.check_hostname = self.check_hostname
        context.verify_mode = self.verify_mode

        return context

    def status(self) -> dict[str, object]:

        return {
            "success": True,
            "tls": True,
            "ssl": True,
            "minimum_version": self.minimum_version.name,
            "certificate_verification": (
                self.verify_mode == ssl.CERT_REQUIRED
            ),
            "hostname_verification": self.check_hostname,
            "status": "SECURE",
        }


tls_configuration = TLSConfiguration()
