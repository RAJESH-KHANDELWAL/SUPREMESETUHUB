<?php
declare(strict_types=1);
/** Thin PHP 8+ metadata facade. No provider API calls or secret access. */
final class GlobalWebsiteCoreManager
{
    public const ECOSYSTEM_ID = 'GLOBAL-WEBSITE-CORE-ECOSYSTEM';
    public const ECOSYSTEM_NAME = 'GLOBAL WEBSITE CORE ECOSYSTEM';

    public function status(): array
    {
        return [
            'success' => true, 'layer' => 'CORE',
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'ecosystem' => self::ECOSYSTEM_NAME,
            'status' => 'CORE_CATALOG_ONLY',
            'live_connection_verified' => false,
            'remote_operations_enabled' => false,
            'api_calls_performed' => 0,
            'credential_storage' => 'EXTERNAL_SECRET_STORE_ONLY',
        ];
    }

    public function sanitize(array $payload): array
    {
        $blocked = ['access_token', 'refresh_token', 'client_secret', 'api_key',
            'private_key', 'password', 'authorization'];
        $clean = [];
        foreach ($payload as $key => $value) {
            if (in_array(strtolower((string) $key), $blocked, true)) continue;
            $clean[$key] = is_array($value) ? $this->sanitize($value) : $value;
        }
        return $clean;
    }
}
