import requests
import pandas as pd

class KoboExtractor:
    def __init__(self, api_token, base_url):
        self.api_token = api_token
        self.base_url = base_url

    def get_data(self, form_uid, query=None, start=None, limit=None, submitted_after=None):
        headers = {
            'Authorization': f'Token {self.api_token}'
        }
        url = f'{self.base_url}/data/{form_uid}.json'
        
        params = {
            'format': 'json'
        }
        
        if query:
            params['query'] = query
        if start:
            params['start'] = start
        if limit:
            params['limit'] = limit
        if submitted_after:
            params['submitted_after'] = submitted_after

        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    def get_dataframe(self, form_uid, query=None, start=None, limit=None, submitted_after=None):
        data = self.get_data(form_uid, query, start, limit, submitted_after)
        if data:
            return pd.json_normalize(data['results'])
        else:
            return pd.DataFrame()
