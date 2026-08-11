import pandas as pd
data={'name':['jack','jill','john','jane'],
      'age':[23,34,45,56],
      'salary':[50000,60000,70000,80000]}
df=pd.DataFrame(data)
res=df.set_index('name') #set_index is used to change the index of a dataframe by setting one oor more column
res=df.reset_index()  #reset_index is used to reset the index back to default integerindex.
row=df.loc[['alice']] # loc is used to access the rows and columns of a dataframe using their labels 

print(row)
print(res)