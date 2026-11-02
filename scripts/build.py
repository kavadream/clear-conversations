#!/usr/bin/env python3
"""Build the Markdown reading edition using only Python's standard library."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
book = json.loads((ROOT / 'book.json').read_text(encoding='utf-8'))
paths = [ROOT / book['preface']] + [ROOT / c['file'] for c in book['chapters']]
for path in paths:
    if not path.is_file():
        raise SystemExit(f'Missing manuscript: {path.name}')
parts = [paths[0].read_text(encoding='utf-8'),
         (ROOT / 'CONTENT-LICENSE.md').read_text(encoding='utf-8')]
parts += [p.read_text(encoding='utf-8') for p in paths[1:]]
parts += [(ROOT / 'sources/README.md').read_text(encoding='utf-8')]
(ROOT / 'dist').mkdir(exist_ok=True)
(ROOT / 'dist/reader-manuscript.md').write_text('\n\n'.join(parts).rstrip() + '\n', encoding='utf-8')
entries = []
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.name == 'manifest.json' or '__pycache__' in p.parts or '.git' in p.parts:
        continue
    data = p.read_bytes()
    entries.append({'path': p.relative_to(ROOT).as_posix(), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
manifest = {'title': book['title'], 'version': book['version'], 'status': book['status'], 'files': entries}
(ROOT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Built {len(book["chapters"])} chapters; manifest covers {len(entries)} files.')
