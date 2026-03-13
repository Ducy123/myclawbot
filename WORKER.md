# Elly Worker Commands

Worker host: `157.10.53.238:27301`

## Shortcuts

From the main VPS:

- `bin/elly-worker '<command>'` — run any command on the worker VPS
- `bin/elly-browser-status` — check browser worker service + GUI/browser processes
- `bin/elly-browser-open-x` — open X in Chrome on the worker
- `bin/elly-tunnel-hint` — print the SSH tunnel command for local noVNC access

## Typical flow

1. Check worker:
   - `bin/elly-browser-status`
2. Open X on worker:
   - `bin/elly-browser-open-x`
3. On your local computer, create the tunnel:
   - `ssh -L 6080:127.0.0.1:6080 -p 27301 root@157.10.53.238`
4. Open:
   - `http://127.0.0.1:6080/vnc.html`

## Notes

- Browser worker service on the worker host: `browser-worker.service`
- GUI stack on worker: `Xvfb + openbox + x11vnc + websockify`
- Chrome on worker uses `DISPLAY=:1`
- noVNC should be accessed through SSH tunnel, not public port 6080
