# Prototype Application Description for IEEE Paper

## Title
Prototype Application for Twitter Toxicity Detection

## One Paragraph Description

We developed a lightweight prototype application that automatically flags potentially harmful tweets as required by the proposal Section III. The prototype consists of two complementary components: a user-friendly Streamlit web interface for interactive tweet analysis and a FastAPI REST API for programmatic access and integration with other systems. The Streamlit interface allows users to analyze individual tweets by entering text into a text area, or to process multiple tweets simultaneously through CSV batch upload. The interface displays analysis results with color-coded sentiment classifications, confidence percentages, and visual probability bars showing the model's certainty for each sentiment class. For toxic content, the system automatically displays warning messages to alert users about potentially harmful language. The FastAPI backend provides a RESTful API endpoint that accepts tweet text and returns JSON responses containing sentiment classification, confidence scores, and probability distributions for all three classes. Both components use the same underlying inference engine that automatically loads the fine-tuned BERT model if available, or falls back to the baseline TF-IDF plus Logistic Regression model for compatibility. The prototype supports real-time analysis of individual tweets and batch processing of multiple tweets, making it suitable for content moderation workflows, research applications, and system integration. The application demonstrates practical usability of the trained models and provides an intuitive interface for non-technical users to interact with the toxicity detection system.

**Figure Name:**
Figure 16. Prototype_Application

---

## Quick Screenshot Guide

### Primary Screenshot: Main Streamlit Interface
**What to capture:**
1. The full Streamlit web interface
2. A tweet entered in the text area (use toxic sample: "This is absolutely disgusting! People like you should be banned from social media.")
3. Analysis result showing:
   - Sentiment classification (NEGATIVE in red box)
   - Three confidence score bars (red, yellow, green)
   - Confidence percentages displayed
   - Warning message for toxic content

**How to capture:**
1. Run: `python -m streamlit run app/ui/app.py`
2. Enter a toxic tweet in the text area
3. Click "Analyze Tweet"
4. Take full-page screenshot

**Code location:**
File: `app/ui/app.py`
Line: `st.title("🔍 Twitter Toxicity Detection")`

---

### Secondary Screenshot: API Documentation (Optional)
**What to capture:**
FastAPI Swagger UI showing:
- API documentation page at `http://localhost:8000/docs`
- POST /analyze endpoint
- Sample request and response JSON

**How to capture:**
1. Run: `python -m uvicorn app.backend.main:app --host 0.0.0.0 --port 8000`
2. Open: `http://localhost:8000/docs`
3. Take screenshot of the documentation page

**Code location:**
File: `app/backend/main.py`
Navigate to: `http://localhost:8000/docs`

