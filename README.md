# 🌾 Forecasting Commodities Prices with Time Series Models

🇪🇸 [Leer en español](./README_ES.md)

This project aims to identify the best prediction model for monthly prices of three key commodities: **beef**, **corn**, and **soybeans**.

More than 25 models were applied, including classic machine learning regressors, neural networks, statistical models, and AutoTS. The analysis involved training and 12-month forecasting, followed by a comparison against the real observed data.

---

## 📌 Table of Contents

- [1. Introducción](#1-introducción)
- [2. Carga y visualización de las series](#2-carga-y-visualización-de-las-series)
- [3. Modelado y Evaluación](#3-modelado-y-evaluación)
- [4. AutoML](#4-AutoML)
- [5. Comparación Final de Modelos y Selección del Ganador](#5-comparación-final-de-modelos-y-selección-del-ganador)
- [6. Pronóstico Final con Modelo Seleccionado GLM Gaussiano](#6-pronóstico-con-el-modelo-seleccionado-glm-gaussiano)
- [7. Analisis de Estacionalidad STL](#7-análisis-de-estacionalidad-stl)
- [8. Evaluacion Ex-Post con Datos Reales Observados Oct 2024 - May 2025](#8-evaluación-ex-post-con-datos-reales-observados-oct-2024--may-2025)
- [9. Reflexion Final y Aprendizajes](#9-reflexión-final-y-apredizajes)

---

## 📊 Dataset

- **Source:** Simulated dataset with a realistic monthly time series structure from 2010 to 2025.
- **Frequency:** Monthly.
- **Columns:** Date, Beef, Corn, Soybeans.

---

## 🧠 Technologies Used

- Python (Pandas, Matplotlib, Seaborn, Statsmodels, Scikit-learn, Keras, AutoTS)
- Jupyter Notebook
- Visual Studio Code

---

## 🏁 Key Results

Based on the best-performing models from each category, the following table summarizes the error metrics (especially **RMSE** as the main criterion), and shows:

| Commodity | Classical ML              | Neural Networks         | Statistical Models          | AutoTS Ensemble        | Final Winner        |
|-----------|---------------------------|--------------------------|------------------------------|------------------------|---------------------|
| Beef      | AdaBoost Regressor (0.3112) | Tuned LSTM (0.2157)     | **GLM Gaussian (0.1935)**    | Ensemble (0.49)        | ✅ GLM Gaussian      |
| Corn      | Gradient Boosting (21.15)   | Tuned NNAR (17.47)      | **GLM Gaussian (16.74)**     | Ensemble (60.24)       | ✅ GLM Gaussian      |
| Soybeans  | AdaBoost Regressor (48.65)  | Simple LSTM (37.38)     | **GLM Gaussian (32.56)**     | Ensemble (166.02)      | ✅ GLM Gaussian      |

🔍 *The `GLM Gaussian` model proved to be the most efficient in all three cases, achieving the lowest **Root Mean Square Error (RMSE)** and demonstrating more stable behavior compared to other approaches.*
> *The forecasts were compared to real values observed between October 2024 and May 2025.*

---

## 🧭 Reflection

This project allowed me to compare classical, statistical, and neural network approaches for time series forecasting, evaluate their strengths and weaknesses, and understand why some models generalize better. I also experimented with AutoML and learned to interpret results from a practical perspective.

> **This project was developed as part of my Data Science training, with the goal of including it in my professional portfolio for applying to Data Analyst or ML Engineer positions.**

---

🙋‍♀️ About the Author

Hi! I'm Melisa Cardozo, an economist currently studying a Master's in Data Science. I'm passionate about applying AI and machine learning to agriculture, sustainability, and data analysis.

If you're interested in similar topics or would like to collaborate, feel free to connect with me on LinkedIn.


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


## 🌱 Reflections

This project allowed me to:

- Apply a broad range of modeling approaches.
- Visualize time series components through STL decomposition.
- Understand the trade-offs between interpretability and accuracy.
- Learn how external shocks can affect forecast reliability.
- Build a clean, reproducible portfolio piece.

---

## 🙋‍♀️ About the Author

Hi! I'm **Melisa Cardozo**, an economist currently pursuing a Master’s degree in Data Science. I'm passionate about applying AI and machine learning to agriculture, sustainability, and data analysis.

If you’re interested in similar topics or would like to collaborate, feel free to connect with me on [LinkedIn](https://www.linkedin.com/).

---

