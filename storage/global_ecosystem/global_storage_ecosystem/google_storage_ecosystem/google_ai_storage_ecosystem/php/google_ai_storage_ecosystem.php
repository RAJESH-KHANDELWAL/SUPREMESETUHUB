<?php
/** Read-only PHP metadata contract for GOOGLE_AI_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GoogleAiStorageEcosystem
{
    public const ECOSYSTEM_ID = 'GOOGLE_AI_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'AI';
    public const CATEGORY_GROUP = 'AI_AND_INTELLIGENCE';

    /** @return array<string,mixed> */
    public function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'provider' => 'GOOGLE',
            'category' => self::CATEGORY,
            'category_group' => self::CATEGORY_GROUP,
            'connection_state' => 'NOT_CONFIGURED',
            'provider_product_verified' => false,
            'storage_operations_enabled' => false,
        ];
    }
}
