import pandas as pd

df = pd.read_csv("people_data.csv")

print(df)
#the data file name and the name u mentoned in the code should be the same



#specific colums from the csv file 
df = pd.read_csv("people_data.csv", usecols=["First Name", "Email"])
print(df)

#2. Setting an Index Column (index_col)

df = pd.read_csv("people_data.csv", index_col="First Name")
print(df)