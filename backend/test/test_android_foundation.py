"""Contract tests for the canonical Backend Global Android Ecosystem native app."""

from pathlib import Path
import re
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
        }
        for label, pattern in checks.items():
            with self.subTest(configuration=label):
                self.assertRegex(content, pattern)

    def test_old_mobile_android_project_is_not_present(self):
        old_project = REPOSITORY_ROOT / "backend" / "mobile" / "android"
        self.assertFalse(old_project.exists(), f"Old Android project still exists: {old_project}")


if __name__ == "__main__":
    unittest.main()
