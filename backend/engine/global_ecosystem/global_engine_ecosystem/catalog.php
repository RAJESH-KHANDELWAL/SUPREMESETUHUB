<?php
declare(strict_types=1);

/**
 * Read-only PHP bridge for the GLOBAL TO SUPREME master planning catalog.
 * This validates catalog data only; it does not claim live integrations.
 */
final class GlobalSupremeEcosystemCatalog
{
    public const TARGET_UNIQUE_ENTRIES = 2468;

    public static function load(?string $catalogPath = null): array
    {
        $path = $catalogPath ?? dirname(__DIR__, 3) . '/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json';
        if (!is_file($path)) {
            throw new RuntimeException('Master ecosystem catalog not found: ' . $path);
        }

        $json = file_get_contents($path);
        if ($json === false) {
            throw new RuntimeException('Unable to read master ecosystem catalog.');
        }

        $catalog = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($catalog) || ($catalog['catalogue_id'] ?? null) !== 'GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM') {
            throw new UnexpectedValueException('Unexpected master ecosystem catalog identity.');
        }

        return $catalog;
    }

    public static function summary(?string $catalogPath = null): array
    {
        $catalog = self::load($catalogPath);
        $sections = $catalog['sections'] ?? null;
        if (!is_array($sections) || $sections === []) {
            throw new UnexpectedValueException('Master catalog must contain a non-empty sections list.');
        }

        $seenSectionIds = [];
        $seenEntryIds = [];
        $seenNames = [];
        $canonicalIds = [];
        $pendingReferences = [];
        $sourceCount = 0;
        $uniqueCount = 0;
        $crossReferenceCount = 0;
        $capabilityLevelCount = 0;
        $sectionSummary = [];

        foreach ($sections as $sectionIndex => $section) {
            $sectionId = trim((string)($section['section_id'] ?? ''));
            if ($sectionId === '' || isset($seenSectionIds[$sectionId])) {
                throw new UnexpectedValueException('Missing or duplicate section_id: ' . $sectionId);
            }
            if (($section['section_number'] ?? null) !== $sectionIndex + 1) {
                throw new UnexpectedValueException('Section numbering must be contiguous: ' . $sectionId);
            }
            $seenSectionIds[$sectionId] = true;
            $entries = $section['entries'] ?? null;
            if (!is_array($entries)) {
                throw new UnexpectedValueException('Section entries must be a list: ' . $sectionId);
            }

            $sectionUnique = 0;
            $sectionReferences = 0;
            foreach ($entries as $entryIndex => $entry) {
                $entryId = trim((string)($entry['entry_id'] ?? ''));
                $name = trim((string)($entry['name'] ?? ''));
                $kind = trim((string)($entry['entry_kind'] ?? ''));
                if ($entryId === '' || isset($seenEntryIds[$entryId])) {
                    throw new UnexpectedValueException('Missing or duplicate entry_id: ' . $entryId);
                }
                if ($name === '' || $kind === '') {
                    throw new UnexpectedValueException('Entry requires name and entry_kind: ' . $entryId);
                }
                if (($entry['position'] ?? null) !== $entryIndex + 1) {
                    throw new UnexpectedValueException('Entry positions must be contiguous: ' . $entryId);
                }
                $seenEntryIds[$entryId] = true;
                $sourceCount++;

                if ($kind === 'cross_reference') {
                    $canonicalId = trim((string)($entry['canonical_entry_id'] ?? ''));
                    if ($canonicalId === '') {
                        throw new UnexpectedValueException('Cross-reference requires canonical_entry_id: ' . $entryId);
                    }
                    $pendingReferences[] = [$entryId, $canonicalId];
                    $sectionReferences++;
                    $crossReferenceCount++;
                    continue;
                }

                $normalizedName = mb_strtolower(preg_replace('/\s+/', ' ', $name) ?? $name);
                if (isset($seenNames[$normalizedName])) {
                    throw new UnexpectedValueException('Duplicate unique catalog entry name: ' . $name);
                }
                $seenNames[$normalizedName] = true;
                $canonicalIds[$entryId] = true;
                $sectionUnique++;
                $uniqueCount++;
                if ($kind === 'capability_level') {
                    $capabilityLevelCount++;
                }
            }

            $sectionSummary[] = [
                'section_number' => $section['section_number'],
                'section_id' => $sectionId,
                'title' => $section['title'] ?? null,
                'source_entry_count' => count($entries),
                'unique_entry_count' => $sectionUnique,
                'cross_reference_count' => $sectionReferences,
            ];
        }

        foreach ($pendingReferences as [$entryId, $canonicalId]) {
            if (!isset($canonicalIds[$canonicalId])) {
                throw new UnexpectedValueException(
                    'Cross-reference ' . $entryId . ' points to missing/non-canonical entry ' . $canonicalId
                );
            }
        }

        $expansion = $catalog['expansion'] ?? [];
        $counts = $catalog['counts'] ?? [];
        $target = (int)($expansion['target_unique_entries'] ?? 0);
        if ($target !== self::TARGET_UNIQUE_ENTRIES) {
            throw new UnexpectedValueException('Catalog target must be exactly ' . self::TARGET_UNIQUE_ENTRIES);
        }

        $actualCounts = [
            'section_count' => count($sections),
            'source_numbered_entries' => $sourceCount,
            'unique_catalogue_entries' => $uniqueCount,
            'cross_reference_entries' => $crossReferenceCount,
            'capability_levels' => $capabilityLevelCount,
        ];
        foreach ($actualCounts as $key => $actual) {
            if (($counts[$key] ?? null) !== $actual) {
                throw new UnexpectedValueException('Catalog counts.' . $key . ' does not match actual entries.');
            }
        }

        $remaining = max($target - $uniqueCount, 0);
        if (($expansion['current_unique_entries'] ?? null) !== $uniqueCount) {
            throw new UnexpectedValueException('Catalog current_unique_entries does not match actual entries.');
        }
        if (($expansion['remaining_unique_entries'] ?? null) !== $remaining) {
            throw new UnexpectedValueException('Catalog remaining_unique_entries does not match actual entries.');
        }
        if ($uniqueCount > $target) {
            throw new UnexpectedValueException('Catalog unique entries exceed the exact target.');
        }

        return [
            'success' => true,
            'catalogue_id' => $catalog['catalogue_id'],
            'section_count' => count($sections),
            'source_numbered_entry_count' => $sourceCount,
            'unique_entry_count' => $uniqueCount,
            'cross_reference_count' => $crossReferenceCount,
            'capability_level_count' => $capabilityLevelCount,
            'target_unique_entry_count' => $target,
            'remaining_unique_entries' => $remaining,
            'target_reached' => $uniqueCount === $target,
            'expansion_status' => $uniqueCount === $target ? 'TARGET_REACHED' : 'FOUNDATION_CATALOG_ONLY',
            'sections' => $sectionSummary,
        ];
    }
}
