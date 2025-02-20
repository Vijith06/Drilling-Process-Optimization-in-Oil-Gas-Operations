import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_drilling_operations_data.csv")

# Display basic statistics
print("\n📊 Basic Statistics:")
print(df.describe())

# Count of records per Weather Condition
plt.figure(figsize=(8, 5))
sns.countplot(x="Weather_Condition", data=df, palette="Set2")
plt.title("Weather Condition Distribution")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Count of records per Terrain Type
plt.figure(figsize=(8, 5))
sns.countplot(x="Terrain_Type", data=df, palette="Set1")
plt.title("Terrain Type Distribution")
plt.xlabel("Terrain Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Between Numerical Features")
plt.show()
