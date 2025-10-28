import pandas as pd
from data_preprocessing import load_and_clean_data
def add_features(df):
    df['price_ma7'] = df['price'].rolling(window=7).mean()
    df['volume_ma7'] = df['volume'].rolling(window=7).mean()
    df['liquidation_ratio'] = df['volume'] / (df['volume'] + df['market_cap'] + 1e-9)
    df = df.dropna()
    return df

if __name__ == "__main__":
    data = laod_and_clean_data()
    data = add_features(data)
    print(data.head())

    