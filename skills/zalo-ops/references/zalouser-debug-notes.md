# Zalouser Debug Notes

## Common failure modes
- duplicate plugin id detected
- plugin install-stage directories left behind
- runtime dependency missing (for example `zca-js`)
- OpenClaw loading builtin/global plugin instead of patched user extension

## Practical rule
If `zalouser` becomes a time sink, stop and prefer official Zalo Bot API + bridge.
