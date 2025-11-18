"""
FastAPI backend for Twitter toxicity detection (per proposal: API demonstration).

Provides REST API endpoint for toxic tweet detection.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Change to project root directory first
import os
os.chdir(PROJECT_ROOT)

# Add project root to Python path
project_root_str = str(PROJECT_ROOT)
if project_root_str not in sys.path:
    sys.path.insert(0, project_root_str)

# Now try the import
try:
    from app.inference.predictor import TweetAnalyzer
except ImportError as e:
    # Fallback: direct import
    import importlib.util
    predictor_path = PROJECT_ROOT / "app" / "inference" / "predictor.py"
    spec = importlib.util.spec_from_file_location("predictor", predictor_path)
    predictor_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(predictor_module)
    TweetAnalyzer = predictor_module.TweetAnalyzer

app = FastAPI(
    title="Twitter Toxicity Detection API",
    description="API for detecting toxic comments on Twitter using BERT",
    version="1.0.0"
)

# Initialize analyzer
analyzer = TweetAnalyzer()


class AnalyzeRequest(BaseModel):
    tweet: str


class AnalyzeResponse(BaseModel):
    sentiment: str
    confidence: float
    scores: Dict[str, float]
    message: str


@app.get("/")
def root():
    return {
        "message": "Twitter Toxicity Detection API",
        "version": "1.0.0",
        "endpoints": {
            "/health": "Health check",
            "/analyze": "POST - Analyze tweet toxicity"
        }
    }


@app.get("/health")
def healthcheck() -> Dict:
    return {"status": "ok", "model_loaded": analyzer.transformer_model is not None}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    """
    Analyze a tweet for toxicity.
    
    Returns sentiment classification (negative/toxic, neutral, positive)
    with confidence scores.
    """
    try:
        result = analyzer.analyze(request.tweet)
        return AnalyzeResponse(
            sentiment=result.sentiment_label,
            confidence=result.confidence,
            scores=result.sentiment_scores,
            message=result.to_dict()["sentiment"]["message"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

