# OPERATIONS.md

## Browser Worker
- Host: `157.10.53.238:27301`
- Access: SSH key at `/root/.ssh/elly_worker`
- Browser worker service: `browser-worker.service`
- X session lives on the remote worker's Chrome profile

## Commands
- `bin/worker-status` — check worker state
- `bin/open-x` — open X on the worker
- `bin/worker 'export DISPLAY=:1; pgrep -a chrome'` — inspect Chrome

## Notes
- Use the remote browser worker for X operations
- Keep Chrome/session intact unless recovery is needed
- Prefer using existing logged-in session over fresh login attempts
