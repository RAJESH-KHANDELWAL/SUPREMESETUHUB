<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class RelationshipTypes
{
    public static function all(): array
    {
        return [
            'HOSTS',
            'USES',
            'DEPENDS_ON',
            'CONNECTS_TO',
            'CONTAINS',
            'MANAGES',
            'REPLICATES',
            'BACKS_UP',
        ];
    }
}
