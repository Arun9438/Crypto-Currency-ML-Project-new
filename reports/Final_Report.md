Cryptocurrency markets are highly volatile, and liquidity — the ability to buy or sell an asset without causing large price changes — plays a crucial role in maintaining market stability.

This project focuses on developing a machine learning model to forecast cryptocurrency liquidity using historical data such as price, volume, and market capitalization.

The goal is to identify early liquidity crises and help traders and financial institutions make better decisions.



A lack of liquidity can lead to:

Large price swings

Increased volatility

Poor market depth

To tackle this, the project uses machine learning to predict future liquidity ratios and detect instability before it happens.


| Feature           | Description                           |
| ----------------- | ------------------------------------- |
| `price`           | Average price of cryptocurrency (USD) |
| `volume`          | Total trading volume (USD)            |
| `market_cap`      | Market capitalization (USD)           |
| `price_ma7`       | 7-day moving average of price         |
| `volume_ma7`      | 7-day moving average of volume        |
| `liquidity_ratio` | Calculated as volume / market_cap     |



Exploratory Data Analysis (EDA)

Goals:

Understand relationships between features

Identify trends in trading volume and liquidity

Visuals Created:

Price Trend Over Time

Trading Volume Over Time

Market Capitalization Over Time

Feature Correlation Heatmap

Key Insights:

Strong positive correlation between volume and market_cap (0.9+).

Liquidity fluctuates with trading activity, not price.

Volume spikes signal temporary liquidity peaks.






| Feature             | Formula                        | Description                      |
| ------------------- | ------------------------------ | -------------------------------- |
| `price_ma7`         | 7-day moving average of price  | Smooths out price fluctuations   |
| `volume_ma7`        | 7-day moving average of volume | Captures trading activity trends |
| `price_volatility7` | Rolling standard deviation     | Measures price uncertainty       |
| `liquidity_ratio`   | volume / (market_cap + 1e-9)   | Target variable for model        |



Model Development

Algorithm Used: Random Forest Regressor
Reason: Handles nonlinear relationships and avoids overfitting.

Model Workflow:

Split data into training (80%) and testing (20%)

Trained RandomForestRegressor

Performed GridSearchCV for hyperparameter tuning

Hyperparameters Tuned:

Number of trees (n_estimators): [100, 200, 300]

Tree depth (max_depth): [None, 5, 10]


| Metric | Formula                    | Purpose                |         |                     |
| ------ | -------------------------- | ---------------------- | ------- | ------------------- |
| RMSE   | √(Σ(y_pred - y_true)² / n) | Measures average error |         |                     |
| MAE    |                            | y_pred - y_true        | average | Absolute difference |
| R²     | 1 - (SS_res / SS_tot)      | Model fit quality      |         |                     |



| Metric | Score |
| ------ | ----- |
| RMSE   | 0.023 |
| MAE    | 0.017 |
| R²     | 0.92  |



| Deliverable         | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| **Cleaned Dataset** | `artifacts/clean/combined.csv`                                 |
| **Feature Dataset** | `artifacts/features/features.csv`                              |
| **EDA Report**      | `reports/EDA_Report.md`                                        |
| **Model & Metrics** | `artifacts/models/model.pkl`, `artifacts/metrics/metrics.json` |
| **Documentation**   | HLD, Final Reports                              |
| **Streamlit App**   | Interactive prediction UI                                      |
