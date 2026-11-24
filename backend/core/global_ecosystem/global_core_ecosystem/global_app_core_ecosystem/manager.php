<?php
declare(strict_types=1);

/** PHP interoperability facade for Global APP Core metadata and master catalog. */
final class GlobalAppCoreManager
{
    public const ECOSYSTEM_ID = 'GLOBAL-APP-CORE-ECOSYSTEM';
    public const MASTER_CATALOG_ID = 'GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM';
    public const MASTER_CATALOG_TARGET_UNIQUE_ENTRIES = 2468;
    public const MASTER_CATALOG_PATH = 'backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json';

    public static function masterCatalogReference(): array
    {
        return [
            'catalogue_id' => self::MASTER_CATALOG_ID,
            'source_path' => self::MASTER_CATALOG_PATH,
            'owner_layer' => 'GLOBAL_ENGINE_ECOSYSTEM',
            'target_unique_entries' => self::MASTER_CATALOG_TARGET_UNIQUE_ENTRIES,
            'access_mode' => 'READ_ONLY_ON_DEMAND',
            'source_of_truth' => true,
        ];
    }

    private static function loadMasterCatalog(): array
    {
        $root = dirname(__DIR__, 5);
        $path = $root . DIRECTORY_SEPARATOR . self::MASTER_CATALOG_PATH;
        if (!is_file($path) || !is_readable($path)) {
            throw new RuntimeException('GLOBAL_SUPREME_MASTER_CATALOG_NOT_FOUND');
        }
        $raw = file_get_contents($path);
        if ($raw === false) {
            throw new RuntimeException('GLOBAL_SUPREME_MASTER_CATALOG_READ_FAILED');
        }
        $catalog = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($catalog)
            || ($catalog['catalogue_id'] ?? null) !== self::MASTER_CATALOG_ID
            || !is_array($catalog['sections'] ?? null)) {
            throw new RuntimeException('GLOBAL_SUPREME_MASTER_CATALOG_INVALID');
        }
        return $catalog;
    }

    public static function masterCatalogInventory(bool $includeCrossReferences = true): array
    {
        $catalog = self::loadMasterCatalog();
        $entries = [];
        $sections = [];
        foreach ($catalog['sections'] as $section) {
            $sectionEntries = [];
            foreach (($section['entries'] ?? []) as $entry) {
                $row = $entry + [
                    'section_id' => $section['section_id'] ?? null,
                    'section_title' => $section['title'] ?? null,
                ];
                $entries[] = $row;
                if ($includeCrossReferences
                    || ($entry['entry_kind'] ?? null) !== 'cross_reference') {
                    $sectionEntries[] = $row;
                }
            }
            $sections[] = [
                'section_number' => $section['section_number'] ?? null,
                'section_id' => $section['section_id'] ?? null,
                'title' => $section['title'] ?? null,
                'entry_count' => count($sectionEntries),
                'entries' => $sectionEntries,
            ];
        }
        $counts = $catalog['counts'] ?? [];
        $expansion = $catalog['expansion'] ?? [];
        $sourceCount = count($entries);
        $crossCount = count(array_filter(
            $entries,
            static fn (array $entry): bool =>
                ($entry['entry_kind'] ?? null) === 'cross_reference'
        ));
        $uniqueCount = $sourceCount - $crossCount;
        $target = $expansion['target_unique_entries'] ?? null;
        $remaining = $expansion['remaining_unique_entries'] ?? null;
        if ($sourceCount !== ($counts['source_numbered_entries'] ?? null)
            || $crossCount !== ($counts['cross_reference_entries'] ?? null)
            || $uniqueCount !== ($counts['unique_catalogue_entries'] ?? null)
            || $uniqueCount !== ($expansion['current_unique_entries'] ?? null)
            || $target !== self::MASTER_CATALOG_TARGET_UNIQUE_ENTRIES
            || $remaining !== $target - $uniqueCount) {
            throw new RuntimeException('GLOBAL_SUPREME_MASTER_CATALOG_COUNT_MISMATCH');
        }
        return [
            'success' => true, 'catalogue_id' => self::MASTER_CATALOG_ID,
            'source_path' => self::MASTER_CATALOG_PATH,
            'owner_layer' => 'GLOBAL_ENGINE_ECOSYSTEM', 'access_mode' => 'READ_ONLY',
            'target_unique_entries' => $target, 'current_unique_entries' => $uniqueCount,
            'remaining_unique_entries' => $remaining, 'source_numbered_entries' => $sourceCount,
            'cross_reference_entries' => $crossCount, 'section_count' => count($sections),
            'entries' => $includeCrossReferences ? $entries : array_values(array_filter(
                $entries,
                static fn (array $entry): bool =>
                    ($entry['entry_kind'] ?? null) !== 'cross_reference'
            )),
            'sections' => $sections,
        ];
    }

    public static function getMasterCatalogEntry(string $entryId): ?array
    {
        $needle = trim($entryId);
        if ($needle === '') {
            return null;
        }
        foreach (self::masterCatalogInventory(true)['entries'] as $entry) {
            if (($entry['entry_id'] ?? null) === $needle) {
                return $entry;
            }
        }
        return null;
    }
}
