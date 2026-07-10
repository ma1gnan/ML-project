# ML-project
Forecasting Residential Electricity Demand in Georgia Using Time Series Machine Learning
# Forecasting Residential Electricity Demand in Georgia Using Time Series Machine Learning

## Project Overview

This project develops and evaluates machine learning models to forecast hourly residential electricity demand in Georgia using historical electricity consumption and weather observations. Accurate short-term electricity demand forecasting helps utility companies improve power generation planning, maintain grid reliability, and prepare for periods of peak energy consumption.

The project compares traditional statistical forecasting methods with modern machine learning algorithms to determine the most accurate approach for predicting the next hour's electricity demand.

---

## Research Question

Can historical electricity demand combined with historical weather observations accurately predict electricity demand for the next immediate hour?

---

## Objectives

- Collect historical electricity demand data.
- Collect historical weather data.
- Merge both datasets into a single hourly dataset.
- Perform exploratory data analysis (EDA).
- Engineer time-series features.
- Train and compare multiple forecasting models.
- Evaluate model performance using standard regression metrics.
- Identify the best-performing forecasting model.

---

## Dataset

### Electricity Demand

- **Source:** U.S. Energy Information Administration (EIA)
- **Dataset:** EIA-930 Hourly and Daily Balancing Authority Operations Report
- **Balancing Authority:** SOCO (Southern Company)

The dataset contains hourly electricity demand (MW) for Georgia's primary service territory.

### Weather Data

Historical weather observations collected from:

- NOAA ASOS
- Open-Meteo Historical Weather API

Features include:

- Temperature
- Humidity
- Precipitation

---

## Feature Engineering

Additional features created for forecasting include:

- Hour of Day
- Day of Week
- Month
- Holiday Indicator
- Previous Hour Demand (Lag-1)
- Previous Day Demand (Lag-24)
- Previous Week Demand (Lag-168)
- Rolling Average Features

---

## Data Preprocessing

The preprocessing pipeline includes:

- Merging electricity and weather datasets
- Timestamp alignment
- Missing value handling
- Removal of anomalous records
- Feature scaling (when required)
- Chronological train/test split (Walk-Forward Validation)

---

## Machine Learning Models

### Baseline Models

- Naive Forecast
- Moving Average
- Linear Regression
- Ridge Regression

### Statistical Models

- ARIMA
- Prophet

### Machine Learning Models

- XGBoost
- LightGBM

### Stretch Goal

- Long Short-Term Memory (LSTM)

---

## Evaluation Metrics

Model performance is evaluated using:

- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)

---

## Project Structure

```
Forecasting-Electricity-Demand/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── feature_engineering.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_models.py
│   ├── evaluate_models.py
│
├── results/
│   ├── figures/
│   ├── model_outputs/
│
├── report/
│   ├── IEEE_Final_Report.pdf
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Workflow

1. Download electricity demand data.
2. Download historical weather data.
3. Clean and merge datasets.
4. Perform exploratory data analysis.
5. Engineer predictive features.
6. Train forecasting models.
7. Evaluate model performance.
8. Compare forecasting accuracy.
9. Select the best-performing model.

---

## Visualizations

The project includes:

- Electricity Demand Time Series
- Temperature vs. Demand Scatter Plot
- Seasonal Demand Trends
- Predicted vs. Actual Demand
- Feature Importance
- Model Comparison Charts

---

## Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- LightGBM
- Prophet
- Statsmodels
- Jupyter Notebook

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ma1gnan/ML-project.git
```

Navigate into the project folder:

```bash
cd Forecasting-Electricity-Demand
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the preprocessing pipeline:

```bash
python src/data_preprocessing.py
```

Train the forecasting models:

```bash
python src/train_models.py
```

Evaluate model performance:

```bash
python src/evaluate_models.py
```

---

## Expected Results

The project compares multiple forecasting methods to determine which model provides the most accurate hourly electricity demand predictions.

The expected outcome is that gradient boosting methods such as **XGBoost** or **LightGBM** will outperform traditional statistical forecasting approaches by better capturing nonlinear relationships between weather conditions and electricity demand.

---

## Future Improvements

- Incorporate additional weather variables
- Add holiday-specific demand modeling
- Develop deep learning LSTM models
- Build an interactive forecasting dashboard
- Deploy the model as a web application

---

## Team

Summer 2026 Machine Learning Project

- Deborah Maignan
- Brian Smith
- Catia de Moraes

---

## License

This project is intended for educational purposes as part of a Machine Learning course.

---

## Acknowledgments

- U.S. Energy Information Administration (EIA)
- NOAA ASOS Weather Data
- Open-Meteo Historical Weather API
- Georgia State University
- Course: Machine Learning (Summer 2026)
