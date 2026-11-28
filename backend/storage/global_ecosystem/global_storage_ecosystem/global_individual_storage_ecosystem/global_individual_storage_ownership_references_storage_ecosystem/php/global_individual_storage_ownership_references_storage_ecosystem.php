<?php
/** Read-only PHP metadata contract for GLOBAL_INDIVIDUAL_STORAGE_OWNERSHIP_REFERENCES_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GlobalindividualstorageOwnershipReferencesstorageecosystem
{
    public const ECOSYSTEM_ID = 'GLOBAL_INDIVIDUAL_STORAGE_OWNERSHIP_REFERENCES_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'STORAGE_OWNERSHIP_REFERENCES';
    public const CATEGORY_GROUP = 'IDENTITY_AND_OWNERSHIP';

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
