import pandas as pd

# Load the dataset
df = pd.read_csv("drilling_operations_data.csv")

# Display the first 5 records
print("📌 First 5 records of the dataset:")
print(df.head())

# Check for missing values
print("\n🔍 Checking for missing values:")
print(df.isnull().sum())

# Check data types
print("\n🔍 Checking data types:")
print(df.dtypes)

# Check for duplicate records
print("\n🔍 Checking for duplicates:", df.duplicated().sum())

# Remove duplicate records (if any)
df = df.drop_duplicates()

# Handle missing values
df.fillna(df.median(numeric_only=True), inplace=True)  # Fill numeric missing values with median
df["Weather_Condition"].fillna(df["Weather_Condition"].mode()[0], inplace=True)  # Fill categorical missing values

# Save cleaned dataset
df.to_csv("cleaned_drilling_operations_data.csv", index=False)

print("\n✅ Cleaned dataset saved as 'cleaned_drilling_operations_data.csv'!")
