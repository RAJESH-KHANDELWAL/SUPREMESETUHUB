<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class GlobalResourceIdentity
{
    public function __construct(
        public readonly string $resourceId,
        public readonly string $resourceType,
        public readonly string $providerId,
        public readonly string $externalId
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
        public readonly string $relationshipType
    ) {}

    public function toArray(): array
    {
        return [
            'source_resource_id' => $this->sourceResourceId,
            'target_resource_id' => $this->targetResourceId,
            'relationship_type' => $this->relationshipType,
        ];
    }
}

final class GlobalResourceLifecycle
{
    public function __construct(public readonly string $state) {}

    public function toArray(): array
    {
        return ['state' => $this->state];
    }
}

final class GlobalResourceLocation
{
    public function __construct(
        public readonly ?string $country = null,
        public readonly ?string $region = null,
        public readonly ?string $zone = null,
        public readonly ?string $city = null
    ) {}

    public function toArray(): array
    {
        return array_filter([
            'country' => $this->country,
            'region' => $this->region,
            'zone' => $this->zone,
            'city' => $this->city,
        ], static fn ($value): bool => $value !== null);
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
        return array_filter([
            'cpu' => $this->cpu,
            'memory' => $this->memory,
            'storage' => $this->storage,
            'bandwidth' => $this->bandwidth,
        ], static fn ($value): bool => $value !== null);
    }
}
