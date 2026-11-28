<?php
/** Backend/frontend global infrastructure ecosystem contract checker. */
final class BackendGlobalInfrastructureEcosystemConnector
{
    private const DOMAINS = [
        'backup', 'billing', 'cdn', 'containers', 'database', 'dns', 'domains',
        'email', 'firewall', 'ftp', 'hosting', 'ipam', 'load_balancer', 'model',
        'monitoring', 'network', 'object_storage', 'security', 'server', 'ssl', 'storage'
    ];

    private string $backendRoot;
    private string $frontendRoot;
    private string $backendEntry;

    public function __construct()
    {
        $this->backendRoot = __DIR__;
        $repositoryRoot = dirname(__DIR__, 4);
        $this->frontendRoot = $repositoryRoot . '/frontend/infrastructure/global_ecosystem/global_infrastructure_ecosystem';
        $this->backendEntry = $repositoryRoot . '/backend/infrastructure/global_ecosystem';
    }

    public function connect(): array
    {
        $backendDomains = [];
        foreach (self::DOMAINS as $domain) {
            $backendDomains[$domain] = is_dir($this->backendRoot . '/' . $domain);
        }

        $backendFiles = [];
        foreach ([
            '__init__.py',
            'manager.py',
            'manager.php',
            'structure.py',
            'backend_global_infrastructure_ecosystem_frontend_global_infrastructure_ecosystem_connect.py',
            'backend_global_infrastructure_ecosystem_frontend_global_infrastructure_ecosystem_connect.php'
        ] as $file) {
            $backendFiles[$file] = is_file($this->backendRoot . '/' . $file);
        }

        $frontendFiles = [];
        foreach ([
            '__init__.py',
            'manager.py',
            'manager.php',
            'frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.py',
            'frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.php'
        ] as $file) {
            $frontendFiles[$file] = is_file($this->frontendRoot . '/' . $file);
        }

        $frontendDomainFiles = array_filter(
            self::DOMAINS,
            fn($name) => is_file($this->frontendRoot . '/' . $name . '.py')
        );
        $frontendDomainFolders = array_filter(
            self::DOMAINS,
            fn($name) => is_dir($this->frontendRoot . '/' . $name)
        );
        $backendEntryChecks = [
            'global_ecosystem_manager.py' => is_file($this->backendEntry . '/manager.py'),
            'global_ecosystem_manager.php' => is_file($this->backendEntry . '/manager.php')
        ];

        $backendHealthy = !in_array(false, $backendDomains, true)
            && !in_array(false, $backendFiles, true);
        $frontendHealthy = !in_array(false, $frontendFiles, true)
            && count($frontendDomainFiles) === 0
            && count($frontendDomainFolders) === 0;
        $entryHealthy = !in_array(false, $backendEntryChecks, true);

        return [
            'name' => 'BACKEND-FRONTEND GLOBAL INFRASTRUCTURE CONNECTOR',
            'backend' => [
                'healthy' => $backendHealthy,
                'domain_checks' => $backendDomains,
                'file_checks' => $backendFiles,
                'expected_domain_count' => count(self::DOMAINS),
                'present_domain_count' => count(array_filter($backendDomains))
            ],
            'frontend' => [
                'healthy' => $frontendHealthy,
                'file_checks' => $frontendFiles,
                'domain_file_count' => count($frontendDomainFiles),
                'domain_folder_count' => count($frontendDomainFolders)
            ],
            'backend_entry' => ['healthy' => $entryHealthy, 'checks' => $backendEntryChecks],
            'connected' => $backendHealthy && $frontendHealthy && $entryHealthy,
            'connection_type' => 'repository structure and contract validation; not a runtime bridge'
        ];
    }
}
