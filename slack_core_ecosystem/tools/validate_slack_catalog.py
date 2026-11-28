import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'ecosystem_manifest.json').read_text(encoding='utf-8'))
assert data['ecosystem_id']=='SLACK-CORE-ECOSYSTEM' and data['product_count']==len(data['products'])==14
ids=[p['product_id'] for p in data['products']];assert len(ids)==len(set(ids))
for p in data['products']:
 d=root/p['package_name'];assert (d/'__init__.py').is_file() and (d/'manager.py').is_file()
print('Slack Core catalog validation: PASS')
