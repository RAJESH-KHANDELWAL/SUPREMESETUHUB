<?php
declare(strict_types=1);

/**
 * Thin PHP interoperability facade for IBM Core catalog status.
 * No IBM API transport, credential exchange, or remote operations occur here.
 */
final class IBMCoreManagerFacade
{
    public const ECOSYSTEM_ID = 'IBM-CORE-ECOSYSTEM';
    public const STATUS = 'CORE_CATALOG_ONLY';

    public static function status(): array
    {
        return [
            'success' => true,
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'name' => 'IBM CORE ECOSYSTEM',
            'status' => self::STATUS,
            'live_connection_verified' => false,
            'api_calls_performed' => 0,
            'remote_operations_enabled' => false,
        ];
    }

    public static function sanitize(array $value): array
    {
        $blocked = ['token', 'access_token', 'refresh_token', 'api_key', 'apikey',
            'secret', 'secret_value', 'client_secret', 'iam_api_key', 'authorization', 'password'];
        $clean = [];
        foreach ($value as $key => $item) {
            if (in_array(strtolower((string) $key), $blocked, true)) {
                continue;
            }
            $clean[$key] = is_array($item) ? self::sanitize($item) : $item;
        }
        return $clean;
    }
}
