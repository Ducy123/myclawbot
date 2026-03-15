#!/usr/bin/env bash
set -euo pipefail
cd /root/.openclaw/workspace
source embedding/.venv/bin/activate
if [ -f embedding/.env ]; then
  set -a
  source embedding/.env
  set +a
fi
python embedding/scripts/ingest.py
