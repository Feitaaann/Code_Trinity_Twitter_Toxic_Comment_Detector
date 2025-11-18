# Streamlit Prototype

Lightweight prototype interface for Twitter toxicity detection (per proposal Section III).

## Quick start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
cd Code_Trinity
streamlit run app/ui/app.py
```

The app will open in your browser at `http://localhost:8501`.

## Features

- Single tweet analysis with real-time toxicity classification
- Confidence scores display
- Visual indicators (red/yellow/green for toxic/neutral/positive)
- Sample tweets for testing
- Batch upload (CSV file processing)
- Toxicity warnings for negative predictions

