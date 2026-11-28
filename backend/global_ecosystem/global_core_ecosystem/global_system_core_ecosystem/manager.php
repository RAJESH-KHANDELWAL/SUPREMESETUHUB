<?php
declare(strict_types=1);

/**
 * Read-only PHP facade for Global System Core metadata.
 * No shell execution, host mutation, package installation or API transport.
 */
final class GlobalSystemCoreManager
{
    private string $root;

    public function __construct(?string $root = null)
    {
        $this->root = $root ?? __DIR__;
    }

    private function readJson(string $file): array
    {
        $path = $this->root . DIRECTORY_SEPARATOR . $file;
        if (!is_file($path)) {
            throw new RuntimeException('SYSTEM_CORE_FILE_NOT_FOUND: ' . $file);
        }
        $decoded = json_decode((string) file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
        return is_array($decoded) ? $decoded : [];
    }

    public function status(): array
    {
        $index = $this->readJson('product_ecosystem_index.json');
        $manifest = $this->readJson('ecosystem_manifest.json');
        return [
            'success' => true,
            'ecosystem_id' => 'GLOBAL-SYSTEM-CORE-ECOSYSTEM',
            'provider_count' => (int) ($manifest['provider_count'] ?? 0),
            'product_count' => count($index['products'] ?? []),
            'domain_count' => count($manifest['domain_ids'] ?? []),
            'live_connections_verified' => false,
            'host_operations_performed' => 0,
        ];
    }

    public function listProducts(): array
    {
        $index = $this->readJson('product_ecosystem_index.json');
        return ['success' => true, 'count' => count($index['products'] ?? []), 'products' => $index['products'] ?? []];
    }
}
