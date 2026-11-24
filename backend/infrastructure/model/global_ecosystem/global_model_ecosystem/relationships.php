<?php
declare(strict_types=1);

namespace SupremeSetuHub\\Infrastructure\\Model\\GlobalEcosystem\\GlobalModelEcosystem;

final class RelationshipTypes
{
    public static function all(): array
    {
        return ['HOSTS', 'USES', 'CONNECTS_TO', 'DEPENDS_ON', 'MANAGES', 'BACKS_UP'];
    }
}

final class GlobalResourceRelationship
{
    public function __construct(
        public string $sourceResourceId,
        public string $targetResourceId,
        public string $relationshipType
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
