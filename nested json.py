import json  
import pandas as pd  
from pandas import json_normalize  

with open('/content/raw_nyc_phil.json') as f:
    d = json.load(f)

nycphil = json_normalize(d['programs'])
nycphil.head(3)

# json.load(f): Loads the raw JSON into a Python dictionary.
# json_normalize(d['programs']): Extracts the list under the programs key and flattens it into columns.