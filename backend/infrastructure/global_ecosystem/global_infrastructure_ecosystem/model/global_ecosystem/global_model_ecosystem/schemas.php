<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class GlobalResourceSchema
{
    public static function requiredFields(): array
    {
        return ['resource_id', 'resource_type', 'category'];
    }

    public static function fields(): array
    {
        return [
            'resource_id' => 'string',
            'resource_type' => 'string',
            'category' => 'string',
            'provider_id' => 'string',
            'external_id' => 'string',
            'state' => 'string',
            'location' => 'array',
            'capacity' => 'array',
        ];
    }
}
