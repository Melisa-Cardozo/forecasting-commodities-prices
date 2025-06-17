# 🌾 Forecasting Commodities Prices with Time Series Models

Este proyecto busca identificar el mejor modelo de predicción para precios mensuales de tres commodities clave: **carne**, **maíz** y **soja**.

Se aplicaron más de 25 modelos entre regresores clásicos de machine learning, redes neuronales, modelos estadísticos y AutoTS. El análisis incluyó tanto el entrenamiento como la evaluación sobre pronósticos de 12 meses, comparando luego con los datos reales disponibles.

---

## 📌 Tabla de contenido

- [1. Introducción](#1-introducción)
- [2. Carga y visualización de las series](#2-carga-y-visualización-de-las-series)
- [3. Modelado clásico con ML](#3-modelado-clásico-con-ml)
- [4. Modelado con redes neuronales](#4-modelado-con-redes-neuronales)
- [5. Modelado con técnicas estadísticas](#5-modelado-con-técnicas-estadísticas)
- [6. Análisis de descomposición STL](#6-análisis-de-descomposición-stl)
- [7. Evaluación del pronóstico con datos reales](#7-evaluación-del-pronóstico-con-datos-reales)
- [8. Reflexión final y aprendizajes](#8-reflexión-final-y-aprendizajes)

---

## 📊 Dataset

- **Fuente:** Base simulada con estructura realista de series temporales mensuales entre 2010 y 2025.
- **Frecuencia:** Mensual.
- **Columnas:** Fecha, Carne, Maíz, Soja.

---

## 🧠 Tecnologías utilizadas

- Python (Pandas, Matplotlib, Seaborn, Statsmodels, Scikit-learn, Keras, AutoTS)
- Jupyter Notebook
- Visual Studio Code

---

## 🏁 Resultados destacados

En base a los resultados obtenidos para los distintos modelos y los valores de las métricas (especialmente **RMSE** como criterio principal), se observó que:

| Cultivo |        ML Clásico            |     Redes Neuronales    |   Modelos Estadísticos      | AutoTS Ensemble   |  **Ganador Final** |
| --------|------------------------------|-------------------------|-----------------------------|-------------------|--------------------|
|  Carne  | AdaBoost Regressor (0.3112)  | LSTM ajustado (0.2157)  | **GLM Gaussiano (0.1935)**  | Ensemble (0.49)   |  **GLM Gaussiano** |
|  Maíz   | Gradient Boosting (21.15)    | NNAR ajustado (17.47)   | **GLM Gaussiano (16.74)**   | Ensemble (60.24)  |  **GLM Gaussiano** |
|  Soja   | AdaBoost Regressor (48.65)   | LSTM simple (37.38)     | **GLM Gaussiano (32.56)**   | Ensemble (166.02) |  **GLM Gaussiano** |

🔍 *El modelo `GLM Gaussiano` resultó ser el más eficiente en los tres casos, logrando el menor error cuadrático medio (RMSE), y mostrando mayor estabilidad frente a otros enfoques.*
> *Se compararon los pronósticos generados con los valores reales observados entre octubre 2024 y mayo 2025.*

---

## 🧭 Reflexión

Este proyecto me permitió comparar enfoques clásicos, estadísticos y neuronales para forecasting, evaluar sus ventajas y limitaciones, y entender por qué algunos modelos generalizan mejor. También experimenté con AutoML y aprendí a interpretar los resultados desde un enfoque práctico.

> **Este trabajo fue realizado como parte de mi formación en Ciencia de Datos, pero con el objetivo de integrar mi portfolio profesional para postularme a puestos como Data Analyst o ML Engineer.**

---

## 🧷 Nota

Si los enlaces de esta tabla no funcionan directamente en GitHub, podés navegar por los encabezados del notebook. Esto se debe a que GitHub no interpreta anclas internas en archivos `.ipynb`.

