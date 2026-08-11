import pandas as pd
nme = ["Aparna", "Pankaj", "Sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
data = {'Name': nme, 'Degree': deg, 'Score': scr}
df = pd.DataFrame(data)

df
df.to_csv('file1.csv')