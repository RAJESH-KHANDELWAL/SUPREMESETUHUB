<?php
/** Structural health manager for the Global Infrastructure Ecosystem. */
final class BackendGlobalInfrastructureEcosystemManager {
    public const NAME = 'BACKEND GLOBAL INFRASTRUCTURE ECOSYSTEM';
    public const VERSION = '1.3.0';
    private const DOMAINS = ['backup','billing','cdn','containers','database','dns','domains','email','firewall','ftp','hosting','ipam','load_balancer','model','monitoring','network','object_storage','security','server','ssl','storage'];
    private const DOMAIN_REQUIRED_FILES = [
        'database' => ['__init__.py','controller.py','model.py','service.py','healthcheck.py'],
        'ftp' => ['__init__.py','controller.py','model.py','service.py','healthcheck.py','profiles.py'],
        'model' => ['__init__.py','README.md','resource.py'],
    ];
    private const DEFAULT_DOMAIN_REQUIRED_FILES = ['__init__.py','controller.py','model.py','service.py'];

    public function health(): array {
        $root = __DIR__;
        $backendRoot = dirname(dirname(dirname($root)));
        $required = ['README.md','__init__.py','catalog.py','capabilities.py','governance.py','integrations.py','models.py','providers.py','registry.py','schemas.py','service.py','services.py','structure.py','manager.py','manager.php'];
        $checks = []; $domainChecks = []; $domainFileChecks = [];
        foreach ($required as $name) { $checks['root_file_' . $name] = is_file($root . '/' . $name); }
        foreach (['__init__.py','controller.py','repository.py','service.py','hostinger_catalog.py'] as $name) {
            $checks['canonical_module_' . $name] = is_file($root . '/modules/' . $name);
        }
        $checks['core_integration_adapter'] = is_file($root . '/integrations/core/__init__.py');
        $checks['global_core_integration_adapter'] = is_file($root . '/integrations/global_core_ecosystem/__init__.py');

        foreach (self::DOMAINS as $domain) {
            $domainRoot = $root . '/' . $domain;
            $domainChecks[$domain] = is_dir($domainRoot) && is_file($domainRoot . '/__init__.py');
            $requiredDomainFiles = self::DOMAIN_REQUIRED_FILES[$domain] ?? self::DEFAULT_DOMAIN_REQUIRED_FILES;
            $fileChecks = [];
            foreach ($requiredDomainFiles as $filename) {
                $fileChecks[$filename] = is_file($domainRoot . '/' . $filename);
            }
            $domainFileChecks[$domain] = $fileChecks;
            $checks['domain_' . $domain] = $domainChecks[$domain];
            $checks['domain_files_' . $domain] = !in_array(false, $fileChecks, true);

            $ecosystemRoot = $domainRoot . '/global_ecosystem';
            $checks['domain_global_ecosystem_' . $domain] = is_dir($ecosystemRoot) && is_file($ecosystemRoot . '/__init__.py');
            $packageRoot = $ecosystemRoot . '/global_' . $domain . '_ecosystem';
            $packageFiles = in_array($domain, ['model','server'], true) ? ['__init__.py'] : ['__init__.py','manager.py','manager.php'];
            $packageHealthy = is_dir($packageRoot);
            foreach ($packageFiles as $filename) {
                if (!is_file($packageRoot . '/' . $filename)) { $packageHealthy = false; }
            }
            $checks['global_package_' . $domain] = $packageHealthy;
        }

        foreach (['backup','rebackup','recovery','rerecovery','database','redatabase','history','rehistory','storage','restorage','sync','resync'] as $domain) {
            $package = $root . '/' . $domain . '/global_ecosystem/global_' . $domain . '_ecosystem';
            $checks['ecosystem_domain_' . $domain] = is_dir($package) && is_file($package . '/README.md');
        }
        $checks['backend_global_hostinger_api'] = is_file($backendRoot . '/global_ecosystem/global_hosting_ecosystem/hostinger_api.py');
        $checks['backend_global_nsfwinfra'] = is_file($backendRoot . '/global_ecosystem/nsfwinfra_ecosystem/nsfwinfra.py');
        $healthy = !in_array(false, $checks, true);
        $present = 0; $globalPackagesPresent = 0;
        foreach (self::DOMAINS as $domain) {
            if ($domainChecks[$domain] && $checks['domain_files_' . $domain]) { $present++; }
            if ($checks['global_package_' . $domain]) { $globalPackagesPresent++; }
        }
        return [
            'name'=>self::NAME,'version'=>self::VERSION,'status'=>$healthy?'READY':'INCOMPLETE',
            'expected_domain_count'=>count(self::DOMAINS),'present_domain_count'=>$present,
            'expected_global_package_count'=>count(self::DOMAINS),'present_global_package_count'=>$globalPackagesPresent,
            'checks'=>$checks,'domain_checks'=>$domainChecks,'domain_file_checks'=>$domainFileChecks,
            'healthy'=>$healthy,'provider_operations_enabled'=>false
        ];
    }
}
