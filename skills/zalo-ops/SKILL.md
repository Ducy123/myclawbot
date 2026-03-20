---
name: zalo-ops
description: "Set up, debug, and operate Zalo integrations for OpenClaw. Use when working with Zalo Bot API, webhooks, tokens, webhook verification, bridge services, message send/receive flows, or when troubleshooting `zalo` / `zalouser` channel issues in OpenClaw."
---

# Zalo Ops

Use this skill when an agent needs to work with Zalo.

## What this skill covers
- Zalo Bot API setup
- Webhook setup and validation
- Token verification
- Message send/receive debugging
- OpenClaw `zalo` / `zalouser` troubleshooting
- Bridge-based fallback architecture when plugin/runtime paths fail

## Decision tree

### 1. Need official Zalo bot?
Use **Zalo Bot API**.
- Best for stable integrations
- Uses bot token
- Requires webhook or polling-like bridge logic

### 2. Need Zalo personal account?
Use **`zalouser`** only if runtime is healthy.
- Experimental / unofficial
- Can break on runtime/plugin dependency issues
- If plugin fails, prefer fallback bridge or stop and report clearly

## Preferred order of attack
1. Verify token / auth
2. Verify webhook endpoint reachability
3. Verify inbound event reaches server
4. Verify agent execution path
5. Verify outbound reply API call
6. Only then debug UI/plugin issues

## Zalo Bot API quick checks
- `getMe`
- `getWebhookInfo`
- `setWebhook`
- `sendMessage`

## Best practices
- Prefer HTTPS webhook URLs
- Use a secret token for webhook verification
- Log inbound payloads and outbound API responses
- Keep bot token out of repo
- Separate bridge code from agent workspace logic

## When plugin/runtime fails
If `zalo` or `zalouser` plugin fails due to duplicate plugin ids, missing runtime deps, or bad loader state:
- stop retry loops
- audit config vs runtime state
- clean temp install-stage dirs
- decide whether to patch plugin or fall back to direct Zalo API bridge

## Recommended local files
- `references/zalo-api-notes.md`
- `references/zalouser-debug-notes.md`
- `scripts/` for bridge helpers if needed
