package com.mainbasefoundation.android

import java.io.IOException
import java.net.HttpURLConnection
import java.net.URL

object ApiClient {
    private const val CONNECT_TIMEOUT = 15000
    private const val READ_TIMEOUT = 30000

    fun get(path: String, bearerToken: String? = null): ApiResponse =
        request(method = "GET", path = path, bearerToken = bearerToken)

    fun post(path: String, jsonBody: String, bearerToken: String? = null): ApiResponse =
        request(method = "POST", path = path, jsonBody = jsonBody, bearerToken = bearerToken)

    private fun request(
        method: String,
        path: String,
        jsonBody: String? = null,
        bearerToken: String? = null
    ): ApiResponse {
        val baseUrl = ApiConfig.BASE_URL.trim()
        if (baseUrl.isEmpty() || !baseUrl.startsWith("https://", ignoreCase = true)) {
            return ApiResponse(
                success = false,
                statusCode = -1,
                body = "",
                error = "Configure SUPREME_API_BASE_URL with the deployed HTTPS backend URL."
            )
        }

        val endpoint = baseUrl.trimEnd('/') + "/" + path.trimStart('/')
        var connection: HttpURLConnection? = null
        return try {
            connection = (URL(endpoint).openConnection() as HttpURLConnection).apply {
                requestMethod = method
                connectTimeout = CONNECT_TIMEOUT
                readTimeout = READ_TIMEOUT
                setRequestProperty("Accept", "application/json")
                setRequestProperty("Content-Type", "application/json")
                setRequestProperty("X-Client", "MAIN-BASE-FOUNDATION-ANDROID")
                if (!bearerToken.isNullOrBlank()) {
                    setRequestProperty("Authorization", "Bearer $bearerToken")
                }
                if (method == "POST") {
                    doOutput = true
                    jsonBody?.let { body ->
                        outputStream.use { stream ->
                            stream.write(body.toByteArray(Charsets.UTF_8))
                        }
                    }
                }
            }

            val statusCode = connection.responseCode
            val responseStream = if (statusCode in 200..399) {
                connection.inputStream
            } else {
                connection.errorStream
            }
            val responseBody = responseStream?.bufferedReader()?.use { it.readText() } ?: ""
            ApiResponse(
                success = statusCode in 200..299,
                statusCode = statusCode,
                body = responseBody,
                error = if (statusCode !in 200..299) responseBody else null
            )
        } catch (exception: IOException) {
            ApiResponse(
                success = false,
                statusCode = -1,
                body = "",
                error = exception.message ?: "Network request failed."
            )
        } finally {
            connection?.disconnect()
        }
    }
}

data class ApiResponse(
    val success: Boolean,
    val statusCode: Int,
    val body: String,
    val error: String?
)
