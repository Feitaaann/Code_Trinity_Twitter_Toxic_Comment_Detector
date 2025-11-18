# Inference Experiment Descriptions and Results

## Enriquez - Inference Experiment Results

**Description:**
Enriquez conducted an inference experiment testing the fine-tuned BERT model on 30 diverse sample tweets representing different linguistic challenges commonly found in social media. The test samples included explicitly toxic tweets, neutral statements, positive sentiment, sarcastic language, and informal expressions with emojis and slang. The model processed each tweet through tokenization, generated predictions using the trained BERT classifier, and produced probability distributions across all three sentiment classes. For each sample, the model displayed the predicted sentiment class along with confidence percentages and full probability breakdowns showing how confident the model was about each possible classification. The experiment demonstrated the model's practical performance on real-world social media text and revealed its ability to handle nuanced language patterns including sarcasm and informal communication styles. Results showed that the model successfully classified most samples correctly, though some confusion occurred between similar sentiment classes, particularly when dealing with ambiguous language or subtle toxicity.

**Results:**
- Total Samples: 30 tweets
- Correct Predictions: 20 out of 30
- Accuracy: 0.6667 (66.67%)
- Precision (Macro): 0.6629
- Recall (Macro): 0.6609
- F1-Score (Macro): 0.6607

**Figure Name:**
Figure 13. Enriquez_Inference_Experiment

---

## Dulo - Inference Experiment Results

**Description:**
Dulo performed an inference experiment evaluating the BERT model's performance on 25 carefully selected sample tweets covering the full spectrum of sentiment classes. The experiment tested the model's ability to correctly identify toxic content, neutral statements, and positive sentiment across different communication styles and linguistic variations. Each tweet was processed through the tokenization pipeline, fed into the trained BERT model, and analyzed for predicted class, confidence scores, and probability distributions. The model generated predictions with varying confidence levels, showing higher certainty for clearly expressed sentiments and lower confidence for ambiguous or nuanced language. The experiment highlighted the model's strengths in identifying explicit toxic content and positive expressions, while also revealing areas where the model struggled, particularly with sarcastic or indirectly toxic language where surface meaning contradicted true sentiment. The results provided valuable insights into the model's practical applicability for real-world content moderation tasks.

**Results:**
- Total Samples: 25 tweets
- Correct Predictions: 19 out of 25
- Accuracy: 0.7600 (76.00%)
- Precision (Macro): 0.7593
- Recall (Macro): 0.7774
- F1-Score (Macro): 0.7634

**Figure Name:**
Figure 14. Dulo_Inference_Experiment

---

## Morales - Inference Experiment Results

**Description:**
Morales executed an inference experiment examining the BERT model's classification performance on 20 representative sample tweets selected to test various linguistic challenges and sentiment expressions. The test set included examples of explicit toxicity, neutral conversational statements, positive expressions, sarcastic language, and informal communication styles typical of social media platforms. Each sample was processed through the complete inference pipeline: text tokenization, model prediction generation, and probability distribution computation across all three sentiment classes. The model provided detailed output for each tweet including the predicted sentiment class, confidence percentage for that prediction, and full probability breakdowns showing how confident the model was about each possible class. The experiment demonstrated the model's capability to accurately classify most samples while revealing occasional misclassifications, particularly when dealing with subtle toxicity, sarcasm, or ambiguous language patterns. These findings showed the model's strengths in handling clear sentiment expressions and identified areas where further refinement might improve performance on challenging edge cases.

**Results:**
- Total Samples: 20 tweets
- Correct Predictions: 14 out of 20
- Accuracy: 0.7000 (70.00%)
- Precision (Macro): 0.6250
- Recall (Macro): 0.6204
- F1-Score (Macro): 0.6209

**Figure Name:**
Figure 15. Morales_Inference_Experiment

---

## Summary

All three team members conducted independent inference experiments using different sample sizes and tweet selections. The experiments demonstrated consistent model performance across different evaluators, with accuracy ranging from 66.67% to 76.00%, showing the model's reliability in practical applications. The results revealed that the BERT model performs well on clear sentiment expressions but faces challenges with ambiguous or sarcastic language, which is consistent with findings from the main evaluation experiments.

