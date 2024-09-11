# CritoRisk

Here’s a formal description of your **Credit Card Fraud Detection Project**:

---

### Credit Card Fraud Detection using Logistic Regression

This project aims to detect fraudulent transactions in credit card data using a binary classification model. The dataset is highly imbalanced, with a small proportion of fraudulent transactions compared to legitimate ones. To address this imbalance, the model employs techniques such as downsampling and applies logistic regression for classification.

#### Key Features:
1. **Data Preprocessing**: 
   - The dataset was cleaned by checking for missing values and handling the class imbalance. Legitimate transactions were downsampled to match the number of fraudulent transactions, resulting in a balanced dataset for model training.

2. **Model Selection**:
   - A **Logistic Regression** model was selected for its interpretability and efficiency in binary classification tasks. The dataset was split into training and testing sets, ensuring stratification to maintain class distribution.

3. **Performance Metrics**:
   - The model’s performance was evaluated using **accuracy**, achieving 95.04% on the training set and 93.40% on the testing set.
   - Additional metrics such as **precision**, **recall**, **F1-score**, and a **confusion matrix** were computed to provide a deeper analysis of the model's ability to detect fraudulent transactions, especially in the context of class imbalance.
     |![image](https://github.com/user-attachments/assets/15c26bb3-6b29-4f5e-a1bc-c4637b7936fe)|![image](https://github.com/user-attachments/assets/c4a203e2-e89c-443e-b1cd-d9b7dbaa3401)|
     |--|--|

     |![image](https://github.com/user-attachments/assets/ec4f8b0d-ecd9-4ddb-9f73-623636b850fc)|
     |-|

     | Dataset | <a href="https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud"> link </a> |
     |-|-|



This project highlights the use of machine learning techniques to address real-world fraud detection challenges by leveraging logistic regression and advanced evaluation metrics for balanced model performance.
