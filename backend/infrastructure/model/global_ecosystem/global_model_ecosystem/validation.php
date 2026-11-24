<?php
declare(strict_types=1);

namespace SupremeSetuHub\\Infrastructure\\Model\\GlobalEcosystem\\GlobalModelEcosystem;

final class ResourceValidator
{
    public static function validate(array $resource): array
    {
        $errors = [];
        foreach (['resource_id', 'resource_type', 'category'] as $field) {
            if (!isset($resource[$field]) || !is_string($resource[$field]) || trim($resource[$field]) === '') {
                $errors[] = $field . ' is required.';
            }
        }

        $categories = ResourceCategories::all();
        $knownCategories = [];
        foreach ($categories as $items) {
            $knownCategories = array_merge($knownCategories, $items);
        }
        if (isset($resource['category']) && is_string($resource['category']) &&
            trim($resource['category']) !== '' && !in_array($resource['category'], $knownCategories, true)) {
            $errors[] = 'category is not recognized.';
        }

        return $errors;
    }
}
