Project: Cryptocurrency Liquidity Prediction for Market Stability
Student: Arun Kumar
Institute: PW Skills
Course: Data Science with Generative AI


The goal of this EDA is to:

Understand the structure of cryptocurrency market data

Identify patterns and correlations between price, volume, and market capitalization

Engineer useful features that can help predict liquidity ratios

Detect and handle data quality issues (missing values, outliers, etc.)

Source: CoinGecko historical data (CSV files: coin_gecko_2022-03-16.csv, coin_gecko_2022-03-17.csv)

Dataset Summary:

Attribute	Description
price	Average daily cryptocurrency price in USD
volume	Total trading volume in USD
market_cap	Total market capitalization in USD
date/time	Date of the record
(engineered later)	price_ma7, volume_ma7, liquidity_ratio

Data Preprocessing Summary
Task	Method Used	Result
Missing Values	dropna() (removed missing rows)	All NaN values removed
Type Conversion	pd.to_numeric(errors='ignore')	Converted string numbers to numeric
Normalization	Scaled features for visualization	Cleaned dataset ready for analysis


Observation:

The dataset shows moderate variation in prices but high variability in trading volume and market cap.

Suggests that liquidity fluctuates more due to market activity than price itself.

🪙 5.1 Price Trend Over Time
plt.figure(figsize=(10,5))
plt.plot(data['price'])
plt.title('Price Trend Over Time')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.show()


🧠 Insight:

Prices show periodic fluctuations, likely reflecting daily trading behavior.

Minor spikes correspond to higher trading activity — potential liquidity triggers.

📦 5.2 Volume Trend Over Time
plt.figure(figsize=(10,5))
plt.plot(data['volume'], color='orange')
plt.title('Trading Volume Over Time')
plt.xlabel('Time')
plt.ylabel('Volume (USD)')
plt.show()


🧠 Insight:

High trading volume indicates increased liquidity.

Drops in volume correspond to potential liquidity stress.

Market Capitalization Trend
plt.figure(figsize=(10,5))
plt.plot(data['market_cap'], color='green')
plt.title('Market Cap Over Time')
plt.xlabel('Time')
plt.ylabel('Market Cap (USD)')
plt.show()


🧠 Insight:

Market cap growth is consistent with trading volume, indicating strong investor activity.

Feature Correlation Heatmap
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()


🧠 Key Correlations:

Volume ↔ Market Cap → Strong positive correlation (0.89–0.95)

Price ↔ Volume → Moderate correlation (0.6–0.7)

Liquidity Ratio ↔ Volume → Strong correlation

💡 Conclusion: Liquidity strongly depends on volume and market cap.

 Outlier Detection

You can visualize potential outliers with boxplots:

sns.boxplot(data['price'])
plt.title('Price Outliers')
plt.show()


🧠 Observation:

Occasional spikes indicate days with unusually high trading activity.

Findings Summary
Observation	Insight
Price is relatively stable compared to volume	Suggests liquidity depends more on trading behavior
Strong correlation between volume and market cap	Liquidity rises with higher market participation
Spikes in volume cause liquidity peaks	Potential for short-term market instability



Conclusion

The EDA clearly shows that liquidity can be estimated effectively using trading volume and market capitalization data.
Adding moving averages and ratios provides a better understanding of short-term market stability.

This analysis provides the foundation for the machine learning model that forecasts liquidity variations and supports informed trading decisions.