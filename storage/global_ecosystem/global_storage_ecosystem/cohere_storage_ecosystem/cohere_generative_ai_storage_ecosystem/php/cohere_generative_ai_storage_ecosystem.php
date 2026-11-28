<?php
/** Read-only PHP metadata contract for COHERE_GENERATIVE_AI_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class CohereGenerativeAiStorageEcosystem
{
    public const ECOSYSTEM_ID = 'COHERE_GENERATIVE_AI_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'GENERATIVE_AI';
    public const CATEGORY_GROUP = 'AI_MODELS_AND_INFERENCE';

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
