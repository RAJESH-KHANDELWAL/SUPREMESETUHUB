<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class RelationshipTypes
{
    public static function all(): array
    {
        return [
            'CONTAINS', 'HOSTS', 'RUNS_ON', 'CONNECTED_TO', 'USES', 'DEPENDS_ON',
            'SERVES', 'ROUTES_TO', 'BACKS_UP', 'PROTECTED_BY', 'DELIVERED_BY',
            'REPLICATES_TO', 'MONITORED_BY',
        ];
    }
}
