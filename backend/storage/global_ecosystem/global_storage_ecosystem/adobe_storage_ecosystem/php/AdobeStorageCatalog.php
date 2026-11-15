<?php
/** Read-only Adobe Storage Ecosystem metadata. No provider API calls are made. */
final class AdobeStorageCatalog {
    public static function describe(): array {
        return [
            'ecosystem_id' => 'ADOBE_STORAGE_ECOSYSTEM',
            'provider' => 'ADOBE',
            'category_count' => 9,
            'external_connection_state' => 'NOT_CONFIGURED',
            'storage_operations_enabled' => false,
        ];
    }
}
