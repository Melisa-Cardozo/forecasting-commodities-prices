🌾 Forecasting Agricultural Commodity Prices using Time Series Models

🇪🇸 Leer en español

This project aims to identify the best prediction models for monthly prices of three key agricultural commodities: Beef, Corn, and Soybeans.

Over 25 models were tested, including classical machine learning regressors, neural networks, statistical models, and AutoML (AutoTS). Each model was trained and validated for 12-month forecasts, then compared against real observed data.

📌 Table of Contents

Introduction

Data Loading and Visualization

Modeling and Evaluation

AutoML Implementation

Final Model Comparison and Winner Selection

Final Forecast with Selected GLM Gaussian Model

Seasonality Analysis with STL

Ex-Post Evaluation (Real Data Oct 2024 - May 2025)

Final Reflections and Learnings

📊 Dataset Information

Source: Simulated realistic dataset structured as monthly time series from January 2010 to May 2025.(Data from October 2024 to May 2025 was not used during model training; it was exclusively reserved for ex-post validation to evaluate the predictive accuracy of the final selected model.)

Frequency: Monthly.

Columns: Date, Beef, Corn, Soybeans.

🧠 Technologies Used

Python: Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, Scikit-learn, Keras, AutoTS

Tools: Jupyter Notebook, Visual Studio Code

🏁 Key Results

Based on the best-performing models in each category, the table summarizes RMSE metrics (lower values indicate better performance):

Commodity

Baseline Naïve

Classical ML

Neural Networks

Statistical Models

AutoTS Ensemble

🥇 Final Winner

Beef

0.90

0.3112

0.2157

0.1935

0.49

✅ GLM Gaussian

Corn

32.47

21.15

17.47

16.74

60.24

✅ GLM Gaussian

Soybeans

137.84

48.65

37.38

32.56

166.02

✅ GLM Gaussian

🔍 Conclusion: The GLM Gaussian model was consistently the most effective, achieving the lowest RMSE across all three commodities and demonstrating more stable predictive performance compared to alternative approaches.

Forecasts were validated against real observed data from October 2024 to May 2025, confirming the robustness of the chosen model.

🧭 Reflection and Learnings

Through this project, I gained hands-on experience comparing classical, statistical, and neural network approaches for time series forecasting. It deepened my understanding of:

The strengths and limitations of each modeling approach.

Why certain models generalize and perform better in forecasting tasks.

Implementing AutoML techniques (AutoTS) and interpreting their practical implications.

This work was developed as part of my Data Science Master's program, intended to be included in my professional portfolio for roles as a Data Analyst or Machine Learning Engineer.

🙋‍♀️ About the Author

Hi! I'm Melisa Cardozo, an economist currently pursuing a Master's in Data Science. I'm passionate about applying artificial intelligence and machine learning to agriculture, sustainability, and impactful data analysis.

🌐 Connect with me on LinkedIn.

