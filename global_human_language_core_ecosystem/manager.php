<?php
/**
 * PHP metadata facade for Global Human Language CORE.
 * Read-only parity layer. No provider API calls, secrets, or persistence.
 */
declare(strict_types=1);

final class GlobalHumanLanguageCoreManager
{
    public const ECOSYSTEM_ID = 'GLOBAL-HUMAN-LANGUAGE-CORE-ECOSYSTEM';
    public const STATUS = 'CORE_CATALOG_ONLY';
    public const MASTER_CATALOG_PATH = 'backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json';

    public static function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'status' => self::STATUS,
            'layer' => 'CORE',
            'master_catalog_source' => self::MASTER_CATALOG_PATH,
            'master_catalog_read_only' => true,
            'live_provider_connections_verified' => false,
            'api_calls_performed' => 0,
        ];
    }

    public static function loadMasterCatalog(string $repositoryRoot): array
    {
        $path = rtrim($repositoryRoot, DIRECTORY_SEPARATOR)
            . DIRECTORY_SEPARATOR . self::MASTER_CATALOG_PATH;
        if (!is_file($path)) {
            throw new RuntimeException('MASTER_ECOSYSTEM_CATALOG_NOT_FOUND');
        }
        $decoded = json_decode((string) file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($decoded)) {
            throw new RuntimeException('MASTER_ECOSYSTEM_CATALOG_INVALID');
        }
        return $decoded;
    }

    public static function languageEntries(array $catalog): array
    {
        $matches = [];
        foreach (($catalog['sections'] ?? []) as $section) {
            foreach (($section['entries'] ?? []) as $entry) {
                if (($entry['entry_id'] ?? null) === 'S02_language') {
                    $matches[] = $entry + [
                        'source_section_id' => $section['section_id'] ?? null,
                        'source_section_title' => $section['title'] ?? null,
                    ];
                }
            }
        }
        return $matches;
    }
}
