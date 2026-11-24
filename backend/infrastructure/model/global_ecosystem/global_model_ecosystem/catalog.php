<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class ModelCatalog
{
    public static function all(): array
    {
        return [
            'resource_identity' => GlobalResourceIdentity::class,
            'provider_reference' => GlobalProviderReference::class,
            'resource_lifecycle' => GlobalResourceLifecycle::class,
            'resource_location' => GlobalResourceLocation::class,
            'resource_capacity' => GlobalResourceCapacity::class,
            'resource_relationship' => GlobalResourceRelationship::class,
            'resource_category' => ResourceCategories::all(),
        ];
    }
}
