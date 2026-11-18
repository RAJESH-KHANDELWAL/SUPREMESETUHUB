<?php
/** Read-only PHP metadata contract for COHERE_AI_AGENTS_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class CohereAiAgentsStorageEcosystem
{
    public const ECOSYSTEM_ID = 'COHERE_AI_AGENTS_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'AI_AGENTS';
    public const CATEGORY_GROUP = 'RESEARCH_AND_ADVANCED_AI';

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
