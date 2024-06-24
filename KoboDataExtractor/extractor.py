# kobo_data_module.py

import requests
import pandas as pd
import time

class KoboDataFetcher:
    def __init__(self, base_url, api_token, asset_uid, limit=100000):
        self.base_url = base_url.format(asset_uid=asset_uid)
        self.api_token = api_token
        self.asset_uid = asset_uid
        self.limit = limit
        self.data = []

    def get_kobo_data(self, url, params=None):
        headers = {
            'Authorization': f'Token {self.api_token}'
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Request error occurred: {err}")
            return None

    def fetch_data(self):
        params = {
            'format': 'json',
            'limit': self.limit,  # User-defined limit
        }
        
        try:
            # Fetch the initial page
            response_data = self.get_kobo_data(self.base_url, params)
            if response_data:
                self.data.extend(response_data['results'])

                # Handle pagination
                while response_data.get('next'):
                    response_data = self.get_kobo_data(response_data['next'])
                    if response_data:
                        self.data.extend(response_data['results'])
                    time.sleep(0.5)  # Be kind to the API server

            # Convert to a pandas DataFrame
            df = pd.DataFrame(self.data)

            # Clean up column names
            df.columns = [col.split('/')[-1] for col in df.columns]

            return df
        
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

# Example usage of the module
if __name__ == "__main__":
    # Prompt user to input base URL, API token, asset UID, and limit
    base_url = input("Enter KoboToolbox base URL (e.g., https://eu.kobotoolbox.org/api/v2/assets/{asset_uid}/data/): ").strip()
    api_token = input("Enter your KoboToolbox API token: ").strip()
    asset_uid = input("Enter your KoboToolbox asset UID: ").strip()
    limit = input("Enter limit for number of records (default is 100,000): ").strip()
    limit = int(limit) if limit else 100000  # Convert to integer, default to 100,000 if empty input

    # Create instance of KoboDataFetcher
    kobo_fetcher = KoboDataFetcher(base_url, api_token, asset_uid, limit)
    df = kobo_fetcher.fetch_data()

    if df is not None:
        print("Data fetched successfully:")
        print(df.head())
    else:
        print("Failed to fetch data.")
