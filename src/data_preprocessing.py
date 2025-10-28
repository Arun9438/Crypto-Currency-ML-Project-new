import pandas as pd

def load_and_clean_data(file_path):
    df1 = pd.read_csv(r"C:\Users\LE NO VO\Desktop\Asignments\Crypto Currency ML Project\Data\coin_gecko_2022-03-16.csv")
    df2 = pd.read_csv(r"C:\Users\LE NO VO\Desktop\Asignments\Crypto Currency ML Project\Data\coin_market_cap_2022-03-17.csv")
    df = pd.concatenate([df1, df2], ignore_index=True)
    df = df.dropna()
    df = df.apply(pd.to_numeric, errors='ignore')
    return df

if __name__ == "__main__":
    data = load_and_clean_data()
    print(data.head())