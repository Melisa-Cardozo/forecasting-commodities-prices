# 🌾 Predicción de Precios de Commodities Agrícolas con Modelos de Series Temporales

[🇬🇧 Read in English](README.md)

Este proyecto busca identificar el mejor modelo de predicción para precios mensuales de tres commodities clave: **carne**, **maíz** y **soja**.

Se aplicaron más de 25 modelos entre regresores clásicos de machine learning, redes neuronales, modelos estadísticos y AutoML (AutoTS). El análisis incluyó tanto el entrenamiento como la evaluación sobre pronósticos de 12 meses, comparando luego con los datos reales disponibles.

---

## 📌 Tabla de contenido

1. [Introducción](#introducción)
2. [Carga y visualización de las series](#carga-y-visualización-de-las-series)
3. [Modelado y Evaluación](#modelado-y-evaluación)
4. [AutoML](#automl)
5. [Comparación Final de Modelos y Selección del Ganador](#comparación-final-de-modelos-y-selección-del-ganador)
6. [Pronóstico Final con Modelo Seleccionado GLM Gaussiano](#pronóstico-final-con-modelo-seleccionado-glm-gaussiano)
7. [Análisis de Estacionalidad STL](#análisis-de-estacionalidad-stl)
8. [Evaluación Ex-Post con Datos Reales Observados Oct 2024 - May 2025](#evaluación-ex-post-con-datos-reales-observados-oct-2024---may-2025)
9. [Reflexión Final y Aprendizajes](#reflexión-final-y-aprendizajes)

---

## 📊 Dataset

* **Fuente:** World Bank Commodity Price Data (The Pink Sheet).

  * Precios mensuales nominales en dólares estadounidenses, disponibles desde 1960 hasta la actualidad.
  * Aunque los datos están disponibles desde 1960, este proyecto utilizó específicamente datos desde enero de 2010 hasta septiembre de 2024 para el entrenamiento y evaluación.
  * (Las series mensuales están disponibles únicamente en dólares estadounidenses nominales.)
  * **Soja:** USD por tonelada métrica.
  * **Maíz:** USD por tonelada métrica.
  * **Carne:** USD por kilogramo.

📌 **Referencias:**

* [World Bank Commodity Price Data](https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Pink-Sheet-October-2024.pdf)
* [Rpubs CES\_BCSF](https://rpubs.com/CES_BCSF/1157675)
* [Base BCSF](https://www.bcsf.com.ar/ces/base-datos/preview/6/precios-internacionales-de-los-commodities)

*(Los datos desde octubre 2024 hasta mayo 2025 no fueron usados en el entrenamiento; se reservaron exclusivamente para la validación ex-post, evaluando la precisión predictiva del modelo final seleccionado.)*

---

## 🧠 Tecnologías utilizadas

* **Python:** Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, Scikit-learn, Keras, AutoTS
* **Herramientas:** Jupyter Notebook, Visual Studio Code

---

## 🏁 Resultados destacados

En base a los modelos ganadores de cada categoría se resumieron los valores de las métricas (RMSE como criterio principal) en el siguiente cuadro:

| Cultivo | Naïve (baseline) | ML Clásico | Redes Neuronales | Modelos Estadísticos | AutoTS Ensemble | 🥇 Ganador Final |
| ------- | ---------------- | ---------- | ---------------- | -------------------- | --------------- | ---------------- |
| Carne   | 0.90             | 0.3112     | 0.2157           | **0.1935**           | 0.49            | ✅ GLM Gaussiano  |
| Maíz    | 32.47            | 21.15      | 17.47            | **16.74**            | 60.24           | ✅ GLM Gaussiano  |
| Soja    | 137.84           | 48.65      | 37.38            | **32.56**            | 166.02          | ✅ GLM Gaussiano  |

🔍 **Conclusión:** El modelo **GLM Gaussiano** resultó ser el más eficiente en los tres casos, logrando el menor error cuadrático medio (RMSE) y mostrando mayor estabilidad frente a otros enfoques.

Se compararon los pronósticos generados con los valores reales observados entre octubre 2024 y mayo 2025.

---

## 🧭 Reflexión

Este proyecto me permitió comparar enfoques clásicos, estadísticos y neuronales para forecasting, evaluar sus ventajas y limitaciones, y entender por qué algunos modelos generalizan mejor. También experimenté con AutoML y aprendí a interpretar los resultados desde un enfoque práctico.

Este trabajo fue realizado como parte de mi formación en Ciencia de Datos, con el objetivo de integrarlo en mi portfolio profesional para postularme a puestos como Data Analyst o ML Engineer.

---

## 🙋‍♀️ Sobre el autor

¡Hola! Soy **Melisa Cardozo**, economista y actualmente estudiante de una maestría en Ciencia de Datos. Me apasiona aplicar la inteligencia artificial y el aprendizaje automático a la agricultura, la sostenibilidad y el análisis de datos.

🌐 Puedes conectar conmigo en [LinkedIn](https://linkedin.com/in/tu-linkedin).

---

## 📌 Estructura del Repositorio

```
forecasting-commodities/
├── data/                         
│   └── precios commodities.xlsx
│
├── notebooks/                    
│   └── forecasting commodities.ipynb
│
├── src/                          
│   └── data.py
│
├── README.md                     
├── README_ES.md                  
└── requirements_clean.txt        
```
