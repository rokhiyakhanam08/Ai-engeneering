import pandas as pd
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

data = pd.json_normalize(response.json())
print(data.head(10))

# requests.get(url) fetches data from the URL.
# response.json() converts response to a Python dictionary/list.
# json_normalize() converts nested JSON into a flat table.