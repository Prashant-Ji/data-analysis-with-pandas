# PANDAS BASIC SYNTAX

import pandas as pd
import numpy as np

print("--- Create Series & DataFrame ---")
s = pd.Series([10,20,30,40])
print(s)

data = {"Name":["Ram","Shyam","Mohan"],"Age":[20,21,19],"Marks":[85,90,88]}
df = pd.DataFrame(data)
print(df)

print("--- View Data ---")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)

print("--- Selection ---")
print(df["Name"])
print(df.iloc[0])
print(df.loc[0:1,"Name":"Marks"])

print("--- Filtering ---")
print(df[df["Marks"]>85])

print("--- Add/Delete Column ---")
df["Bonus"] = df["Marks"]+5
print(df)
df.drop("Bonus",axis=1,inplace=True)

print("--- Sorting ---")
print(df.sort_values("Marks"))

print("--- Value Counts ---")
print(df["Age"].value_counts())

print("Basic Pandas Completed!")
