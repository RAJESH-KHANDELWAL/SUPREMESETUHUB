<?php
declare(strict_types=1);

namespace GithubSupreme;

use RuntimeException;

final class Registry
{
    private function __construct(
        private array $hosts,
        private array $domains
    ) {}

    public static function fromDirectory(string $root): self
    {
        $configDir = $root . '/config';
        $hostsFile = $configDir . '/hosts.json';
        $domainsFile = $configDir . '/domains.json';

        if (!is_file($hostsFile) || !is_file($domainsFile)) {
            throw new RuntimeException('Registry configuration files are missing.');
        }

        $hosts = self::readJson($hostsFile);
        $domains = self::readJson($domainsFile);

        if (!isset($hosts['hosts']) || !is_array($hosts['hosts'])) {
            throw new RuntimeException('Invalid hosts configuration.');
        }
        if (!isset($domains['domains']) || !is_array($domains['domains'])) {
            throw new RuntimeException('Invalid domains configuration.');
        }

        return new self($hosts['hosts'], $domains['domains']);
    }

    private static function readJson(string $file): array
    {
        $contents = file_get_contents($file);
        if ($contents === false) {
            throw new RuntimeException('Unable to read configuration.');
        }

        $data = json_decode($contents, true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($data)) {
            throw new RuntimeException('Configuration must be a JSON object.');
        }
        return $data;
    }

    public function hostSlotCount(): int
    {
        return count($this->hosts);
    }

    public function configuredHostCount(): int
    {
        return count(array_filter($this->hosts, static function (array $host): bool {
            return !empty($host['hostname']) && !empty($host['username']);
        }));
    }

    public function domains(): array
    {
        return array_values(array_map(static function (array $domain): array {
            return [
                'name' => (string) ($domain['name'] ?? ''),
                'url' => (string) ($domain['url'] ?? ''),
                'deployment_path' => (string) ($domain['deployment_path'] ?? ''),
            ];
        }, $this->domains));
    }
}
