import requests
from unittest.mock import patch

def get_data(url):
    response = requests.get(url)
    return response.json()

# Patching `requests.get` to mock the API call
with patch('requests.get') as mock_get:
    mock_get.return_value.json.return_value = {"key": "value"}

    result = get_data("http://example.com")

print(result)  # Output: {'key': 'value'}

"""

"""
