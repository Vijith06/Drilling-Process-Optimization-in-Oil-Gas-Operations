import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_drilling_operations_data.csv")

# Calculate Total Time and Drilling Efficiency
df["Total_Time_Hours"] = df["Setup_Time_Hours"] + df["Drilling_Time_Hours"] + df["Maintenance_Time_Hours"]
df["Drilling_Efficiency"] = df["Drilling_Time_Hours"] / df["Total_Time_Hours"]

# Display efficiency statistics
print("\n📊 Drilling Efficiency Statistics:")
print(df["Drilling_Efficiency"].describe())

# Visualize Drilling Efficiency Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Drilling_Efficiency"], bins=20, kde=True, color="blue")
plt.title("Drilling Efficiency Distribution")
plt.xlabel("Drilling Efficiency")
plt.ylabel("Frequency")
plt.show()

# Analyze Efficiency by Weather Condition
plt.figure(figsize=(8, 5))
sns.boxplot(x="Weather_Condition", y="Drilling_Efficiency", data=df, palette="Set2")
plt.title("Drilling Efficiency by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Drilling Efficiency")
plt.xticks(rotation=45)
plt.show()

# Analyze Efficiency by Terrain Type
plt.figure(figsize=(8, 5))
sns.boxplot(x="Terrain_Type", y="Drilling_Efficiency", data=df, palette="Set1")
plt.title("Drilling Efficiency by Terrain Type")
plt.xlabel("Terrain Type")
plt.ylabel("Drilling Efficiency")
plt.xticks(rotation=45)
plt.show()

# Save the updated dataset
df.to_csv("optimized_drilling_data.csv", index=False)

print("\n✅ Drilling efficiency analysis complete! Data saved as 'optimized_drilling_data.csv'")
