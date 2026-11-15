<?php
/**
 * Google Storage Ecosystem PHP interoperability reader.
 * Catalog-only: deliberately performs no uploads, deletes, or provider API calls.
 */
declare(strict_types=1);

final class GoogleStorageCatalog
{
    private string $taxonomyPath;

    public function __construct(?string $taxonomyPath = null)
    {
        $this->taxonomyPath = $taxonomyPath ?? __DIR__ . '/taxonomy/google_storage_taxonomy.json';
    }

    /** @return array<string,mixed> */
    public function load(): array
    {
        if (!is_file($this->taxonomyPath) || !is_readable($this->taxonomyPath)) {
            throw new RuntimeException('Google taxonomy file is missing or unreadable');
        }
        $json = file_get_contents($this->taxonomyPath);
        if ($json === false) {
            throw new RuntimeException('Unable to read Google taxonomy file');
        }
        $data = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
        if (($data['ecosystem_id'] ?? null) !== 'GOOGLE_STORAGE_ECOSYSTEM') {
            throw new UnexpectedValueException('Unexpected taxonomy ecosystem_id');
        }
        return $data;
    }

    /** @return list<array<string,mixed>> */
    public function all(): array
    {
        $items = [];
        foreach ($this->load()['categories'] as $group) {
            foreach ($group['items'] as $item) {
                $items[] = $item;
            }
        }
        return $items;
    }

    /** @return array<string,mixed>|null */
    public function find(string $nameOrId): ?array
    {
        $needle = strtoupper(trim($nameOrId));
        foreach ($this->all() as $item) {
            if ($item['name'] === $needle || $item['id'] === $needle) {
                return $item;
            }
        }
        return null;
    }
}
