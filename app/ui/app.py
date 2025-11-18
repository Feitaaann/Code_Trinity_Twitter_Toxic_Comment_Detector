"""
Streamlit UI prototype for Twitter Toxicity Detection (per proposal Section III).

Lightweight prototype interface that automatically flags potentially harmful tweets.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd
import streamlit as st

# Get project root (Code_Trinity folder)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Change to project root directory first
import os
original_cwd = os.getcwd()
os.chdir(PROJECT_ROOT)

# Add project root to Python path (must be first)
project_root_str = str(PROJECT_ROOT)
if project_root_str not in sys.path:
    sys.path.insert(0, project_root_str)

# Ensure app package is recognized
app_dir = PROJECT_ROOT / "app"
if str(app_dir) not in sys.path:
    sys.path.insert(0, str(app_dir.parent))  # Add parent of app (PROJECT_ROOT)

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

# Initialize analyzer with cache clearing option
@st.cache_resource
def load_analyzer():
    analyzer = TweetAnalyzer()
    return analyzer

# Add a button to clear cache and reload model
if st.sidebar.button("🔄 Reload Model"):
    load_analyzer.clear()
    st.rerun()

analyzer = load_analyzer()

# Show model status
model_type = "BERT" if analyzer.transformer_model is not None else "Baseline TF-IDF"
st.sidebar.info(f"**Model:** {model_type}")

# Check if pytorch_model.bin exists
import os
pytorch_model_path = PROJECT_ROOT / "checkpoints" / "bert-base" / "best" / "pytorch_model.bin"
if analyzer.transformer_model is None:
    st.sidebar.warning("⚠️ Using baseline model. For better accuracy, re-export the full BERT model (pytorch_model.bin) from Colab.")
elif pytorch_model_path.exists():
    file_size_mb = pytorch_model_path.stat().st_size / (1024 * 1024)
    st.sidebar.success(f"✅ Full BERT model loaded ({file_size_mb:.1f} MB)")
else:
    st.sidebar.info("ℹ️ BERT model loaded (may be using safetensors or quantized weights)")

SAMPLE_TWEETS: List[Tuple[str, str]] = [
    (
        "Toxic Example",
        "This is absolutely disgusting! People like you should be banned from social media. Horrible!",
    ),
    (
        "Neutral Example",
        "Just finished my morning coffee. Weather is okay today, nothing special.",
    ),
    (
        "Positive Example",
        "So grateful for all the support today! Amazing community, thank you everyone! 🙏",
    ),
    (
        "Sarcastic/Toxic",
        "Oh wonderful, another day of dealing with this nonsense. Just perfect...",
    ),
    (
        "Informal Positive",
        "This made my day! So happy right now! Best news ever! 🔥",
    ),
]

SENTIMENT_COLORS = {
    "negative": "#F87171",  # Red
    "neutral": "#FBBF24",   # Yellow
    "positive": "#34D399",  # Green
}

CUSTOM_CSS = """
<style>
.stApp {
    background: linear-gradient(180deg, #0b1220 0%, #111827 100%);
    color: #E5E7EB;
    font-family: "Inter", sans-serif;
}
.metric-container {
    background: rgba(148, 163, 184, 0.1);
    padding: 20px;
    border-radius: 12px;
    border: 1px solid rgba(148, 163, 184, 0.2);
}
.confidence-bar {
    background: rgba(148, 163, 184, 0.18);
    border-radius: 999px;
    overflow: hidden;
    height: 12px;
    margin-top: 8px;
}
.confidence-bar__fill {
    height: 100%;
    border-radius: inherit;
    transition: width 0.3s ease;
}
.tweet-box {
    padding: 20px;
    border-radius: 12px;
    background: #1e293b;
    border: 1px solid rgba(148, 163, 184, 0.2);
    margin: 10px 0;
}
</style>
"""


def render_confidence_bar(score: float, color: str) -> None:
    """Render a confidence bar"""
    st.markdown(
        f"""
        <div class="confidence-bar">
            <div class="confidence-bar__fill" style="width: {score*100}%; background: {color};"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="Twitter Toxicity Detector",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    st.title("🔍 Twitter Toxicity Detection")
    st.caption("Lightweight prototype for automatically flagging potentially harmful tweets (per proposal Section III)")

    # Sidebar
    st.sidebar.header("Guided Samples")
    sample_labels = [label for label, _ in SAMPLE_TWEETS]
    selected = st.sidebar.selectbox("Choose a sample", sample_labels)
    if st.sidebar.button("Load sample"):
        st.session_state.tweet_text = dict(SAMPLE_TWEETS)[selected]

    st.sidebar.divider()
    st.sidebar.subheader("Batch Analysis")
    uploaded = st.sidebar.file_uploader("Upload CSV with a `tweet` column", type=["csv"])
    
    # Main interface
    if uploaded is not None:
        try:
            # Read CSV with proper handling of quoted fields and commas
            # Use engine='python' for better compatibility with quoted fields containing commas
            import io
            # Reset file pointer to beginning
            uploaded.seek(0)
            # Try with on_bad_lines for newer pandas
            try:
                df = pd.read_csv(uploaded, quotechar='"', skipinitialspace=True, engine='python', on_bad_lines='skip')
            except TypeError:
                # Fallback for older pandas versions
                df = pd.read_csv(uploaded, quotechar='"', skipinitialspace=True, engine='python')
        except Exception as e:
            st.error(f"Error reading CSV file: {str(e)}. Please ensure the CSV is properly formatted with a 'tweet' column.")
            return
        
        if "tweet" not in df.columns:
            st.error("CSV must have a 'tweet' column")
            return
        
        st.subheader("Batch Analysis Results")
        results = []
        for idx, row in df.iterrows():
            try:
                result = analyzer.analyze(row["tweet"])
                results.append({
                    "tweet": row["tweet"],
                    "sentiment": result.sentiment_label,
                    "confidence": result.confidence,
                })
            except Exception as e:
                st.warning(f"Error processing row {idx}: {e}")
        
        results_df = pd.DataFrame(results)
        st.dataframe(results_df, use_container_width=True)
        
        # Summary
        st.subheader("Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Tweets", len(results_df))
        with col2:
            toxic_count = len(results_df[results_df["sentiment"] == "negative"])
            st.metric("Toxic Tweets", toxic_count, delta=f"{toxic_count/len(results_df)*100:.1f}%")
        with col3:
            st.metric("Avg Confidence", f"{results_df['confidence'].mean():.2%}")
    else:
        # Single tweet analysis
        tweet_text = st.text_area(
            "Enter a tweet to analyze:",
            value=st.session_state.get("tweet_text", ""),
            height=100,
            placeholder="Type or paste a tweet here..."
        )
        
        if st.button("Analyze Tweet", type="primary"):
            if not tweet_text.strip():
                st.warning("Please enter a tweet to analyze.")
            else:
                try:
                    result = analyzer.analyze(tweet_text)
                    
                    # Debug info (can be removed later)
                    with st.expander("🔍 Debug Info", expanded=False):
                        st.write(f"Model: {'BERT' if analyzer.transformer_model else 'Baseline'}")
                        st.write(f"Raw scores: {result.sentiment_scores}")
                        st.write(f"Predicted label: {result.sentiment_label}")
                    
                    # Display result
                    st.markdown("---")
                    st.subheader("Analysis Result")
                    
                    # Sentiment card
                    color = SENTIMENT_COLORS.get(result.sentiment_label, "#9CA3AF")
                    st.markdown(
                        f"""
                        <div class="tweet-box">
                            <h3 style="color: {color}; margin-bottom: 10px;">
                                Sentiment: {result.sentiment_label.upper()}
                            </h3>
                            <p style="font-size: 1.1em; margin-bottom: 15px;">{result.to_dict()['sentiment']['message']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    
                    # Confidence scores
                    st.subheader("Confidence Scores")
                    cols = st.columns(3)
                    for idx, (label, score) in enumerate(result.sentiment_scores.items()):
                        with cols[idx]:
                            label_color = SENTIMENT_COLORS.get(label, "#9CA3AF")
                            st.markdown(f"<div class='metric-container'>", unsafe_allow_html=True)
                            st.metric(label.capitalize(), f"{score:.2%}")
                            render_confidence_bar(score, label_color)
                            st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Warning for toxic content
                    if result.sentiment_label == "negative":
                        st.warning("⚠️ This tweet has been flagged as potentially toxic/negative.")
                    
                except Exception as e:
                    st.error(f"Error analyzing tweet: {e}")


if __name__ == "__main__":
    main()

