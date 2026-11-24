<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class ResourceCategories
{
    public static function all(): array
    {
        return [
            'compute' => ['server', 'virtual_machine', 'container'],
            'storage' => ['block', 'object', 'file'],
            'network' => ['vpc', 'subnet', 'firewall'],
            'database' => ['relational', 'document', 'cache'],
        ];
    }
}
