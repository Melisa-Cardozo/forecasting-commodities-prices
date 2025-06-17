# Forecasting Commodities Prices 📈

🇪🇸 [Leer en español](./README_ES.md)

## 📌 Overview

This project explores and compares different forecasting models to predict monthly prices of key agricultural commodities: beef, corn, and soybeans. 

The goal was to evaluate multiple modeling families (statistical, machine learning, neural networks, and automated tools) and determine which provided the most accurate forecasts for each time series.

---

## 📂 Project Structure

- `Forecasting Commodities Prices.ipynb`: Main notebook containing all analysis, modeling, and visualizations.
- `precios commodities.xlsx`: Dataset with monthly prices from 2010 to 2025.
- `README.md`: Project description (English).
- `README_ES.md`: Project description (Spanish).
- `images/`: Folder with relevant visualizations for the README (optional).

---

## 📈 Models Evaluated

1. **Classical Machine Learning**  
   AdaBoost, Gradient Boosting, Random Forest...

2. **Neural Networks**  
   LSTM (Keras), NNAR (statsmodels)...

3. **Statistical Models**  
   ARIMA, SARIMA, Holt-Winters, GLM Gaussian...

4. **AutoML**  
   AutoTS, FLAML...

---

🏁 Key Results  
Based on the best-performing models from each category, the following table summarizes the main error metrics (with **RMSE** used as the primary criterion). The findings were:

| Commodity | Classical ML                | Neural Networks         | Statistical Models           | AutoTS Ensemble       | Final Winner        |
|-----------|-----------------------------|-------------------------|------------------------------|-----------------------|---------------------|
| Beef      | AdaBoost Regressor (0.3112) | Tuned LSTM (0.2157)     | **GLM Gaussian (0.1935)**    | Ensemble (0.49)       |  GLM Gaussian       |
| Corn      | Gradient Boosting (21.15)   | Tuned NNAR (17.47)      | **GLM Gaussian (16.74)**     | Ensemble (60.24)      |  GLM Gaussian       |
| Soybeans  | AdaBoost Regressor (48.65)  | Simple LSTM (37.38)     | **GLM Gaussian (32.56)**     | Ensemble (166.02)     |  GLM Gaussian       |
 
🔍 The **GLM Gaussian model** proved to be the most effective across all three commodities, consistently achieving the lowest **Root Mean Square Error (RMSE)** and demonstrating more stable behavior compared to other approaches.

The 12-month forecasts were then compared to the **actual values observed between October 2024 and May 2025**.


---

## 🔎 Forecast Results

Forecasts were generated for the 12-month period between October 2024 and September 2025 and compared to the actual values available through May 2025.

---

## 🔧 Tools and Libraries

- Python 3.11
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn, Statsmodels
- Keras, AutoTS, FLAML
- Jupyter Notebook

---

## 🙋‍♀️ About the Author

Hi! I'm **Melisa Cardozo**, an economist currently pursuing a Master’s degree in Data Science. I'm passionate about applying AI and machine learning to agriculture, sustainability, and public data analysis.

If you’re interested in similar topics or would like to collaborate, feel free to connect with me on [LinkedIn](https://www.linkedin.com/).

---

## 🌱 Reflections

This project allowed me to:

- Apply a broad range of modeling approaches.
- Visualize time series components through STL decomposition.
- Understand the trade-offs between interpretability and accuracy.
- Learn how external shocks can affect forecast reliability.
- Build a clean, reproducible portfolio piece.

