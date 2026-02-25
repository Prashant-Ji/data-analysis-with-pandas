# PANDAS ADVANCED CONCEPTS

import pandas as pd
import numpy as np

print("--- Vectorization ---")
df = pd.DataFrame({"Salary":[100,200,300,400]})
df["Tax"] = df["Salary"]*0.1
print(df)

print("--- Map / Replace ---")
df2 = pd.DataFrame({"Dept":["IT","HR","IT","Sales"]})
df2["Dept"] = df2["Dept"].map({"IT":"Tech","HR":"Human","Sales":"Business"})
print(df2)

print("--- MultiIndex ---")
arrays = [["A","A","B","B"],[1,2,1,2]]
index = pd.MultiIndex.from_arrays(arrays,names=("letter","number"))
mdf = pd.DataFrame({"value":[10,20,30,40]},index=index)
print(mdf.loc["A"])

print("--- Rolling Window ---")
sales = pd.Series([10,20,30,40,50])
print(sales.rolling(3).mean())

print("--- Binning ---")
ages = pd.Series([10,18,25,35,60])
print(pd.cut(ages,bins=[0,18,30,60],labels=["Teen","Adult","Senior"]))

print("--- Query ---")
df3 = pd.DataFrame({"Marks":[70,85,95,60]})
print(df3.query("Marks>80"))

print("--- Time Series Resample ---")
dates = pd.date_range("2024-01-01",periods=5)
tdf = pd.DataFrame({"Date":dates,"Sales":[10,20,30,40,50]})
tdf.set_index("Date",inplace=True)
print(tdf.resample('ME').sum())

print("--- Groupby Transform ---")
df4 = pd.DataFrame({"Dept":["IT","IT","HR","HR"],"Salary":[50,60,45,40]})
df4["Avg"] = df4.groupby("Dept")["Salary"].transform("mean")
print(df4)

print("Advanced Pandas Completed!")
