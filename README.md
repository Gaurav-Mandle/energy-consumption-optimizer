# Smart City Energy Consumption Optimizer ⚡

This repository contains a Machine Learning project to predict the hourly electricity load of a smart city neighborhood. Accurate load prediction is crucial for optimizing power distribution, preventing grid overloads, and reducing energy waste.

## 📋 Project Overview
- **ML Task:** Regression
- **Objective:** Predict electricity load (kWh) based on time of day, calendar features, and weather conditions.
- **Key Concepts Covered:** 
  - Data Simulation & Generation
  - Exploratory Data Analysis (EDA)
  - Data Imputation & Cleaning
  - Feature Scaling (`StandardScaler` vs `MinMaxScaler`)
  - Supervised Model Training (Linear Regression & Random Forest Regressor)
  - Model Serialization & Saving (`joblib`)

---

## 📊 Dataset & Features
The dataset simulates 1 year of hourly energy consumption readings (8,760 records) featuring real-world patterns like daily peak hours, seasonal temperature swings, and weekend drop-offs.

### Feature columns:
1. `hour`: Hour of the day (0–23)
2. `day_of_week`: Day of the week (0 = Monday, 6 = Sunday)
3. `month`: Month of the year (1–12)
4. `temperature`: Hourly temperature in Celsius (includes seasonal variation & random noise)
5. `humidity`: Hourly humidity percentage (40% to 90%)
6. `is_weekend`: Binary flag (1 if weekend, 0 otherwise)

**Target Variable:**
- `electricity_load`: Energy consumption in kWh.

---

## 📈 Model Performance & Evaluation
Two regression models were trained on the scaled features:
1. **Linear Regression** (baseline)
2. **Random Forest Regressor** (100 decision trees)

### Metrics:
- **R² Score (Coefficient of Determination):** Measures how closely the predictions match actual values (higher is better).
- **Mean Squared Error (MSE):** Measures average squared difference between predictions and actuals (lower is better).

*Results show that the Random Forest Regressor achieves significantly higher accuracy and closely maps actual electricity consumption compared to the baseline Linear Regression model.*

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed. You can install all dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Running the Notebook
You can open and run the Jupyter notebook:

```bash
jupyter notebook energy_consumption_optimizer.ipynb
```


