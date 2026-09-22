import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# ============================================
# 1. Load the logistics dataset
# ============================================

df = pd.read_csv(
    "DataCoSupplyChainDataset.csv.csv",
    encoding="latin-1"
)

print("Initial dataset shape:", df.shape)


# ============================================
# 2. Check missing values
# ============================================

print("\nTop 10 columns with missing values:")
print(
    df.isnull()
      .sum()
      .sort_values(ascending=False)
      .head(10)
)


# ============================================
# 3. Handle missing values
# ============================================

# Replace missing customer zipcode with "Unknown"
df['Customer Zipcode'] = df['Customer Zipcode'].fillna('Unknown')

# Replace missing customer last name with "Unknown"
df['Customer Lname'] = df['Customer Lname'].fillna('Unknown')

print("\nMissing values handled for selected columns.")


# ============================================
# 4. Check and remove duplicate rows
# ============================================

print("\nDuplicate rows before:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicate rows after:", df.duplicated().sum())


# ============================================
# 5. Convert date columns
# ============================================

df['order date (DateOrders)'] = pd.to_datetime(
    df['order date (DateOrders)']
)

df['shipping date (DateOrders)'] = pd.to_datetime(
    df['shipping date (DateOrders)']
)


# ============================================
# 6. Calculate delivery delay
# ============================================

df['delivery_delay_days'] = (
    df['shipping date (DateOrders)']
    - df['order date (DateOrders)']
).dt.days

print("\nDelivery delay calculated successfully.")


# ============================================
# 7. Detect outliers using IQR
# ============================================

Q1 = df['Benefit per order'].quantile(0.25)
Q3 = df['Benefit per order'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df['Benefit per order'] < lower_bound) |
    (df['Benefit per order'] > upper_bound)
]

print("\nIQR Outlier Detection:")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)
print("Number of outlier rows:", len(outliers))


# ============================================
# 8. Standardize text columns
# ============================================

df['Category Name'] = (
    df['Category Name']
    .str.strip()
    .str.title()
)

df['Customer Segment'] = (
    df['Customer Segment']
    .str.strip()
    .str.title()
)

print("\nText columns standardized successfully.")


# ============================================
# 9. Normalize numerical columns
# ============================================

scaler = MinMaxScaler()

df[['Sales_norm', 'ShippingDays_norm']] = scaler.fit_transform(
    df[['Sales', 'Days for shipping (real)']]
)

print("Normalization completed successfully.")


# ============================================
# 10. Final verification
# ============================================

print("\nFinal dataset shape:", df.shape)

print("\nMissing values in important columns:")
print(
    df[
        [
            'Customer Zipcode',
            'Customer Lname',
            'order date (DateOrders)',
            'shipping date (DateOrders)',
            'Benefit per order',
            'Category Name',
            'Customer Segment',
            'Sales',
            'Days for shipping (real)'
        ]
    ].isnull().sum()
)

print("\nDuplicate rows:", df.duplicated().sum())

print("\nNew columns added:")
print([
    'delivery_delay_days',
    'Sales_norm',
    'ShippingDays_norm'
])


# ============================================
# 11. Save the cleaned dataset
# ============================================

df.to_csv(
    "cleaned_logistics_data.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")

