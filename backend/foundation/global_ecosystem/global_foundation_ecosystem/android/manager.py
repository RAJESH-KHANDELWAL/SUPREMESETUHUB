"""Contract manager for the repository's native Android application."""

from pathlib import Path
import re


class AndroidFoundationManager:
    """Expose the configured Android project contract without claiming a build."""

    NAME = "ANDROID FOUNDATION"
    VERSION = "1.0.0"

    def __init__(self):
        self.repository_root = Path(__file__).resolve().parents[5]
        self.project_path = self.repository_root / "backend" / "mobile" / "android"
        self.app_module_path = self.project_path / "app"
        self.build_file = self.app_module_path / "build.gradle"

    @staticmethod
    def _match(pattern, content, label):
        match = re.search(pattern, content, re.MULTILINE)
        if not match:
            raise ValueError(f"Android Gradle configuration is missing {label}")
        return match.group(1)

    def project_contract(self):
        if not self.build_file.is_file():
            raise FileNotFoundError(f"Android app build file not found: {self.build_file}")
        content = self.build_file.read_text(encoding="utf-8")
        application_id = self._match(r"""applicationId\s+['"]([^'"]+)['"]""", content, "applicationId")
        namespace = self._match(r"""namespace\s+['"]([^'"]+)['"]""", content, "namespace")
        compile_sdk = int(self._match(r"compileSdk\s+(\d+)", content, "compileSdk"))
        min_sdk = int(self._match(r"minSdk\s+(\d+)", content, "minSdk"))
        target_sdk = int(self._match(r"targetSdk\s+(\d+)", content, "targetSdk"))
        java_version = int(self._match(r"sourceCompatibility\s+JavaVersion\.VERSION_(\d+)", content, "Java source compatibility"))
        return {
            "project_path": "backend/mobile/android",
            "app_module_path": "backend/mobile/android/app",
            "application_id": application_id,
            "namespace": namespace,
            "compile_sdk": compile_sdk,
            "min_sdk": min_sdk,
            "target_sdk": target_sdk,
            "java_version": java_version,
            "release_task": ":app:bundleRelease",
            "release_artifact": "backend/mobile/android/app/build/outputs/bundle/release/app-release.aab",
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
