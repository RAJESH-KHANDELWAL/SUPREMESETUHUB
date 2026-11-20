<?php
declare(strict_types=1);

/**
 * Global AI Core PHP interoperability facade.
 * Metadata only: no provider authentication, HTTP requests or inference.
 */
final class GlobalAICoreManager
{
    public const ECOSYSTEM_ID = 'GLOBAL-AI-CORE-ECOSYSTEM';
    public const MASTER_CATALOG_TARGET_UNIQUE_ENTRIES = 2468;

    public static function masterCatalogReference(): array
    {
        return [
            'catalogue_id' => 'GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM',
            'source_path' => 'backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json',
            'owner_layer' => 'GLOBAL_ENGINE_ECOSYSTEM',
            'target_unique_entries' => self::MASTER_CATALOG_TARGET_UNIQUE_ENTRIES,
            'loaded_by_global_ai_core' => false,
        ];
    }

    public static function sanitize(array $payload): array
    {
        $blocked = [
            'token', 'access_token', 'refresh_token', 'client_secret',
            'api_key', 'secret', 'authorization', 'password',
            'credential_value', 'private_key',
        ];
        $safe = [];
        foreach ($payload as $key => $value) {
            if (in_array(strtolower((string) $key), $blocked, true)) {
                continue;
            }
            $safe[$key] = is_array($value) ? self::sanitize($value) : $value;
        }
        return $safe;
    }
}
