package com.mainbasefoundation.android

object ApiConfig {
    /*
     * Configure the deployed backend URL through the Gradle property
     * SUPREME_API_BASE_URL or the environment variable of the same name.
     *
     * The value is intentionally blank by default: the app must not silently
     * call an obsolete or unverified host. Never put secrets in this file.
     */
    const val BASE_URL = BuildConfig.API_BASE_URL

    const val AUTH_PATH = "/auth"
    const val USERS_PATH = "/users"
    const val BUSINESS_PATH = "/businesses"
    const val PROJECTS_PATH = "/projects"
    const val PROFILES_PATH = "/profiles"
    const val IDENTITY_PATH = "/identity"
    const val ROLES_PATH = "/roles"
    const val OPPORTUNITIES_PATH = "/opportunities"
    const val MATCHING_PATH = "/matching"
    const val ECOSYSTEM_PATH = "/ecosystem"
    const val STORAGE_PATH = "/storage"
    const val CONNECTIVITY_PATH = "/connectivity"
    const val CLOUD_PATH = "/cloud"
    const val INTEGRATIONS_PATH = "/integrations"
    const val INFRASTRUCTURE_PATH = "/infrastructure"
    const val DNS_PATH = "/dns"
    const val MUKTI_MAHAL_PATH = "/mukti-mahal"
}
