 ┌────────────────────────┐
 │  Raw Data (CSV Files)  │
 └────────────┬───────────┘
              ↓
 ┌────────────────────────┐
 │ Data Preprocessing     │
 │  - Clean missing data  │
 │  - Normalize features  │
 └────────────┬───────────┘
              ↓
 ┌────────────────────────┐
 │ Feature Engineering    │
 │  - Moving Averages     │
 │  - Volatility Ratios   │
 │  - Liquidity Ratio     │
 └────────────┬───────────┘
              ↓
 ┌────────────────────────┐
 │ Model Training         │
 │  - Random Forest       │
 │  - Evaluate Metrics    │
 └────────────┬───────────┘
              ↓
 ┌────────────────────────┐
 │ Deployment (Streamlit) │
 │  - Input Parameters    │
 │  - Predict Liquidity   │
 └────────────────────────┘



| Layer         | Tool / Library                        |
| ------------- | ------------------------------------- |
| Programming   | Python 3.x                            |
| Data Handling | Pandas, NumPy                         |
| Visualization | Matplotlib, Seaborn                   |
| ML Framework  | Scikit-learn                          |
| Deployment    | Streamlit                             |
| IDE           | Visual Studio Code / Jupyter Notebook |



| Interface           | Description                                                         |
| ------------------- | ------------------------------------------------------------------- |
| **User Interface**  | Streamlit app with text inputs for Price, Volume, and Market Cap    |
| **Data Interface**  | Reads data from local CSV files in the `data/` folder               |
| **Model Interface** | Random Forest model trained in Python and integrated with Streamlit |


Process Flow Summary

Data Loading: Merge multiple CSVs into a single DataFrame.

Preprocessing: Remove missing values, normalize data.

Feature Engineering: Generate moving averages and liquidity ratio.

Model Training: Train ML model on historical data.

Evaluation: Test model accuracy with RMSE, MAE, R².

Deployment: Provide local interface for prediction.

 Expected Outcome

An accurate model that can forecast cryptocurrency liquidity.

Insights on which factors (volume, market cap) impact liquidity the most.

Deployed application where users can input current crypto stats and get instant liquidity predictions.

 Future Enhancements

Integrate real-time API data (CoinGecko or Binance).

Add sentiment analysis using Twitter or Reddit data.

Improve forecasting using LSTM (Deep Learning).

Deploy on cloud (AWS / Azure) for live access.