import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 95, 80]}
df=pd.DataFrame(data)
sorted_df=df.sort_values(by='Age')
print(sorted_df)

#sort for index
#df_sorted=df.sort_index()
print(df_sorted_byindex)
      