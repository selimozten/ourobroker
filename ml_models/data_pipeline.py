import requests
import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self):
        self.dex_urls = [
            "https://dex1.api",
            "https://dex2.api"
        ]
        self.tokens = ["ETH", "DAI", "USDC"]

    def fetch_market_data(self):
        data_frames = []
        for url in self.dex_urls:
            for token in self.tokens:
                response = requests.get(f"{url}/market_data/{token}")
                if response.status_code == 200:
                    data = response.json()
                    df = pd.DataFrame(data)
                    data_frames.append(df)
        if data_frames:
            return pd.concat(data_frames)
        else:
            return pd.DataFrame()

    def preprocess_data(self, df):
        # Handle missing values
        df = df.fillna(method='ffill').fillna(method='bfill')
        # Normalize data
        normalized_df = (df - df.mean()) / df.std()
        return normalized_df

    def get_training_data(self):
        raw_data = self.fetch_market_data()
        if not raw_data.empty:
            processed_data = self.preprocess_data(raw_data)
            return processed_data.values
        else:
            return np.array([])

# Example usage
if __name__ == "__main__":
    loader = DataLoader()
    training_data = loader.get_training_data()
    print(f"Loaded training data of shape: {training_data.shape}")
