# PANDAS INTERMEDIATE PROGRAMS
import pandas as pd
import numpy as np

print("--- Missing Values ---")
df = pd.DataFrame({"Name":["Ram","Shyam","Mohan"],"Marks":[85,np.nan,88]})
print(df.isnull())
df["Marks"].fillna(df["Marks"].mean(),inplace=True)
print(df)

print("--- Apply Function ---")
def grade(x):
    if x>=90: return 'A'
    elif x>=80: return 'B'
    else: return 'C'

df["Grade"] = df["Marks"].apply(grade)
print(df)

print("--- GroupBy ---")
df2 = pd.DataFrame({"Dept":["IT","IT","HR","HR"],"Salary":[50,60,45,40]})
print(df2.groupby("Dept").mean())

print("--- Merge ---")
a = pd.DataFrame({"ID":[1,2,3],"Name":["A","B","C"]})
b = pd.DataFrame({"ID":[1,2,3],"Marks":[90,80,70]})
print(pd.merge(a,b,on="ID"))

print("--- String Operations ---")
print(df["Name"].str.upper())
print(df["Name"].str.len())

print("--- Pivot Table ---")
pivot_df = pd.DataFrame({"Dept":["IT","IT","HR"],"Salary":[50,60,40]})
print(pivot_df.pivot_table(values="Salary",index="Dept",aggfunc="mean"))

print("Intermediate Pandas Completed!")

