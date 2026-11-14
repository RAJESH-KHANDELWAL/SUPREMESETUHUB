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

final class GlobalProviderReference
{
    public function __construct(
        public readonly string $providerId,
        public readonly string $externalId
    ) {}

    public function toArray(): array
    {
        return ['provider_id' => $this->providerId, 'external_id' => $this->externalId];
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

final class GlobalResourceLifecycle
{
    public function __construct(
        public readonly string $state,
        public readonly ?string $createdAt = null,
        public readonly ?string $updatedAt = null
    ) {}

    public function toArray(): array
    {
        return ['state' => $this->state, 'created_at' => $this->createdAt, 'updated_at' => $this->updatedAt];
    }
}

final class GlobalResourceLocation
{
    public function __construct(
        public readonly ?string $region = null,
        public readonly ?string $zone = null,
        public readonly ?string $datacenter = null,
        public readonly ?string $location = null
    ) {}

    public function toArray(): array
    {
        return ['region' => $this->region, 'zone' => $this->zone, 'datacenter' => $this->datacenter, 'location' => $this->location];
    }
}

final class GlobalResourceCapacity
{
    public function __construct(
        public readonly ?string $cpu = null,
        public readonly ?string $memory = null,
        public readonly ?string $storage = null,
        public readonly ?string $bandwidth = null
    ) {}

    public function toArray(): array
    {
        return ['cpu' => $this->cpu, 'memory' => $this->memory, 'storage' => $this->storage, 'bandwidth' => $this->bandwidth];
    }
}
