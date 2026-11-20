<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class ResourceValidator
{
    public static function validate(array $resource): array
    {
        $errors = [];
        foreach (GlobalResourceSchema::requiredFields() as $field) {
            if (!isset($resource[$field]) || !is_string($resource[$field]) || trim($resource[$field]) === '') {
                $errors[] = "Missing or invalid required field: {$field}";
            }
        }

        if (isset($resource['metadata']) && !is_array($resource['metadata'])) {
            $errors[] = 'metadata must be an array when provided';
        }

        if (isset($resource['category']) && is_string($resource['category'])) {
            $knownCategories = array_keys(ResourceCategories::all());
            if (!in_array($resource['category'], $knownCategories, true)) {
                $errors[] = 'Unknown resource category';
            }
        }

        return $errors;
    }
}
