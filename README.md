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
from kobo_data_extractor.extractor import KoboDataExtractor

# Example usage
api_token = 'your_api_token'
base_url = 'https://your_kobo_url.com'
form_uid = 'your_form_uid'

kobo_extractor = KoboDataExtractor(api_token, base_url)
data_df = kobo_extractor.get_data(form_uid)

# Process data_df as needed
print(data_df.head())
```
