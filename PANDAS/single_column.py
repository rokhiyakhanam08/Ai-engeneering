#1. Selecting a Single Row by Label
import pandas as pd

data = pd.read_csv("nba.csv", index_col="Name")

print("Dataset")
print(data.head(5))

first = data["Age"]
print("\nSingle Column selected from Dataset")
print(first.head(5))

#To select multiple rows, pass a list of labels:
first = data[["Age", "College", "Salary"]]
print("\nMultiple Columns selected from Dataset")
print(first.head(5))


#3. Selecting Specific Rows and Columns
selection = data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]]
print(selection)




