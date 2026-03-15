# Embedding Local-First v1

Purpose: semantic retrieval for Ducy + Elly using local vector storage.

## Stack
- Embedding provider: OpenAI `text-embedding-3-small`
- Vector DB: Chroma local
- Storage path: `vectorstore/chroma/`

## Sources (v1)
- `memory/*.md`
- `.learnings/*.md`
- `WORKER.md`
- `ELLY_HANDOFF.md`
- `REPO_LAYOUT.md`
- `SKILLS.md`
- `skills/*/SKILL.md`
- `profiles/elly/playbooks/*`
- `profiles/elly/*.md`

## Do not index
- `.git/`
- `.openclaw/`
- secrets/env files
- browser/session state
- images/log noise
