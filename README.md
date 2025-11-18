# Twitter Toxicity Detection Project

Toxic Comment Detection on Twitter Using BERT - Implementation based on proposal methodology.

## Project Overview

This project implements a complete toxic comment detection system for Twitter posts using:
- **Baseline Model**: TF-IDF + Logistic Regression (per proposal Section V.C)
- **Main Model**: BERT-base-uncased (per proposal Section V.C)
- **Dataset**: mteb/tweet_sentiment_extraction from Hugging Face
- **Split Ratio**: 70/15/15 (training/validation/testing) per proposal Section V.B
- **Target Performance**: Macro F1-score > 0.85 (per proposal Section III)

## Project Structure

```
Code_Trinity/
├── Code_Trinity_Final_Project.ipynb  # Main notebook (complete workflow)
├── Code_Trinity_FinalProject.txt     # Proposal paper
├── export_dataset.py                  # Dataset export script
├── TwitterToxicity.csv                # Exported dataset (run export_dataset.py first)
├── requirements.txt                  # Python dependencies
├── train_ids.csv, val_ids.csv, test_ids.csv  # Reproducible split IDs
├── runs_log.csv                      # Experiment logs
├── checkpoints/                      # Saved model checkpoints
│   └── bert-base/
│       └── best/
├── models/                           # Saved baseline models
├── tuning/                           # Hyperparameter tuning results
├── exports/                          # Evaluation results, predictions, metrics
└── app/                              # Prototype application
    ├── inference/                    # Core inference logic
    ├── backend/                      # FastAPI REST API
    └── ui/                           # Streamlit web interface
```

## Quick Start

### 1. Export Dataset

First, export the dataset from Hugging Face:

```bash
cd Code_Trinity
python export_dataset.py
```

This will create `TwitterToxicity.csv` with labels mapped to proposal format (-1, 0, 1).

### 2. Run Notebook

Open `Code_Trinity_Final_Project.ipynb` in Jupyter/Colab and run all cells. The notebook includes:

- Data preprocessing (per proposal Section V.B)
- Baseline TF-IDF + Logistic Regression model
- BERT-base-uncased fine-tuning
- Automated hyperparameter tuning (Optuna)
- Comprehensive evaluation with ROC-AUC/PR-AUC curves
- Model comparison and visualization

### 3. Run Prototype Application

**Streamlit UI:**
```bash
streamlit run app/ui/app.py
```

**Backend API:**
```bash
python -m app.backend.main
# Or: uvicorn app.backend.main:app --host 0.0.0.0 --port 8000
```

## Key Features

- **Reproducible Splits**: 70/15/15 stratified split with saved IDs
- **Automated Hyperparameter Tuning**: Grid and random search with Optuna
- **Comprehensive Evaluation**: Accuracy, Precision, Recall, F1-score, ROC-AUC, PR-AUC
- **Model Comparison**: Baseline vs BERT performance analysis
- **Deployment Ready**: Quantized models, REST API, Streamlit UI

## Methodology

This implementation follows the proposal paper (Code_Trinity_FinalProject.txt) exactly:
- Data preprocessing with lemmatization, stemming, and SMOTE for imbalanced data
- TF-IDF + Logistic Regression baseline with grid search CV
- BERT-base-uncased fine-tuning with AdamW optimizer
- Automated hyperparameter tuning for optimum performance
- Evaluation metrics as specified in proposal Section VI

## Results

Results are exported to:
- `exports/model_comparison.csv` - Baseline vs BERT comparison
- `exports/bert_predictions_test.csv` - Test set predictions
- `exports/confusion_matrices/` - Confusion matrix plots
- `exports/roc_curves/` - ROC and PR curves
- `runs_log.csv` - All experiment logs

## Requirements

See `requirements.txt` for full list. Key dependencies:
- torch, transformers, datasets
- scikit-learn, pandas, numpy
- optuna (for hyperparameter tuning)
- streamlit, fastapi (for prototype app)
- nltk, imbalanced-learn (for preprocessing)

## Notes

- The notebook uses the same cell structure format as 3DEV_Final_Project.ipynb but implements the proposal methodology
- All code is contained in the `Code_Trinity/` folder
- Dataset must be exported first using `export_dataset.py`
- GPU recommended for BERT training but CPU will work (slower)

