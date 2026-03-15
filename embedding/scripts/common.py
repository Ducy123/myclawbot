from __future__ import annotations
import json, os, glob, fnmatch
from pathlib import Path
from typing import List, Dict, Any
import yaml

ROOT = Path('/root/.openclaw/workspace')


def load_settings() -> Dict[str, Any]:
    return json.loads((ROOT / 'embedding/config/settings.json').read_text())


def load_sources() -> Dict[str, Any]:
    return yaml.safe_load((ROOT / 'embedding/config/sources.yaml').read_text())


def should_exclude(path: str, patterns: List[str]) -> bool:
    rel = path.replace(str(ROOT) + '/', '')
    return any(fnmatch.fnmatch(rel, p) or fnmatch.fnmatch(path, p) for p in patterns)


def collect_files() -> List[Path]:
    cfg = load_sources()
    files = []
    for pat in cfg.get('include', []):
        files.extend(ROOT.glob(pat))
    dedup = []
    seen = set()
    for p in files:
        if not p.is_file():
            continue
        s = str(p)
        if s in seen:
            continue
        if should_exclude(s, cfg.get('exclude', [])):
            continue
        seen.add(s)
        dedup.append(p)
    return sorted(dedup)


def chunk_text(text: str, target_chars: int, overlap_chars: int, min_chars: int):
    text = text.strip()
    if len(text) <= target_chars:
        return [text] if len(text) >= min_chars else []
    chunks = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + target_chars, n)
        if end < n:
            split = text.rfind('\n\n', start, end)
            if split == -1:
                split = text.rfind('\n', start, end)
            if split != -1 and split > start + min_chars:
                end = split
        chunk = text[start:end].strip()
        if len(chunk) >= min_chars:
            chunks.append(chunk)
        if end >= n:
            break
        start = max(end - overlap_chars, start + 1)
    return chunks


def collection_for_path(path: Path, settings: Dict[str, Any]) -> str:
    s = str(path)
    c = settings['collections']
    if '/memory/' in s or '/.learnings/' in s:
        return c['memory']
    if '/skills/' in s and s.endswith('SKILL.md'):
        return c['skills']
    if '/profiles/elly/' in s:
        return c['elly']
    return c['docs']
