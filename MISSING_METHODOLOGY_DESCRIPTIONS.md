# Missing Methodology Sections - Descriptions and Screenshot Guide

## Section V.E.ii - Baseline Evaluation on Validation Set

**Title:**
Baseline Evaluation on Validation Set

**Description:**
Before testing on the final test set, we evaluated the baseline Logistic Regression model on the validation set to establish a performance baseline. The evaluation process transformed validation text using the fitted TF-IDF vectorizer and generated predictions from the trained model. We computed accuracy, precision, recall, and F1-score metrics to measure how well the baseline model performed on unseen validation data. The results showed the baseline model's ability to classify tweets into three categories: negative or toxic, neutral, and positive. We also created a confusion matrix visualization to see where the model made correct predictions and where it confused different classes. This validation evaluation provided a performance benchmark for comparing against the BERT model on the same validation data.

**Figure Name:**
Figure 7. Baseline_Validation_Evaluation

**Cell to Screenshot:**
Look for the code cell that starts with:
```
print("Evaluating baseline model on validation set...")
```

---

## Section V.E.iii - BERT Evaluation on Validation Set

**Title:**
BERT Evaluation on Validation Set

**Description:**
We evaluated the fine-tuned BERT model on the validation set to assess its performance before final test evaluation. The evaluation loaded the best BERT checkpoint from hyperparameter tuning and created a Trainer instance configured for evaluation. We ran the model on the validation dataset and computed the same metrics used during training: accuracy, precision, recall, and F1-score. The model generated predictions for all validation samples, which we then converted from BERT's internal label format back to our original format for consistent reporting. We generated a detailed classification report showing per-class performance metrics and created a confusion matrix visualization. This validation evaluation allowed us to compare BERT's performance directly with the baseline model and verify that the transformer model learned generalizable patterns rather than memorizing the training data.

**Figure Name:**
Figure 8. BERT_Validation_Evaluation

**Cell to Screenshot:**
Look for the code cell that starts with:
```
print("\nEvaluating BERT model on validation set...")
```

---

## Section V.E.iv - Validation vs Test Set Comparison

**Title:**
Validation vs Test Set Comparison

**Description:**
We compared model performance between validation and test sets for both the baseline and BERT models to check for overfitting and ensure generalization. This analysis calculated the absolute differences between validation and test metrics to identify any significant performance gaps that might indicate the models memorized validation data. We created a structured comparison table showing all metrics for both models across both dataset splits. We then generated a multi-panel visualization with grouped bar charts comparing validation versus test performance for each metric: accuracy, precision, recall, and F1-macro. This comparison helped verify that both models maintained consistent performance across validation and test sets, confirming that our training approach learned generalizable patterns rather than fitting to specific validation examples. The results showed that both models performed similarly on validation and test data, indicating good generalization capability.

**Figure Name:**
Figure 9. Validation_Test_Comparison

**Cell to Screenshot:**
Look for the code cell that starts with:
```
print("Validation vs Test Set Performance Comparison")
```

---

## Section V.E.v - Visualization and Analysis

**Title:**
Visualization and Analysis

**Description:**
We created a comprehensive visualization grid to analyze and compare model performance across multiple dimensions. The visualization combined four key visualizations into a single figure: confusion matrices for both baseline and BERT models showing true versus predicted labels, a side-by-side bar chart comparing accuracy, precision, recall, and F1-macro between the two models on the test set, and a bar chart showing the test set class distribution. The confusion matrices revealed how each model classified samples across all three sentiment classes, highlighting where predictions matched true labels and where errors occurred. The metric comparison chart made it easy to see which model performed better for each evaluation metric. The class distribution chart showed the balance of samples across negative or toxic, neutral, and positive categories in the test set. This unified visualization provided a complete picture of model performance and helped identify patterns in classification behavior.

**Figure Name:**
Figure 10. Model_Visualization_Analysis

**Cell to Screenshot:**
Look for the code cell that starts with:
```
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
```

---

## Section V.E.vi - Inference Examples and Model Testing

**Title:**
Inference Examples and Model Testing

**Description:**
We demonstrated the BERT model's practical performance by testing it on diverse sample tweets representing different linguistic challenges commonly found in social media. The test samples included explicitly toxic tweets, neutral statements, positive sentiment, sarcastic or indirectly toxic language where surface meaning contradicts true sentiment, and informal positive expressions with emojis and slang. For each sample tweet, the model tokenized the input, processed it through the trained BERT model, and generated probability distributions across all three sentiment classes. We displayed the predicted sentiment class, the confidence percentage for that prediction, and the full probability breakdown showing how confident the model was about each possible class. This demonstration showed the model's ability to handle nuanced language patterns including sarcasm and informal communication styles. The results provided transparency into how the model makes predictions and its level of confidence for different types of social media text.

**Figure Name:**
Figure 11. Model_Inference_Examples

**Cell to Screenshot:**
Look for the code cell that starts with:
```
sample_tweets = [
```

---

## Section V.E.vii - Export and Deployment Preparation

**Title:**
Export and Deployment Preparation

**Description:**
We prepared all necessary artifacts for model deployment and research reproduction. The export process saved the trained BERT model in multiple formats: full PyTorch format for complete model restoration, and quantized format using dynamic quantization to reduce model size for efficient deployment. We consolidated all experiment runs from our training logs into exportable CSV and Excel formats for easy sharing and analysis. We generated a comprehensive model card in JSON format containing model metadata, architecture details, training configuration, dataset information, and performance metrics. We also created a human-readable summary report comparing baseline and BERT model performance, documenting F1-macro improvements and target achievement status. All exported artifacts were organized in a dedicated exports directory with clear naming conventions. This comprehensive export ensured that classmates and graders could reproduce, audit, and extend our workflow without rerunning training from scratch, supporting transparency and research reproducibility.

**Figure Name:**
Figure 12. Deployment_Preparation

**Cell to Screenshot:**
Look for the code cell that starts with:
```
print("Exporting artifacts for deployment...")
```

---

## Summary

All missing subsections from Section V.E. Model Evaluation have been documented above. Each includes:
- Title for the subsection
- One paragraph description (simple language, no em dashes, no AI-structured phrasing, no deep technical terms)
- Figure name for the screenshot
- First line of the code cell to help locate the correct cell for screenshot

You can use these descriptions directly in your IEEE paper's Methodology section.

