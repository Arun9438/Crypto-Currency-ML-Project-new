import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from data_preprocessing import load_and_clean_data
from feature_engineering import add_features

st.title("Crypto Liquidity Prediction App")

data = load_and_clean_data()
data = add_features(data)

X = data[['price', 'volume', 'market_cap', 'price_ma7', 'volume_ma7']]
y = data['liquidity_ratio']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

price = st.number_input("Enter Price:")
volume = st.number_input("Enter Volume:")
market_cap = st.number_input("Enter Market Cap:")

if st.button("Predict Liquidity"):
    pred = model.predict([[price, volume, market_cap, price, volume]])
    st.success(f"Predicted Liquidity Ratio: {pred[0]:.4f}")
