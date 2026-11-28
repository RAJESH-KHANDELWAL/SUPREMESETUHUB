<?php
/** Read-only PHP metadata contract for GLOBAL_INDIVIDUAL_PERSONAL_DATA_EXPORT_AND_PORTABILITY_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GlobalindividualpersonalDataExportAndPortabilitystorageecosystem
{
    public const ECOSYSTEM_ID = 'GLOBAL_INDIVIDUAL_PERSONAL_DATA_EXPORT_AND_PORTABILITY_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'PERSONAL_DATA_EXPORT_AND_PORTABILITY';
    public const CATEGORY_GROUP = 'DATA_RIGHTS_AND_LIFECYCLE';

    /** @return array<string,mixed> */
    public function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'provider' => 'GLOBAL_INDIVIDUAL',
            'category' => self::CATEGORY,
            'category_group' => self::CATEGORY_GROUP,
            'connection_state' => 'NOT_CONFIGURED',
            'provider_product_verified' => false,
            'storage_operations_enabled' => false,
        ];
    }
}
