# Ethereum Fraud Account Detection

<p align="center">
  <img width="600" height="300" src="https://github.com/shazzad-hasan/ethereum-fraud-detection/blob/main/ethereum.png" />
</p>

The blockchain technology-based cryptocurrency Ether has gained substantial popularity, emerging as the second-largest cryptocurrency by market capitalization after Bitcoin as of 2024. Despite the robust security features offered by the Ethereum platform, the prevalence of illegal activities such as money laundering, bribery, phishing, and Ponzi schemes has risen remarkably in recent years. Moreover, the vast number of deployed smart contracts and the lack of comprehensive analytics tools for these contracts pose challenges in gaining insights from this complex ecosystem. To address these challenges, I developed some machine learning models, utilizing Logistic Regression, Support Vector Machine, Multi-layer Perceptron, Random Forest, Extreme Gradient Boosting, and Light Gradient Boosting, based on transaction history to classify accounts as fraudulent or non-fraudulent. Comparative analysis of these models reveals that tree-based ensemble models, particularly Random Forest, and gradient boosting methods, outperform others in terms of classification accuracy.

### Performance Comparison of Classification Models

<div align="center">

| Models             | Precision | Recall | Accuracy | F1-score | AUC-ROC |
|--------------------|-----------|--------|----------|----------|---------|
| Logistic Regression | 0.8693    | 0.8313 | 0.8674   | 0.8499   | 0.9407  |
| SVM                | 0.9146    | 0.8870 | 0.9116   | 0.9006   | 0.9594  |
| MLP                | 0.9258    | 0.8846 | 0.9159   | 0.9048   | 0.9700  |
| Random Forest      | 0.9334    | 0.9260 | 0.9367   | 0.9297   | 0.9842  |
| XGBoost            | 0.9388    | 0.9276 | 0.9400   | 0.9331   | 0.9882  |
| LightGBM           | 0.9400    | 0.9363 | 0.9443   | 0.9382   | 0.9880  |


<div align="center">
    <img src="https://github.com/shazzad-hasan/ethereum-fraud-detection/blob/main/results/images/roc_curve.png" alt="ROC Curves" width="45%" />
    <img src="https://github.com/shazzad-hasan/ethereum-fraud-detection/blob/main/results/images/pr_curve.png" alt="PR Curves" width="45%" />
</div>

