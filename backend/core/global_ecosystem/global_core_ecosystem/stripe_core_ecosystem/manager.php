<?php
declare(strict_types=1);

/**
 * PHP interoperability facade for Stripe Core metadata.
 * Python remains the canonical registry and orchestration implementation.
 * This facade never calls Stripe APIs or accepts raw payment credentials.
 */
final class StripeCoreManager
{
    public const ECOSYSTEM_ID = 'STRIPE-CORE-ECOSYSTEM';
    public const MASTER_CATALOG_PATH = 'backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json';
    public const MASTER_CATALOG_TARGET = 2468;

    private const SECRET_KEYS = [
        'token', 'access_token', 'refresh_token', 'client_secret',
        'api_key', 'secret', 'stripe_secret_key', 'webhook_secret',
        'authorization', 'pan', 'cvc', 'card_number',
    ];

    public static function sanitize(array $payload): array
    {
        $safe = [];
        foreach ($payload as $key => $value) {
            if (in_array(strtolower((string) $key), self::SECRET_KEYS, true)) {
                continue;
            }
            if (is_array($value)) {
                $value = self::sanitize($value);
            }
            $safe[$key] = $value;
        }
        return $safe;
    }

    public static function normalizeResult(array $payload): array
    {
        $safe = self::sanitize($payload);
        $safe['ecosystem_id'] = self::ECOSYSTEM_ID;
        $safe['live_connection_verified'] = false;
        $safe['api_calls_performed'] = 0;
        return $safe;
    }

    public static function masterCatalogReference(): array
    {
        return [
            'path' => self::MASTER_CATALOG_PATH,
            'target_unique_entries' => self::MASTER_CATALOG_TARGET,
            'access_mode' => 'READ_ONLY_ON_DEMAND',
            'source_modified' => false,
        ];
    }
}
