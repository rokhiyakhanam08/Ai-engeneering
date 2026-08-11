import pandas as pd

df = pd.read_csv("people_data.csv")
df = pd.read_csv("people_data.csv", na_values=["N/A", "Unknown"])
print(df)