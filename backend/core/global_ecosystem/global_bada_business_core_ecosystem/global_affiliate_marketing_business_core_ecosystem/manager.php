<?php
/**
 * PHP 8+ read-only facade for affiliate CORE inventory and master catalog.
 * No provider API calls, authentication, persistence, or payouts are performed.
 */
final class GlobalAffiliateMarketingCoreManager
{
    public const ECOSYSTEM_ID = 'GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM';
    public const VERSION = '1.0.0';
    private const MASTER_CATALOG_ID = 'GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM';

    /** @return array<string, mixed> */
    public function masterCatalogInventory(): array
    {
        $path = dirname(__DIR__, 5) . DIRECTORY_SEPARATOR . 'GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json';
        if (!is_file($path)) {
            throw new RuntimeException('GLOBAL_SUPREME_MASTER_CATALOG_NOT_FOUND');
        }
        $catalog = json_decode((string) file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
        if (($catalog['catalogue_id'] ?? null) !== self::MASTER_CATALOG_ID) {
            throw new RuntimeException('GLOBAL_SUPREME_MASTER_CATALOG_ID_MISMATCH');
        }
        $entries = [];
        foreach (($catalog['sections'] ?? []) as $section) {
            foreach (($section['entries'] ?? []) as $entry) {
                $entry['section_id'] = $section['section_id'] ?? null;
                $entry['section_title'] = $section['title'] ?? null;
                $entries[] = $entry;
            }
        }
        $counts = $catalog['counts'] ?? [];
        $expansion = $catalog['expansion'] ?? [];
        $crossRefs = count(array_filter(
            $entries,
            static fn (array $entry): bool => ($entry['entry_kind'] ?? null) === 'cross_reference'
        ));
        $uniqueCount = count($entries) - $crossRefs;
        $target = $expansion['target_unique_entries'] ?? null;
        if (count($catalog['sections'] ?? []) !== ($counts['section_count'] ?? null)
            || count($entries) !== ($counts['source_numbered_entries'] ?? null)
            || $crossRefs !== ($counts['cross_reference_entries'] ?? null)
            || $uniqueCount !== ($counts['unique_catalogue_entries'] ?? null)
            || $uniqueCount !== ($expansion['current_unique_entries'] ?? null)
            || $target !== 2468
            || ($expansion['remaining_unique_entries'] ?? null) !== $target - $uniqueCount) {
            throw new RuntimeException('GLOBAL_SUPREME_MASTER_CATALOG_COUNT_MISMATCH');
        }
        return [
            'success' => true,
            'catalogue_id' => self::MASTER_CATALOG_ID,
            'access_mode' => 'READ_ONLY',
            'target_unique_entries' => $target,
            'current_unique_entries' => $uniqueCount,
            'remaining_unique_entries' => $target - $uniqueCount,
            'source_numbered_entries' => count($entries),
            'cross_reference_entries' => $crossRefs,
            'section_count' => count($catalog['sections']),
            'entries' => $entries,
        ];
    }

    /** @return array<string, mixed>|null */
    public function getMasterCatalogEntry(string $entryId): ?array
    {
        $needle = trim($entryId);
        if ($needle === '') {
            return null;
        }
        foreach ($this->masterCatalogInventory()['entries'] as $entry) {
            if (($entry['entry_id'] ?? null) === $needle) {
                return $entry;
            }
        }
        return null;
    }

    /** @return array<string, mixed> */
    public function health(): array
    {
        $required = ['README.md', '__init__.py', 'catalog.py', 'contracts.py',
            'manager.py', 'manager.php', 'models.py', 'module_service.py',
            'orchestrator.py', 'policies.py', 'service.py'];
        $checks = [];
        foreach ($required as $file) {
            $checks[$file] = is_file(__DIR__ . DIRECTORY_SEPARATOR . $file);
        }
        $healthy = !in_array(false, $checks, true);
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'version' => self::VERSION,
            'healthy' => $healthy,
            'status' => $healthy ? 'READY' : 'INCOMPLETE',
            'required_file_count' => count($required),
            'present_file_count' => count(array_filter($checks)),
            'file_checks' => $checks,
            'live_connections_verified' => false,
            'payout_execution_enabled' => false,
        ];
    }
}
