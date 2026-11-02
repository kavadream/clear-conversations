#!/usr/bin/env python3
"""Structural checks; these do not assess literary quality or real-world effects."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
book = json.loads((ROOT / 'book.json').read_text(encoding='utf-8'))
errors = []
chapters = book['chapters']
if [c['id'] for c in chapters] != [f'ch{i:02}' for i in range(1, 13)]:
    errors.append('Expected twelve stable chapter IDs in order.')
for c in chapters:
    p = ROOT / c['file']
    if not p.is_file():
        errors.append(f'Missing {c["file"]}')
        continue
    text = p.read_text(encoding='utf-8')
    if text.splitlines()[0] != '# ' + c['title']:
        errors.append(f'Title mismatch: {p.name}')
    if '## 读者练习' not in text:
        errors.append(f'Missing exercise: {p.name}')
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts:
        continue
    text = p.read_text(encoding='utf-8')
    for token in ('Sentinel_', 'turn426search', 'TODO', '待补正文', '/workspace/', '子agent'):
        if token in text:
            errors.append(f'Unexpected internal or placeholder token in {p.name}: {token}')
    for link in re.findall(r'\]\(([^)]+)\)', text):
        if link.startswith(('https://', 'http://', '#', 'mailto:')):
            continue
        target = (p.parent / link.split('#')[0]).resolve()
        if not target.exists():
            errors.append(f'Broken relative link in {p.name}: {link}')
manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    p = ROOT / item['path']
    if not p.is_file() or len(p.read_bytes()) != item['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest() != item['sha256']:
        errors.append(f'Manifest mismatch: {item["path"]}')
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: chapter IDs, titles, exercises, local links, placeholder scan, file hashes.')
