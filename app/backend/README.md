# Twitter Toxicity Detection API

FastAPI backend for toxic tweet detection (per proposal: API demonstration).

## Quick start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the API
cd Code_Trinity
python -m app.backend.main

# Or with uvicorn directly
uvicorn app.backend.main:app --host 0.0.0.0 --port 8000
```

## Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `POST /analyze` - Analyze tweet toxicity
  - Request body: `{"tweet": "your tweet text here"}`
  - Response: `{"sentiment": "negative/neutral/positive", "confidence": 0.95, "scores": {...}}`

## Example

```bash
curl -X POST "http://localhost:8000/analyze" \
     -H "Content-Type: application/json" \
     -d '{"tweet": "This is a toxic comment!"}'
```

