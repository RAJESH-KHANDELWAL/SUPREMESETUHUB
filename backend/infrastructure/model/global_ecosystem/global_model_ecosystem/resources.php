<?php
declare(strict_types=1);

namespace SupremeSetuHub\\Infrastructure\\Model\\GlobalEcosystem\\GlobalModelEcosystem;

final class GlobalResourceIdentity
{
    public function __construct(
        public string $resourceId,
        public string $resourceType,
        public string $providerId,
        public string $externalId
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
    public function __construct(public string $providerId, public string $externalId) {}

    public function toArray(): array
    {
        return ['provider_id' => $this->providerId, 'external_id' => $this->externalId];
    }
}

final class GlobalResourceLifecycle
{
    public function __construct(public string $state) {}

    public function toArray(): array
    {
        return ['state' => $this->state];
    }
}

final class GlobalResourceLocation
{
    public function __construct(
        public ?string $region = null,
        public ?string $zone = null,
        public ?string $country = null
    ) {}

    public function toArray(): array
    {
        return ['region' => $this->region, 'zone' => $this->zone, 'country' => $this->country];
    }
}

final class GlobalResourceCapacity
{
    public function __construct(
        public ?string $cpu = null,
        public ?string $memory = null,
        public ?string $storage = null
    ) {}

    public function toArray(): array
    {
        return ['cpu' => $this->cpu, 'memory' => $this->memory, 'storage' => $this->storage];
    }
}
