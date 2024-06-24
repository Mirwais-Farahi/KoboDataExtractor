# main.py

from kobo_data_module import KoboDataFetcher

def main():
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

if __name__ == "__main__":
    main()
