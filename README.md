# Wine Quality Predictor

This project aims to analyze the `winequality.csv` dataset to predict the quality of wine based on various chemical properties. The dataset includes features describing the chemical composition of different wines, and the goal is to build a predictive model that can assess wine quality.

## Dataset Overview

The `winequality.csv` dataset consists of several physicochemical properties of wines, which can be used to predict the quality rating. The dataset includes the following columns:

- **Fixed Acidity:** The amount of non-volatile acids in the wine.
- **Volatile Acidity:** The amount of acetic acid in wine, which can affect its taste.
- **Citric Acid:** The amount of citric acid, contributing to the wine's acidity.
- **Residual Sugar:** The amount of sugar remaining after fermentation.
- **Chlorides:** The amount of salt in the wine.
- **Free Sulfur Dioxide:** The amount of free sulfur dioxide.
- **Total Sulfur Dioxide:** The total amount of sulfur dioxide.
- **Density:** The density of the wine.
- **pH:** The acidity or alkalinity of the wine.
- **Sulphates:** The amount of sulfates added to the wine.
- **Alcohol:** The alcohol content in the wine.
- **Quality:** The target variable (score between 0 and 10), representing the quality of the wine as rated by experts.

## Project Objectives

The main goals of this project are:
1. **Exploratory Data Analysis (EDA):** To explore the relationships and distributions of various features in the dataset.
2. **Data Preprocessing:** To clean the dataset, handle missing values, and perform feature scaling if necessary.
3. **Model Development:** To build machine learning models that predict the quality of wine based on the given features.
4. **Model Evaluation:** To evaluate model performance using metrics like accuracy, mean squared error, R-squared, and others.
5. **Feature Importance Analysis:** To identify which features are most influential in determining wine quality.

## Exploratory Data Analysis (EDA)

- **Data Distribution:** Analyzed the distribution of each feature using histograms and boxplots.
- **Correlation Analysis:** Generated a correlation heatmap to identify relationships between features and the target variable (quality).
- **Missing Values:** Checked for missing or inconsistent values in the dataset.
- **Outliers:** Used boxplots to detect outliers, particularly in acidity, residual sugar, and alcohol content.

## Data Preprocessing

- **Handling Missing Values:** Imputed missing values where necessary, though the dataset had very few or no missing entries.
- **Normalization/Standardization:** Scaled the features to bring them onto a similar scale, especially for algorithms sensitive to feature scaling.
- **Train-Test Split:** Split the data into training and testing sets for evaluating model generalization.

## Machine Learning Models

The following machine learning algorithms were implemented and compared:
1. **Linear Regression:** A baseline model for regression tasks.
2. **Decision Tree Regressor:** A tree-based model to capture non-linear relationships in the data.
3. **Random Forest Regressor:** An ensemble model to improve accuracy and reduce overfitting.
4. **Support Vector Regressor (SVR):** A model to find the optimal hyperplane for predicting wine quality.
5. **Gradient Boosting Regressor:** A boosting algorithm for better performance.

## Model Evaluation

- **Mean Squared Error (MSE):** Measured the average squared difference between the predicted and actual quality ratings.
- **R-squared (R²):** Assessed the proportion of variance in wine quality explained by the model.
- **Cross-Validation:** Used K-fold cross-validation to ensure model generalization and avoid overfitting.
- **Feature Importance:** Evaluated the influence of each feature on the model’s predictions.

## Results

- The models demonstrated varying degrees of accuracy, with ensemble methods such as Random Forest and Gradient Boosting showing the best performance.
- Feature importance analysis indicated that alcohol content, volatile acidity, and sulphates were significant predictors of wine quality.
- Hyperparameter tuning significantly improved the performance of some models.

## Future Work

- **Hyperparameter Optimization:** Further fine-tuning to achieve better prediction accuracy.
- **Feature Engineering:** Exploring new features or combinations of existing features for improved prediction.
- **Deploying the Model:** Creating a web interface to predict wine quality based on user input.
- **Using Additional Data:** Incorporating a larger and more diverse wine dataset for better generalization.

## Project Structure

- `data/`: Contains the `winequality.csv` dataset.
- `notebooks/`: Jupyter notebooks for EDA and model development.
- `src/`: Source code for data processing, modeling, and evaluation.
- `models/`: Trained models used for prediction.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Prerequisites

- Python 3.x
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `jupyter`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/wine-quality-predictor.git
   cd wine-quality-predictor
2. **Install all the required packages:**
   ```bash
   pip install -r requirements.txt
 3.**Run the jupyter notebook:**
   ```bash
   jupyter notebook
