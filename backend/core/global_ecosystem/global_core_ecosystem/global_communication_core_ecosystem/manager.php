<?php
declare(strict_types=1);

/**
 * PHP interoperability facade for Communication Core metadata.
 * Python remains canonical. No provider credentials or live API calls here.
 */
final class CommunicationCoreManager
{
    public const ECOSYSTEM_ID = 'GLOBAL-COMMUNICATION-CORE-ECOSYSTEM';

    public static function normalizeResult(array $payload): array
    {
        $blocked = ['token', 'access_token', 'refresh_token', 'client_secret', 'api_key', 'secret'];
        foreach ($blocked as $key) {
            unset($payload[$key]);
        }
        $payload['ecosystem_id'] = self::ECOSYSTEM_ID;
        $payload['live_connection_verified'] = false;
        return $payload;
    }

    public static function masterCatalogPath(): string
    {
        return dirname(__DIR__, 4) . DIRECTORY_SEPARATOR . 'GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json';
    }

    public static function masterCatalogSummary(): array
    {
        $path = self::masterCatalogPath();
        if (!is_file($path)) {
            return ['available' => false, 'status' => 'MASTER_CATALOG_NOT_FOUND'];
        }
        $data = json_decode((string) file_get_contents($path), true);
        if (!is_array($data)) {
            return ['available' => false, 'status' => 'MASTER_CATALOG_INVALID'];
        }
        return [
            'available' => true,
            'catalogue_id' => $data['catalogue_id'] ?? null,
            'expansion' => $data['expansion'] ?? [],
            'counts' => $data['counts'] ?? [],
            'read_only' => true,
        ];
    }
}
