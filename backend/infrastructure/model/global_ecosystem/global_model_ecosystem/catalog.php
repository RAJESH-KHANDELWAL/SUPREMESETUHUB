<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class ModelCatalog
{
    public const MODEL_FAMILY = 'GLOBAL_MODEL_ECOSYSTEM';

    public static function all(): array
    {
        return [
            'resource_identity' => ['required_fields' => ['resource_id', 'resource_type']],
            'resource_category' => ['categories' => ResourceCategories::all()],
            'resource_relationship' => ['relationship_types' => RelationshipTypes::all()],
            'provider_reference' => ['fields' => ['provider_id', 'external_id']],
            'lifecycle' => ['states' => ['PLANNED', 'PROVISIONING', 'ACTIVE', 'DEGRADED', 'SUSPENDED', 'FAILED', 'RETIRED']],
            'location' => ['fields' => ['region', 'zone', 'datacenter', 'location']],
            'capacity' => ['fields' => ['cpu', 'memory', 'storage', 'bandwidth']],
        ];
    }
}
