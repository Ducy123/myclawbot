# Errors Log

Command failures, exceptions, and unexpected behaviors.

---
## [ERR-20260314-001] bybit-api-order-permission

**Logged**: 2026-03-14T13:14:56+00:00
**Priority**: high
**Status**: pending
**Area**: config

### Summary
Bybit API key can read account data but order-placement endpoints return permission denied, blocking live trade execution.

### Error
```
retCode 10005: Permission denied, please check your API key permissions.
```

### Context
- Operation attempted: `/v5/position/set-leverage` and `/v5/order/create`
- Read-only account endpoints succeeded (`wallet-balance`, `position/list`)
- Environment: Bybit mainnet credentials loaded from `.env.bybit`
- Impact: scan can validate setups but cannot execute live orders

### Suggested Fix
Enable trading permissions for the configured Bybit API key (and verify derivatives trading scope), then re-run the live scanner.

### Metadata
- Reproducible: yes
- Related Files: .env.bybit, TRADING_RUNBOOK.md

---
