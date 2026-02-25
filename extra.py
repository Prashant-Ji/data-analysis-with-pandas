import pandas as pd
import numpy as np

data = {
    "OrderID":[101,102,103,104,105,106,107,108],
    "City":["Delhi","Delhi","Mumbai","Mumbai","Delhi","Chennai","Chennai","Mumbai"],
    "Product":["Laptop","Mouse","Laptop","Keyboard","Keyboard","Mouse","Laptop","Mouse"],
    "Category":["Electronics","Accessories","Electronics","Accessories","Accessories","Accessories","Electronics","Accessories"],
    "Price":[70000,800,72000,1500,1800,900,68000,850],
    "Quantity":[1,2,1,3,2,4,1,5],
    "Date":pd.to_datetime([
        "2024-01-01","2024-01-02","2024-01-03","2024-01-04",
        "2024-01-05","2024-01-06","2024-01-07","2024-01-08"
    ])
}

df = pd.DataFrame(data)
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)


# Total revenue city wise
city_sales = df.groupby("City")["Revenue"].sum()
print(city_sales)

summary = df.groupby("Product").agg({
    "Revenue":"sum",
    "Quantity":"mean",
    "Price":"max"
})
print(summary)


multi_group = df.groupby(["City","Category"])["Revenue"].sum()
print(multi_group)


city_sales = df.groupby("City", as_index=False)["Revenue"].sum()
print(city_sales)


# Add column: percentage contribution of each order in its city
df["City_Total"] = df.groupby("City")["Revenue"].transform("sum")
df["Percent_Contribution"] = df["Revenue"] / df["City_Total"] * 100
print(df)


customers = pd.DataFrame({
    "City":["Delhi","Mumbai","Chennai"],
    "Manager":["Amit","Rahul","Suresh"]
})


merged = pd.merge(df, customers, on="City", how="inner")
print("\nMerged DataFrame (inner join):")
print(merged)

merged = pd.merge(df, customers, on="City", how="left")
print("\nMerged DataFrame (left join):")
print(merged)

merged = pd.merge(df, customers, on="City", how="right")
print(merged)

merged = pd.merge(df, customers, on="City", how="outer")
print(merged)

pd.merge(df, customers, left_on="City", right_on="City")
print(merged)


df = df.sort_values("Date")

df["3_day_avg"] = df["Revenue"].rolling(window=3).mean()
print(df[["Date","Revenue","3_day_avg"]])

df["rolling_sum"] = df["Revenue"].rolling(3).sum()
print(df[["Date","Revenue","rolling_sum"]])

df["Rank"] = df["Revenue"].rank(ascending=False)
print(df[["Date","Revenue","Rank"]])

df["Dense_Rank"] = df["Revenue"].rank(method="dense", ascending=False)
print(df[["Date","Revenue","Dense_Rank"]])





