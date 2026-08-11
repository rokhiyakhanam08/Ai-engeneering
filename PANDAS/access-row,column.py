import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
# Display the entire DataFrame
print(df)


age_column =df['Age']  
print(age_column)

age_rows=df.loc[1]
print(age_rows)

# Access rows where 'Age' is greater than 25
filtered_data = df[df['Age']>25]
print(filtered_data)