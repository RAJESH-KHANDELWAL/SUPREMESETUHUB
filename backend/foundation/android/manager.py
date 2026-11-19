"""Foundation contract for the existing native Android application."""

from pathlib import Path
import re


class AndroidFoundationManager:
    """Describe and validate the repository's existing native Android app.

    The manager reads the real Gradle module configuration. It does not
    duplicate the Android application or claim a successful release build.
    """

    NAME = "ANDROID_FOUNDATION"
    PROJECT_PATH = "mobile/android"
    APP_MODULE_PATH = "mobile/android/app"
    RELEASE_TASK = ":app:bundleRelease"
    DEBUG_TASK = ":app:assembleDebug"
    RELEASE_ARTIFACT = (
        "mobile/android/app/build/outputs/bundle/release/app-release.aab"
    )

    def _gradle_config(self):
        repository_root = Path(__file__).resolve().parents[3]
        gradle_file = (
            repository_root / self.PROJECT_PATH / "app" / "build.gradle"
        )
        if not gradle_file.is_file():
            raise FileNotFoundError(
                f"Android app Gradle configuration not found: {gradle_file}"
            )

        source = gradle_file.read_text(encoding="utf-8")

        def required(pattern, label, cast=str):
            match = re.search(pattern, source, re.MULTILINE)
            if match is None:
                raise ValueError(f"Android Gradle setting is missing: {label}")
            return cast(match.group(1))

        return {
            "application_id": required(
                r"applicationId\s+['\"]([^'\"]+)['\"]",
                "applicationId",
            ),
            "namespace": required(
                r"namespace\s+['\"]([^'\"]+)['\"]",
                "namespace",
            ),
            "compile_sdk": required(r"compileSdk\s+(\d+)", "compileSdk", int),
            "min_sdk": required(r"minSdk\s+(\d+)", "minSdk", int),
            "target_sdk": required(r"targetSdk\s+(\d+)", "targetSdk", int),
            "java_version": required(
                r"sourceCompatibility\s+JavaVersion\.VERSION_(\d+)",
                "sourceCompatibility",
                int,
            ),
        }

    def project_contract(self):
        """Read actual Android app settings and expose the Foundation contract."""
        return {
            "component": self.NAME,
            "project_path": self.PROJECT_PATH,
            "app_module_path": self.APP_MODULE_PATH,
            **self._gradle_config(),
            "release_task": self.RELEASE_TASK,
            "debug_task": self.DEBUG_TASK,
            "release_artifact": self.RELEASE_ARTIFACT,
        }

    def status(self):
        """Report Gradle configuration presence, not build/runtime health."""
        contract = self.project_contract()
        return {
            "component": self.NAME,
            "status": "CONFIGURED",
            "project_path": self.PROJECT_PATH,
            "build_task": self.RELEASE_TASK,
            "build_verified": False,
            "application_id": contract["application_id"],
        }


__all__ = ["AndroidFoundationManager"]
