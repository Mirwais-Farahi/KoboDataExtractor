import unittest
from unittest.mock import patch
import pandas as pd
from koboextractor import KoboExtractor
from KoboDataExtractor.extractor import KoboDataExtractor

class TestKoboDataExtractor(unittest.TestCase):
    def setUp(self):
        self.api_token = 'your_api_token'
        self.base_url = 'https://your_kobo_url.com'
        self.form_uid = 'your_form_uid'
        self.kobo_extractor = KoboDataExtractor(self.api_token, self.base_url)

    def test_get_data_with_data(self):
        # Mock the KoboExtractor.get_data method to return a dictionary with 'results' key
        with patch.object(KoboExtractor, 'get_data', return_value={'results': [{'key': 'value'}]}):
            data_df = self.kobo_extractor.get_data(self.form_uid)
            self.assertIsInstance(data_df, pd.DataFrame)
            self.assertEqual(data_df.shape[0], 1)
            self.assertEqual(data_df.shape[1], 1)

    def test_get_data_without_data(self):
        # Mock the KoboExtractor.get_data method to return None
        with patch.object(KoboExtractor, 'get_data', return_value=None):
            data_df = self.kobo_extractor.get_data(self.form_uid)
            self.assertIsNone(data_df)

if __name__ == '__main__':
    unittest.main()