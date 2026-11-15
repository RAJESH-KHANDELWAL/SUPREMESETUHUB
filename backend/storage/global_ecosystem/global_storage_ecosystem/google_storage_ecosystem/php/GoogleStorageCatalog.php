<?php
/** Read-only PHP reader for the shared Google storage taxonomy JSON. */
declare(strict_types=1);
final class GoogleStorageCatalog
{
    private string $taxonomyPath;
    public function __construct(?string $taxonomyPath = null)
    {
        $this->taxonomyPath = $taxonomyPath ?? __DIR__ . '/../taxonomy/google_storage_taxonomy.json';
    }
    /** @return array<string,mixed> */
    public function load(): array
    {
        if (!is_file($this->taxonomyPath) || !is_readable($this->taxonomyPath)) {
            throw new RuntimeException('Google taxonomy file is missing or unreadable');
        }
        $raw = file_get_contents($this->taxonomyPath);
        if ($raw === false) throw new RuntimeException('Unable to read Google taxonomy file');
        $data = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
        if (($data['ecosystem_id'] ?? null) !== 'GOOGLE_STORAGE_ECOSYSTEM') {
            throw new UnexpectedValueException('Unexpected taxonomy ecosystem_id');
        }
        return $data;
    }
    /** @return list<array<string,string>> */
    public function all(): array
    {
        $rows = [];
        foreach ($this->load()['groups'] as $group) foreach ($group['categories'] as $category) {
            $rows[] = ['group'=>$group['group'],'category'=>$category,'name'=>'GOOGLE_'.$category.'_STORAGE_ECOSYSTEM','status'=>'CATALOG_ONLY','provider_product_verified'=>'false'];
        }
        return $rows;
    }
    /** @return array<string,string>|null */
    public function find(string $nameOrCategory): ?array
    {
        $needle = strtoupper(trim($nameOrCategory));
        foreach ($this->all() as $row) if ($row['name'] === $needle || $row['category'] === $needle) return $row;
        return null;
    }
}
