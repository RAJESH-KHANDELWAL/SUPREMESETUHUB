<?php
declare(strict_types=1);

/** Thin PHP interoperability facade; no Meta OAuth or API request is performed. */
final class MetaCoreManagerFacade
{
    public const ECOSYSTEM_ID = 'META-CORE-ECOSYSTEM';
    public const STATUS = 'CORE_CATALOG_ONLY';

    public static function status(): array
    {
        return [
            'success' => true,
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'name' => 'META CORE ECOSYSTEM',
            'status' => self::STATUS,
            'live_connection_verified' => false,
            'oauth_exchange_performed' => false,
            'api_calls_performed' => 0,
            'remote_operations_enabled' => false,
        ];
    }

    public static function sanitize(array $value): array
    {
        $blocked = ['token','access_token','refresh_token','client_secret','app_secret',
            'appsecret_proof','api_key','apikey','secret','secret_value','authorization',
            'password','verification_token'];
        $clean = [];
        foreach ($value as $key => $item) {
            if (in_array(strtolower((string) $key), $blocked, true)) continue;
            $clean[$key] = is_array($item) ? self::sanitize($item) : $item;
        }
        return $clean;
    }
}
