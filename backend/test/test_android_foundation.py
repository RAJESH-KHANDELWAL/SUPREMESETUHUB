"""Contract tests for the Backend Global Android native app setup."""

from pathlib import Path
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
PROJECT = (
    REPOSITORY_ROOT
    / "backend"
    / "android"
    / "global_ecosystem"
    / "global_android_ecosystem"
    / "native_android_app"
)
ANDROID_SOURCE = (
    PROJECT / "app" / "src" / "main" / "java" / "com" / "mainbasefoundation" / "android"
)


class AndroidFoundationTests(unittest.TestCase):
    def test_native_android_project_files_exist(self):
        required_files = (
            PROJECT / "settings.gradle",
            PROJECT / "build.gradle",
            PROJECT / "gradle.properties",
            PROJECT / "app" / "build.gradle",
            PROJECT / "app" / "src" / "main" / "AndroidManifest.xml",
        )
        for path in required_files:
            with self.subTest(path=path.relative_to(PROJECT)):
                self.assertTrue(path.is_file(), f"Missing Android project file: {path}")

    def test_android_app_configuration(self):
        content = (PROJECT / "app" / "build.gradle").read_text(encoding="utf-8")
        checks = {
            "applicationId": r"""applicationId\s+['"]com\.mainbasefoundation\.android['"]""",
            "namespace": r"""namespace\s+['"]com\.mainbasefoundation\.android['"]""",
            "compileSdk": r"compileSdk\s+36",
            "minSdk": r"minSdk\s+26",
            "targetSdk": r"targetSdk\s+36",
            "Java 17": r"sourceCompatibility\s+JavaVersion\.VERSION_17",
            "BuildConfig generation": r"buildConfig\s+true",
            "external API URL configuration": r"SUPREME_API_BASE_URL",
        }
        for label, pattern in checks.items():
            with self.subTest(configuration=label):
                self.assertRegex(content, pattern)

    def test_native_android_sources_exist(self):
        for filename in (
            "ApiClient.kt", "ApiClientAsync.kt", "ApiConfig.kt", "AuthApi.kt",
            "MainActivity.kt", "SecureSessionStore.kt", "SessionManager.kt",
        ):
            with self.subTest(filename=filename):
                self.assertTrue((ANDROID_SOURCE / filename).is_file())

    def test_api_endpoint_is_not_hardcoded_to_obsolete_host(self):
        api_config = (ANDROID_SOURCE / "ApiConfig.kt").read_text(encoding="utf-8")
        api_client = (ANDROID_SOURCE / "ApiClient.kt").read_text(encoding="utf-8")
        app_gradle = (PROJECT / "app" / "build.gradle").read_text(encoding="utf-8")
        self.assertNotIn("onrender.com", api_config.lower())
        self.assertIn("BuildConfig.API_BASE_URL", api_config)
        self.assertIn("SUPREME_API_BASE_URL", app_gradle)
        self.assertIn("baseUrl.isEmpty()", api_client)
        self.assertIn('startsWith("https://"', api_client)

    def test_old_mobile_android_project_is_not_present(self):
        old_project = REPOSITORY_ROOT / "backend" / "mobile" / "android"
        self.assertFalse(old_project.exists(), f"Old Android project still exists: {old_project}")


if __name__ == "__main__":
    unittest.main()
