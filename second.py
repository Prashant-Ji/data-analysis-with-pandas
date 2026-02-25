import numpy as np
import pandas as pd
import random

ser = pd.Series(np.random.randint(1, 100, 10))
print(ser)

print(type(ser))

newdf = pd.DataFrame(np.random.rand(5, 4), columns=['A', 'B', 'C', 'D'])
# print(newdf) 
print(type(newdf))
print(newdf['A'])  # Accessing a column

print(newdf.index)  # Accessing the index of the DataFrame
print(newdf.columns)  # Accessing the columns of the DataFrame

newdf.to_numpy()  # Convert the DataFrame to a NumPy array
print(newdf.to_numpy())

newdf1 = newdf.copy()  # Create a copy of the DataFrame
print(newdf1)


newdf.T  # Transpose the DataFrame
print(newdf.T)

print(newdf.sort_index(axis=0, ascending=True))  # Sort the DataFrame by index in descending order

print(newdf.iloc[0])  # Accessing the first row using iloc
print(newdf.iloc[0, 3])  # Accessing a specific value using il
print(newdf.iloc[0:2, 0:2])  # Accessing a subset of the DataFrame using iloc

print(newdf.drop(0, axis=0))  # Dropping a row from the DataFrame
print(newdf.reset_index(drop=True))  # Resetting the index of the DataFrame

newdf["Passed"] = True  # Adding a new column to the DataFrame with a default value
newdf["Bonus"] = newdf["A"] + 5  # Adding a new column to the DataFrame based on existing columns

#Please explore some more functions and methods of pandas to enhance your understanding. Happy coding!