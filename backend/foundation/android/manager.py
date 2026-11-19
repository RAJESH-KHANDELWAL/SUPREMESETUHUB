"""Foundation contract for the existing native Android application."""


class AndroidFoundationManager:
    """Describe and validate the repository's Android project contract.

    This manager does not duplicate the Android application or claim that a
    Gradle build has succeeded. The native app remains in ``mobile/android``.
    """

    NAME = "ANDROID_FOUNDATION"
    PROJECT_PATH = "mobile/android"
    APP_MODULE_PATH = "mobile/android/app"
    APPLICATION_ID = "com.mainbasefoundation.android"
    NAMESPACE = "com.mainbasefoundation.android"
    COMPILE_SDK = 36
    MIN_SDK = 26
    TARGET_SDK = 36
    JAVA_VERSION = 17
    RELEASE_TASK = ":app:bundleRelease"
    DEBUG_TASK = ":app:assembleDebug"
    RELEASE_ARTIFACT = (
        "mobile/android/app/build/outputs/bundle/release/app-release.aab"
    )

    def project_contract(self):
        """Return the canonical paths and build contract for the Android app."""
        return {
            "component": self.NAME,
            "project_path": self.PROJECT_PATH,
            "app_module_path": self.APP_MODULE_PATH,
            "application_id": self.APPLICATION_ID,
            "namespace": self.NAMESPACE,
            "compile_sdk": self.COMPILE_SDK,
            "min_sdk": self.MIN_SDK,
            "target_sdk": self.TARGET_SDK,
            "java_version": self.JAVA_VERSION,
            "release_task": self.RELEASE_TASK,
            "debug_task": self.DEBUG_TASK,
            "release_artifact": self.RELEASE_ARTIFACT,
        }

    def status(self):
        """Report declared project configuration, not build/runtime health."""
        return {
            "component": self.NAME,
            "status": "CONFIGURED",
            "project_path": self.PROJECT_PATH,
            "build_task": self.RELEASE_TASK,
            "build_verified": False,
        }


__all__ = ["AndroidFoundationManager"]
