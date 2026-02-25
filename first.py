import numpy as np
import pandas as pd

dict = {'Name': ['Rohit', 'Anna', 'Neha', 'Prashant'],
        'Age': [28, 24, 35, 21],
        'City': ['Rajasthan', 'Tamil Nadu', 'Uttar Pradesh', 'Delhi']}

df = pd.DataFrame(dict)
print(df)

# convert the DataFrame to a CSV file without the index column
df.to_csv('data.csv', index=False)

# Read the CSV file back into a DataFrame
read_df = pd.read_csv('data.csv')
print(read_df)

# Syntax for accessing a column in a DataFrame 
print(read_df['Age'])

# Syntax for accessing a specific value in a DataFrame using the column name and row index
print(read_df['Age'][0])  # Output: 28

# read_df.loc[0, 'Age'] = 29
print(read_df['Age'][0])  # Output: 29


