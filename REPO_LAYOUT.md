# Repo Layout

This repo stores the durable, portable setup for Ducy + Elly.

## Included
- Core workspace docs for Ducy
- `profiles/elly/` — mirrored Elly workspace docs, scripts, playbooks, selected daily memory
- `skills/self-improvement/` — imported skill contents cleaned for repo storage
- `WORKER.md`, `ELLY_HANDOFF.md`, `SKILLS.md` — important operating docs

## Excluded on purpose
- Secrets and tokens
- SSH private keys
- Live browser profiles / cookies / sessions
- OpenClaw runtime state in `.openclaw/`
- Screenshots and bulky troubleshooting captures
- Machine-specific auth/config outside the repo

## Restore idea
On a fresh machine, use this repo as the source of truth for docs, scripts, playbooks, and skill content, then recreate runtime auth/session state separately.
