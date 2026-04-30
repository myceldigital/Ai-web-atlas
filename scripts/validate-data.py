#!/usr/bin/env python3
import json
from pathlib import Path

path = Path('data/companies.json')
if not path.exists():
    raise SystemExit('Missing data/companies.json')

data = json.loads(path.read_text(encoding='utf-8'))
companies = data.get('companies', [])
if not isinstance(companies, list) or not companies:
    raise SystemExit('companies must be a non-empty list')

required = {'name', 'category', 'map_version', 'relationship_type', 'confidence', 'evidence_urls', 'notes'}
allowed_confidence = {'low', 'medium', 'high'}
allowed_relationships = {'customer', 'probable_customer', 'peer', 'supplier', 'substrate', 'category_marker', 'uncertain'}

seen = set()
for i, company in enumerate(companies):
    missing = required - company.keys()
    if missing:
        raise SystemExit(f'Company index {i} missing fields: {sorted(missing)}')
    name = company['name']
    if name in seen:
        raise SystemExit(f'Duplicate company: {name}')
    seen.add(name)
    if company['confidence'] not in allowed_confidence:
        raise SystemExit(f'Invalid confidence for {name}: {company["confidence"]}')
    if company['relationship_type'] not in allowed_relationships:
        raise SystemExit(f'Invalid relationship_type for {name}: {company["relationship_type"]}')
    if not isinstance(company['evidence_urls'], list):
        raise SystemExit(f'evidence_urls must be a list for {name}')

print(f'OK: {len(companies)} companies validated')
