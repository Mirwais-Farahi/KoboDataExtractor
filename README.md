# Kobo Data Extractor
- The Kobo Data Extractor is a Python module designed to automate the process of downloading data from KoboToolbox into pandas DataFrames. It simplifies the retrieval and normalization of data collected via KoboToolbox forms, facilitating seamless integration into data analysis pipelines. Ideal for researchers and organizations leveraging KoboToolbox for data collection, the module enhances efficiency in data handling and analysis tasks.

## Key Features:
1. Automated Data Retrieval: Fetches data from KoboToolbox using API requests.
2. Data Normalization: Converts JSON-formatted data into structured pandas DataFrames.
3. Flexible Integration: Supports customization with query parameters for tailored data extraction.

## Installation:
```
!pip install --upgrade git+https://github.com/mirwais-farahi/KoboDataExtractor.git

```
## Usage:
```
from KoboDataExtractor.extractor import KoboDataExtractor

# Example usage
api_token = 'your_api_token'
base_url = 'https://your_kobo_url.com'
form_uid = 'your_form_uid'

kobo_extractor = KoboDataExtractor(api_token, base_url)
data_df = kobo_extractor.get_data(form_uid)

# Process data_df as needed
print(data_df.head())
```

- get_data method has the following format of arguments: get_data(form_uid, query, start, limit, submitted_after)

The number of downloaded results is available in ``data_df['count']``.
'''
data_df = kobo_extractor.sort_results_by_time(data_df['results'])
'''

Download all responses submitted after a certain point in time:

```
data_df = kobo_extractor.get_data(asset_uid, submitted_after='2020-05-20T17:29:30')
```