# Zalo API Notes

## Core endpoints
- `getMe`
- `getWebhookInfo`
- `setWebhook`
- `sendMessage`

## Important observations
- Bot token authenticates API calls
- Webhook can require `secret_token`
- Public HTTPS endpoint is preferred for webhook delivery
- Debug order: token -> webhook info -> inbound POST -> agent reply path -> sendMessage
