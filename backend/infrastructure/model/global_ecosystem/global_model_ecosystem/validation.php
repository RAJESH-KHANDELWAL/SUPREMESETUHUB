<?php
declare(strict_types=1);

namespace SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem;

final class ResourceValidator
{
    private const REQUIRED_FIELDS = ['resource_id', 'resource_type', 'category'];

    public static function validate(array $record): array
    {
        $errors = [];
        foreach (self::REQUIRED_FIELDS as $field) {
            if (!isset($record[$field]) || !is_string($record[$field]) || trim($record[$field]) === '') {
                $errors[] = $field . ' must be a non-empty string';
            }
        }

        if (isset($record['metadata']) && !is_array($record['metadata'])) {
            $errors[] = 'metadata must be an array when provided';
        }

        return $errors;
    }
}
