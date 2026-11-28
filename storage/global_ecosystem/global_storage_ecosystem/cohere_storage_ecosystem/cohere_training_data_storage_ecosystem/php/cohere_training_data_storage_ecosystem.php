<?php
/** Read-only PHP metadata contract for COHERE_TRAINING_DATA_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class CohereTrainingDataStorageEcosystem
{
    public const ECOSYSTEM_ID = 'COHERE_TRAINING_DATA_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'TRAINING_DATA';
    public const CATEGORY_GROUP = 'DATA_AND_STORAGE';

    /** @return array<string,mixed> */
    public function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'provider' => 'COHERE',
            'category' => self::CATEGORY,
            'category_group' => self::CATEGORY_GROUP,
            'connection_state' => 'NOT_CONFIGURED',
            'provider_product_verified' => false,
            'storage_operations_enabled' => false,
        ];
    }
}
