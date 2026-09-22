import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Load and inspect data
df = pd.read_csv("DataCoSupplyChainDataset.csv", encoding="latin-1")

print("Dataset shape:", df.shape)
print(df.info())
print(df.isnull().sum().sort_values(ascending=False).head(10))

# 2. Handle missing values
df["Customer Zipcode"] = df["Customer Zipcode"].fillna("Unknown")

df["Order Item Discount"] = df["Order Item Discount"].fillna(
    df["Order Item Discount"].median()
)

# 3. Remove duplicates
print("Duplicate rows before:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicate rows after:", df.duplicated().sum())

# 4. Correct data types
df["order date (DateOrders)"] = pd.to_datetime(
    df["order date (DateOrders)"]
)

df["shipping date (DateOrders)"] = pd.to_datetime(
    df["shipping date (DateOrders)"]
)

df["delivery_delay_days"] = (
    df["shipping date (DateOrders)"]
    - df["order date (DateOrders)"]
).dt.days

# 5. Detect outliers using IQR
Q1 = df["Benefit per order"].quantile(0.25)
Q3 = df["Benefit per order"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Benefit per order"] < lower_bound)
    | (df["Benefit per order"] > upper_bound)
]

print("Number of outlier rows:", len(outliers))

# 6. Standardize categorical text
df["Category Name"] = (
    df["Category Name"].str.strip().str.title()
)

df["Customer Segment"] = (
    df["Customer Segment"].str.strip().str.title()
)

# 7. Normalize numerical variables
scaler = MinMaxScaler()

df[["Sales_norm", "ShippingDays_norm"]] = scaler.fit_transform(
    df[["Sales", "Days for shipping (real)"]]
)

# 8. Save cleaned dataset
df.to_csv("cleaned_logistics_data.csv", index=False)

print("Preprocessing completed successfully.")
