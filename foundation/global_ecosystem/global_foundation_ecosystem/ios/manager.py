"""Contract manager for the repository's native iOS Swift package."""

from pathlib import Path


class IOSFoundationManager:
    NAME = "IOS FOUNDATION"
    VERSION = "1.0.0"

    def __init__(self):
        self.repository_root = Path(__file__).resolve().parents[5]
        self.project_path = self.repository_root / "backend" / "mobile" / "ios"
        self.package_file = self.project_path / "Package.swift"

    def project_contract(self):
        if not self.package_file.is_file():
            raise FileNotFoundError(f"iOS Swift package manifest not found: {self.package_file}")
        content = self.package_file.read_text(encoding="utf-8")
        if 'name: "SupremeSetuHubIOS"' not in content:
            raise ValueError("iOS Swift package name is missing or incorrect")
        return {
            "project_path": "backend/mobile/ios",
            "manifest_path": "backend/mobile/ios/Package.swift",
            "platform": "iOS",
            "minimum_ios_version": "16.0",
            "build_verified": False,
        }

    def status(self):
        contract = self.project_contract()
        return {
            "name": self.NAME,
            "version": self.VERSION,
            "status": "CONFIGURED",
            "project_path": contract["project_path"],
            "build_verified": False,
        }
