# Next Step to Go Live

The local-first embedding stack is fully scaffolded and dependencies are installed.

## What is already done
- source selection configured
- chunking logic implemented
- Chroma local storage path prepared
- ingest/query scripts implemented
- Python venv + dependencies installed
- files-to-index scan verified

## What is missing
Only one thing: `OPENAI_API_KEY`.

## To finish
1. Copy `embedding/.env.example` to `embedding/.env`
2. Put a valid OpenAI API key in `embedding/.env`
3. Run:
   - `embedding/scripts/run-ingest.sh`
4. Test:
   - `embedding/scripts/run-query.sh "your query here"`

## Current indexed source plan
25 files are selected in v1.
