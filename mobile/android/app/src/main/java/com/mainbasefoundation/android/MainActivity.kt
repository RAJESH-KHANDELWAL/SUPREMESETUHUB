package com.mainbasefoundation.android

import android.annotation.SuppressLint
import android.content.ActivityNotFoundException
import android.content.Intent
import android.graphics.Color
import android.net.Uri
import android.os.Bundle
import android.view.ViewGroup
import android.webkit.WebChromeClient
import android.webkit.WebResourceRequest
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AppCompatActivity
import androidx.webkit.WebSettingsCompat
import androidx.webkit.WebViewFeature

class MainActivity : AppCompatActivity() {

    private lateinit var webView: WebView

    private val appUrl = "https://rajeshkhandelwalofficial.com"
    private val internalHosts = setOf(
        "rajeshkhandelwalofficial.com",
        "www.rajeshkhandelwalofficial.com"
    )

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        webView = WebView(this)

        webView.layoutParams = ViewGroup.LayoutParams(
            ViewGroup.LayoutParams.MATCH_PARENT,
            ViewGroup.LayoutParams.MATCH_PARENT
        )

        webView.setBackgroundColor(Color.WHITE)

        webView.settings.apply {
            javaScriptEnabled = true
            domStorageEnabled = true
            databaseEnabled = true

            allowFileAccess = false
            allowContentAccess = false

            builtInZoomControls = false
            displayZoomControls = false

            javaScriptCanOpenWindowsAutomatically = false
            setSupportMultipleWindows(false)
        }

        if (WebViewFeature.isFeatureSupported(WebViewFeature.FORCE_DARK)) {
            WebSettingsCompat.setForceDark(
                webView.settings,
                WebSettingsCompat.FORCE_DARK_OFF
            )
        }

        webView.webViewClient = object : WebViewClient() {

            override fun shouldOverrideUrlLoading(
                view: WebView?,
                request: WebResourceRequest?
            ): Boolean {
                val uri = request?.url ?: return true
                return handleNavigation(uri)
            }

            @Suppress("DEPRECATION")
            override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
                val uri = url?.let { runCatching { Uri.parse(it) }.getOrNull() } ?: return true
                return handleNavigation(uri)
            }
        }

        webView.webChromeClient = WebChromeClient()

        setContentView(webView)
        webView.loadUrl(appUrl)

        onBackPressedDispatcher.addCallback(
            this,
            object : OnBackPressedCallback(true) {
                override fun handleOnBackPressed() {
                    if (webView.canGoBack()) {
                        webView.goBack()
                    } else {
                        finish()
                    }
                }
            }
        )
    }

    private fun handleNavigation(uri: Uri): Boolean {
        val scheme = uri.scheme?.lowercase() ?: return true
        val host = uri.host?.lowercase()

        // Only the production HTTPS site is allowed to navigate inside the app.
        if (scheme == "https" && host != null && host in internalHosts) {
            return false
        }

        // Never open arbitrary/custom schemes from a WebView.
        if (scheme !in setOf("https", "http", "mailto", "tel")) {
            return true
        }

        // External web links and contact links are handed to the user's browser/app.
        return try {
            startActivity(Intent(Intent.ACTION_VIEW, uri))
            true
        } catch (_: ActivityNotFoundException) {
            true
        } catch (_: SecurityException) {
            true
        }
    }

    override fun onDestroy() {
        webView.apply {
            stopLoading()
            webChromeClient = null
            webViewClient = WebViewClient()
            destroy()
        }

        super.onDestroy()
    }
}
