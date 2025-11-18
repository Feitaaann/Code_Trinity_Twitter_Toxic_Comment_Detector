# Prototype/App Screenshot Guide and Description

## Overview
The prototype consists of two components:
1. **Streamlit Web Interface** - User-friendly web application
2. **FastAPI REST API** - Backend API for programmatic access

---

## Component 1: Streamlit Web Interface

### Screenshot 1: Main Interface with Single Tweet Analysis

**What to Screenshot:**
- The entire Streamlit application window showing:
  - Main title: "🔍 Twitter Toxicity Detection"
  - Text input area with a tweet entered (use one of the sample toxic tweets)
  - "Analyze Tweet" button clicked
  - Analysis Result section showing:
    - Sentiment classification (NEGATIVE/NEUTRAL/POSITIVE) in colored box
    - Confidence Scores section with three metric containers
    - Three colored confidence bars (red for toxic, yellow for neutral, green for positive)
  - Warning message for toxic content (if applicable)

**First Line to Find:**
```
st.title("🔍 Twitter Toxicity Detection")
```

**How to Capture:**
1. Run the Streamlit app: `python -m streamlit run app/ui/app.py`
2. Enter a sample toxic tweet: "This is absolutely disgusting! People like you should be banned from social media."
3. Click "Analyze Tweet" button
4. Take a full-page screenshot showing all the analysis results

**Figure Name:**
Figure 16. Streamlit_Interface_Single_Analysis

---

### Screenshot 2: Batch Analysis Results

**What to Screenshot:**
- The Streamlit application showing:
  - Sidebar with "Batch Analysis" section
  - CSV file uploaded (or show the upload button)
  - "Batch Analysis Results" section with a table/DataFrame showing:
    - Tweet column
    - Sentiment column
    - Confidence column
  - Summary metrics section showing:
    - Total Tweets
    - Toxic Tweets (with percentage)
    - Average Confidence

**First Line to Find:**
```
st.subheader("Batch Analysis Results")
```

**How to Capture:**
1. Use the sidebar "Upload CSV" file uploader
2. Upload a CSV file with a `tweet` column containing multiple tweets
3. Take a screenshot showing the batch results table and summary metrics

**Figure Name:**
Figure 17. Streamlit_Batch_Analysis

---

### Screenshot 3: Sample Tweets Selection

**What to Screenshot:**
- The Streamlit sidebar showing:
  - "Guided Samples" section
  - Dropdown/selectbox with sample tweet options:
    - Toxic Example
    - Neutral Example
    - Positive Example
    - Sarcastic/Toxic
    - Informal Positive
  - "Load sample" button
  - Model status information showing "Model: BERT" or "Model: Baseline TF-IDF"
  - Reload Model button

**First Line to Find:**
```
st.sidebar.header("Guided Samples")
```

**How to Capture:**
1. Show the sidebar with the sample selection dropdown visible
2. Optionally show one of the sample tweets loaded in the main text area

**Figure Name:**
Figure 18. Streamlit_Sample_Selection

---

## Component 2: FastAPI REST API

### Screenshot 4: API Documentation Interface

**What to Screenshot:**
- The FastAPI automatic documentation page (Swagger UI) showing:
  - API title: "Twitter Toxicity Detection API"
  - List of endpoints:
    - GET /
    - GET /health
    - POST /analyze
  - Interactive API documentation with:
    - Request body example for /analyze endpoint
    - Try it out button
    - Response schema showing sentiment, confidence, scores, and message fields

**First Line to Find:**
Navigate to: `http://localhost:8000/docs`

**How to Capture:**
1. Start the FastAPI server: `python -m uvicorn app.backend.main:app --host 0.0.0.0 --port 8000`
2. Open browser to: `http://localhost:8000/docs`
3. Take a screenshot of the Swagger UI documentation page
4. Optionally show the /analyze endpoint expanded with request/response examples

**Figure Name:**
Figure 19. FastAPI_Documentation

---

### Screenshot 5: API Response Example

**What to Screenshot:**
- The FastAPI /docs page showing:
  - POST /analyze endpoint expanded
  - "Try it out" button clicked
  - Request body with a sample tweet entered
  - "Execute" button clicked
  - Response section showing:
    - HTTP 200 status
    - Response body with JSON containing:
      - sentiment: "negative" (or "neutral" or "positive")
      - confidence: 0.8532 (example number)
      - scores: {"negative": 0.8532, "neutral": 0.1234, "positive": 0.0234}
      - message: "Tweet sentiment is negative with confidence 85.32%."

**First Line to Find:**
The response JSON output in the Swagger UI after executing the /analyze endpoint

**How to Capture:**
1. In the /docs page, expand the POST /analyze endpoint
2. Click "Try it out"
3. Enter a sample tweet in the request body JSON
4. Click "Execute"
5. Take a screenshot showing the request and response

**Figure Name:**
Figure 20. FastAPI_Response_Example

---

## One Paragraph Description for IEEE Paper

**Title:**
Prototype Application for Twitter Toxicity Detection

**Description:**
We developed a lightweight prototype application that automatically flags potentially harmful tweets as required by the proposal Section III. The prototype consists of two complementary components: a user-friendly Streamlit web interface for interactive tweet analysis and a FastAPI REST API for programmatic access and integration with other systems. The Streamlit interface allows users to analyze individual tweets by entering text into a text area, or to process multiple tweets simultaneously through CSV batch upload. The interface displays analysis results with color-coded sentiment classifications, confidence percentages, and visual probability bars showing the model's certainty for each sentiment class. For toxic content, the system automatically displays warning messages to alert users about potentially harmful language. The FastAPI backend provides a RESTful API endpoint that accepts tweet text and returns JSON responses containing sentiment classification, confidence scores, and probability distributions for all three classes. Both components use the same underlying inference engine that automatically loads the fine-tuned BERT model if available, or falls back to the baseline TF-IDF plus Logistic Regression model for compatibility. The prototype supports real-time analysis of individual tweets and batch processing of multiple tweets, making it suitable for content moderation workflows, research applications, and system integration. The application demonstrates practical usability of the trained models and provides an intuitive interface for non-technical users to interact with the toxicity detection system.

**Figure Name:**
Figure 16. Prototype_Application (or use the individual figure names above for multiple screenshots)

---

## Screenshot Checklist

### Streamlit UI Screenshots:
- [ ] Main interface with single tweet analysis result
- [ ] Batch analysis results with summary metrics
- [ ] Sidebar with sample tweets and model status

### FastAPI API Screenshots:
- [ ] API documentation page (Swagger UI)
- [ ] API response example with request/response JSON

### Optional Screenshots:
- [ ] Model status indicator showing BERT model loaded
- [ ] Confidence score visualization with colored bars
- [ ] Warning message for toxic content

---

## Notes

- Make sure the app is running before taking screenshots
- Use sample tweets that clearly demonstrate different sentiment classes
- For batch analysis, create a small CSV file with 5-10 diverse tweets
- Capture full browser windows for clarity
- Ensure text is readable in screenshots (adjust zoom if needed)

