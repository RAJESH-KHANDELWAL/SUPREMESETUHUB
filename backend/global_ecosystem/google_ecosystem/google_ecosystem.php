<?php
/**
 * Google Ecosystem read-only PHP client.
 *
 * Calls the authenticated SUPREMESETUHUB catalog API. This is metadata access,
 * not a live Google account connection or Gmail/Drive operation.
 *
 * Server-side environment variables:
 *   SUPREMESETUHUB_API_BASE_URL
 *   SUPREMESETUHUB_ADMIN_TOKEN
 */
declare(strict_types=1);

if (!class_exists('GoogleEcosystemClient')) {
    final class GoogleEcosystemClient
    {
        private string $baseUrl;
        private string $token;

        public function __construct(?string $baseUrl = null, ?string $token = null)
        {
            $this->baseUrl = rtrim($baseUrl ?? (getenv('SUPREMESETUHUB_API_BASE_URL') ?: ''), '/');
            $this->token = $token ?? (getenv('SUPREMESETUHUB_ADMIN_TOKEN') ?: '');

            if ($this->baseUrl === '' || $this->token === '') {
                throw new RuntimeException('Set SUPREMESETUHUB_API_BASE_URL and SUPREMESETUHUB_ADMIN_TOKEN server-side.');
            }
            if (parse_url($this->baseUrl, PHP_URL_SCHEME) !== 'https') {
                throw new RuntimeException('The API base URL must use HTTPS.');
            }
        }

        public function status(): array
        {
            return $this->get('/api/v1/google-ecosystem/status');
        }

        public function products(): array
        {
            return $this->get('/api/v1/google-ecosystem/products');
        }

        public function product(string $productId): array
        {
            $productId = strtolower(trim($productId));
            if (!preg_match('/^[a-z0-9_-]+$/', $productId)) {
                throw new InvalidArgumentException('Invalid Google product ID.');
            }
            return $this->get('/api/v1/google-ecosystem/products/' . rawurlencode($productId));
        }

        private function get(string $path): array
        {
            if (!function_exists('curl_init')) {
                throw new RuntimeException('PHP cURL extension is required.');
            }

            $handle = curl_init($this->baseUrl . $path);
            curl_setopt_array($handle, [
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_HTTPGET => true,
                CURLOPT_CONNECTTIMEOUT => 5,
                CURLOPT_TIMEOUT => 15,
                CURLOPT_FOLLOWLOCATION => false,
                CURLOPT_SSL_VERIFYPEER => true,
                CURLOPT_SSL_VERIFYHOST => 2,
                CURLOPT_HTTPHEADER => [
                    'Accept: application/json',
                    'Authorization: Bearer ' . $this->token,
                ],
            ]);
            $body = curl_exec($handle);
            $status = (int) curl_getinfo($handle, CURLINFO_HTTP_CODE);
            $error = curl_error($handle);
            curl_close($handle);

            if ($body === false) {
                throw new RuntimeException('SUPREMESETUHUB API request failed: ' . $error);
            }
            $decoded = json_decode($body, true);
            if (!is_array($decoded)) {
                throw new RuntimeException('SUPREMESETUHUB API returned invalid JSON.');
            }
            if ($status < 200 || $status >= 300) {
                throw new RuntimeException('SUPREMESETUHUB API returned HTTP ' . $status . ': ' . (string) ($decoded['detail'] ?? 'Request failed'));
            }
            return $decoded;
        }
    }
}
