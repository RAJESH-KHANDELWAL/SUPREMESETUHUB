<?php

declare(strict_types=1);

namespace SupremeSetuHub\PeopleLife\AdultMedia;

final class AdultMediaClassificationContract
{
    public const TAXONOMY_VERSION = '1.0.0';

    public const ORIENTATION_LABELS = [
        'STRAIGHT',
        'GAY',
        'BISEXUAL',
        'OTHER',
        'UNSPECIFIED',
    ];

    public const PARTICIPANT_CONFIGURATIONS = [
        'DIFFERENT_GENDER',
        'SAME_GENDER',
        'MULTIPLE_GENDERS',
        'UNSPECIFIED',
    ];

    public static function validate(array $record): array
    {
        foreach (['media', 'media_bytes', 'binary_content', 'raw_media_url', 'viewer_profile', 'viewer_orientation_profile'] as $forbidden) {
            if (array_key_exists($forbidden, $record)) {
                throw new \InvalidArgumentException('MEDIA_OR_VIEWER_PROFILE_NOT_ACCEPTED');
            }
        }

        $label = strtoupper(trim((string)($record['orientation_label'] ?? 'UNSPECIFIED')));
        if (!in_array($label, self::ORIENTATION_LABELS, true)) {
            throw new \InvalidArgumentException('UNKNOWN_ORIENTATION_LABEL');
        }

        if (($record['orientation_inferred'] ?? false) === true) {
            throw new \\InvalidArgumentException('ORIENTATION_INFERENCE_PROHIBITED');
        }

        $subject = strtoupper(trim((string)($record['classification_subject_type'] ?? '')));
        $source = strtoupper(trim((string)($record['orientation_source'] ?? '')));
        if ($label !== 'UNSPECIFIED') {
            if (!in_array($subject, ['CREATOR', 'PERFORMER'], true)) {
                throw new \InvalidArgumentException('CREATOR_OR_PERFORMER_SUBJECT_REQUIRED');
            }
            if (!in_array($source, ['SELF_DECLARED', 'AUTHORIZED_RIGHTS_HOLDER'], true)) {
                throw new \InvalidArgumentException('SELF_DECLARATION_OR_AUTHORIZED_SOURCE_REQUIRED');
            }
            if (($record['orientation_inferred'] ?? false) === true) {
                throw new \InvalidArgumentException('ORIENTATION_INFERENCE_PROHIBITED');
            }
        }

        $configuration = strtoupper(trim((string)($record['participant_configuration'] ?? 'UNSPECIFIED')));
        if (!in_array($configuration, self::PARTICIPANT_CONFIGURATIONS, true)) {
            throw new \InvalidArgumentException('UNKNOWN_PARTICIPANT_CONFIGURATION');
        }

        return [
            'taxonomy_version' => self::TAXONOMY_VERSION,
            'orientation_label' => $label,
            'orientation_source' => $label === 'UNSPECIFIED' ? 'UNSPECIFIED' : $source,
            'classification_subject_type' => $label === 'UNSPECIFIED' ? 'UNSPECIFIED' : $subject,
            'participant_configuration' => $configuration,
            'orientation_inferred' => false,
            'viewer_orientation_profile_created' => false,
        ];
    }
}
