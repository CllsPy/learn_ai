# Overview

Welcome to the 2024 Kaggle Playground Series! We plan to continue in the spirit of previous playgrounds, providing interesting an approachable datasets for our community to practice their machine learning skills, and anticipate a competition each month.
Your Goal: Predict the probability of various defects on steel plates. Good luck!

# Evaluation
Submissions are evaluated using area under the ROC curve using the predicted probabilities and the ground truth targets.
To calculate the final score, AUC is calculated for each of the 7 defect categories and then averaged. In other words, the score is the average of the individual AUC of each predicted column.

# Citation
Walter Reade, Ashley Chow. (2024). Regression with an Abalone Dataset. Kaggle. https://kaggle.com/competitions/playground-series-s4e4
