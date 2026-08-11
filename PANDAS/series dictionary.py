import pandas as pd

data_dict = {'Geeks': 10, 'for': 20, 'geeks': 30}

ser = pd.Series(data_dict)
print(ser)