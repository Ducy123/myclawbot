# TRADING_RUNBOOK.md

## Objective
Operate Bybit mainnet for Ducy under strict risk control and concise reporting.

## Credentials
- Load credentials only from `/root/.openclaw/workspace/.env.bybit`
- Never print secrets back to chat
- Never commit secrets to git

## User Authorization
- Exchange: Bybit mainnet
- Live trading: authorized
- Max account usage: account may be used, but do NOT all-in a single trade
- Risk per trade: 5 USDT max loss at stop
- Max leverage: 125x ceiling; may use high leverage up to 125x when setup confidence is high, while still capping stop-loss risk near 5 USDT
- Market scope: unrestricted
- Reporting style: short, results-first, no long explanations
- Stay completely silent when there is no real trading action
- Do not send internal logs, scan updates, tool updates, planning notes, or status messages
- Notify in chat immediately only when:
  - opening a trade
  - setting/changing SL or TP
  - closing a trade
  - canceling an order that had already been placed
  - important account/security/risk events that require immediate user awareness or intervention

## Trading Constraints
- No revenge trading
- No averaging down losers unless a preplanned scale-in rule exists
- No trade if stop placement is unclear
- No trade if order sizing cannot keep max loss near 5 USDT
- Prefer liquid markets
- Avoid low-liquidity traps and extreme spread
- Keep concurrent exposure conservative relative to account size

## Scan Cadence
- Background scan every 5 minutes
- If no valid setup, do nothing
- If valid setup exists, act and report briefly

## Execution Standard
Before any order:
1. Check wallet balance and open positions
2. Avoid duplicate/conflicting exposure
3. Define entry, stop, TP
4. Size position so stop-loss risk is about 5 USDT or less
5. Use leverage only as needed for sizing efficiency
6. Place protective stop promptly after entry

## Reporting Format
Use short Vietnamese updates like:
- "Đã mở LONG BTCUSDT | entry ... | SL ... | TP ... | risk 5 USDT"
- "Đã chốt ETHUSDT | PnL ..."
- "Chưa có kèo đẹp | tiếp tục scan"

## Safety Rule
If market conditions are unclear or execution confidence is low, skip the trade.
