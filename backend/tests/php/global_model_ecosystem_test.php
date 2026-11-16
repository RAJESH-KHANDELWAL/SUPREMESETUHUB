<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/infrastructure/model/global_ecosystem/global_model_ecosystem/resources.php';
require_once dirname(__DIR__, 2) . '/infrastructure/model/global_ecosystem/global_model_ecosystem/relationships.php';
require_once dirname(__DIR__, 2) . '/infrastructure/model/global_ecosystem/global_model_ecosystem/catalog.php';
require_once dirname(__DIR__, 2) . '/infrastructure/model/global_ecosystem/global_model_ecosystem/schemas.php';
require_once dirname(__DIR__, 2) . '/infrastructure/model/global_ecosystem/global_model_ecosystem/validation.php';

use SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\GlobalProviderReference;
use SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\GlobalResourceCapacity;
use SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\GlobalResourceIdentity;
use SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\GlobalResourceLifecycle;
use SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\GlobalResourceLocation;
use SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\GlobalResourceRelationship;
use SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\ModelCatalog;
use SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\ResourceCategories;
use SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\ResourceValidator;

function expectModel(bool $condition, string $message): void
{
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

$catalog = ModelCatalog::all();
expectModel(isset($catalog['resource_identity'], $catalog['resource_category']), 'model catalog families');
expectModel(in_array('server', ResourceCategories::all()['compute'], true), 'compute resource category');
expectModel(in_array('HOSTS', \SupremeSetuHub\Infrastructure\Model\GlobalEcosystem\GlobalModelEcosystem\RelationshipTypes::all(), true), 'relationship vocabulary');

$identity = new GlobalResourceIdentity('srv-1', 'vps', 'provider-x', 'remote-1');
expectModel($identity->toArray()['resource_id'] === 'srv-1', 'resource identity serialization');
$provider = new GlobalProviderReference('provider-x', 'remote-1');
expectModel($provider->toArray()['external_id'] === 'remote-1', 'provider reference serialization');
$relationship = new GlobalResourceRelationship('srv-1', 'db-1', 'USES');
expectModel($relationship->toArray()['relationship_type'] === 'USES', 'relationship serialization');
expectModel((new GlobalResourceLifecycle('ACTIVE'))->toArray()['state'] === 'ACTIVE', 'lifecycle serialization');
expectModel((new GlobalResourceLocation(region: 'ap-south-1'))->toArray()['region'] === 'ap-south-1', 'location serialization');
expectModel((new GlobalResourceCapacity(cpu: '4 vCPU'))->toArray()['cpu'] === '4 vCPU', 'capacity serialization');

$valid = ['resource_id' => 'srv-1', 'resource_type' => 'vps', 'category' => 'compute'];
expectModel(ResourceValidator::validate($valid) === [], 'valid resource record');
expectModel(count(ResourceValidator::validate(['resource_id' => '', 'resource_type' => 'vps'])) === 2, 'invalid resource record');

echo "All Global Model Ecosystem PHP tests passed.\n";
