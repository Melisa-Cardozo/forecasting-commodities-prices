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

| Commodity | Classical ML                | Neural Networks         | Statistical Models           | AutoTS Ensemble        | Final Winner       |
|-----------|-----------------------------|-------------------------|------------------------------|------------------------|--------------------|
| Beef      | AdaBoost Regressor (0.3112) | Tuned LSTM (0.2157)     | **GLM Gaussian (0.1935)**    | Ensemble (0.49)        |  GLM Gaussian      |
| Corn      | Gradient Boosting (21.15)   | Tuned NNAR (17.47)      | **GLM Gaussian (16.74)**     | Ensemble (60.24)       |  GLM Gaussian      |
| Soybeans  | AdaBoost Regressor (48.65)  | Simple LSTM (37.38)     | **GLM Gaussian (32.56)**     | Ensemble (166.02)      |  GLM Gaussian      |

🔍 *The `GLM Gaussian` model proved to be the most efficient in all three cases, achieving the lowest **Root Mean Square Error (RMSE)** and demonstrating more stable behavior compared to other approaches.*
> *The forecasts were compared to real values observed between October 2024 and May 2025.*

---

## 🧭 Reflection

This project allowed me to compare classical, statistical, and neural network approaches for time series forecasting, evaluate their strengths and weaknesses, and understand why some models generalize better. I also experimented with AutoML and learned to interpret results from a practical perspective.

> **This project was developed as part of my Data Science training, with the goal of including it in my professional portfolio for applying to Data Analyst or ML Engineer positions.**

---

🙋‍♀️ About the Author

Hi! I'm Melisa Cardozo, an economist currently studying a Master's in Data Science. I'm passionate about applying AI and machine learning to agriculture, sustainability, and data analysis.

If you’re interested in similar topics or would like to collaborate, feel free to connect with me on [LinkedIn](https://www.linkedin.com/).

---

