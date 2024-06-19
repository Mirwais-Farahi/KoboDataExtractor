import requests
import pandas as pd
from koboextractor import KoboExtractor

class KoboDataExtractor:
    def __init__(self, api_token, base_url):
        self.kobo = KoboExtractor(api_token, base_url)

    def get_data(self, form_uid, query=None, start=None, limit=None, submitted_after=None):
        data = self.kobo.get_data(form_uid, query, start, limit, submitted_after)
        if data:
            df = pd.json_normalize(data['results'])
            return df
        else:
            return None