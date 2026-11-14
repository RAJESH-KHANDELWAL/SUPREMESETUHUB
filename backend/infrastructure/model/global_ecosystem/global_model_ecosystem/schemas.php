<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class GlobalResourceIdentity
{
    public function __construct(
        public readonly string $resourceId,
        public readonly string $resourceType,
        public readonly ?string $providerId = null,
        public readonly ?string $externalId = null
    ) {}

    public function toArray(): array
    {
        return [
            'resource_id' => $this->resourceId,
            'resource_type' => $this->resourceType,
            'provider_id' => $this->providerId,
            'external_id' => $this->externalId,
        ];
    }
}

final class GlobalResourceRelationship
{
    public function __construct(
        public readonly string $sourceResourceId,
        public readonly string $targetResourceId,
        public readonly string $relationshipType,
        public readonly array $metadata = []
    ) {}

    public function toArray(): array
    {
        return [
            'source_resource_id' => $this->sourceResourceId,
            'target_resource_id' => $this->targetResourceId,
            'relationship_type' => $this->relationshipType,
            'metadata' => $this->metadata,
        ];
    }
}
