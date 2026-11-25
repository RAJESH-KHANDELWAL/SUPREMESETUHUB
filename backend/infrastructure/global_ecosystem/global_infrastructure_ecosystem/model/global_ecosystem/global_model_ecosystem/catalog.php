<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class ResourceCategories
{
    public static function all(): array
    {
        return [
            'compute' => ['server', 'virtual_machine', 'container', 'function'],
            'storage' => ['block_storage', 'object_storage', 'file_storage', 'database'],
            'network' => ['network', 'load_balancer', 'firewall', 'gateway'],
            'platform' => ['runtime', 'orchestrator', 'service'],
        ];
    }
}

final class ModelCatalog
{
    public static function all(): array
    {
        return [
            'resource_identity' => GlobalResourceIdentity::class,
            'resource_provider_reference' => GlobalProviderReference::class,
            'resource_relationship' => GlobalResourceRelationship::class,
            'resource_lifecycle' => GlobalResourceLifecycle::class,
            'resource_location' => GlobalResourceLocation::class,
            'resource_capacity' => GlobalResourceCapacity::class,
            'resource_category' => ResourceCategories::all(),
            'relationship_types' => RelationshipTypes::all(),
        ];
    }
}
