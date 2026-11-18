<?php
/**
 * Read-only metadata contract for GOOGLE_STORAGE_ECOSYSTEM.
 * This file does not connect to Google APIs or perform storage operations.
 */

declare(strict_types=1);

return [
    'ecosystem_id' => 'GOOGLE_STORAGE_ECOSYSTEM',
    'package_name' => 'google_storage_ecosystem',
    'provider' => 'GOOGLE',
    'package_type' => 'STORAGE_TAXONOMY_AND_METADATA_FOUNDATION',
    'implementation_state' => 'TAXONOMY_AND_CATALOG_FOUNDATION',
    'external_connection_state' => 'NOT_CONFIGURED',
    'taxonomy_only' => true,
    'taxonomy_file' => 'taxonomy/google_storage_taxonomy.json',
    'category_index_file' => 'category_index.json',
    'taxonomy_group_count' => 18,
    'category_folder_count' => 184,
    'provider_product_verification_required' => true,
    'requires_authorized_credentials' => true,
    'requires_live_health_check' => true,
    'requires_end_to_end_tests' => true,
    'storage_operations_enabled' => false,
];
