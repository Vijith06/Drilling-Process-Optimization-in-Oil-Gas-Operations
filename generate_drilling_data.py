import pandas as pd
import numpy as np
import random

# Define the number of records
num_records = 500

# Define categories for weather and terrain
weather_conditions = ["Clear", "Rain", "Storm", "Foggy"]
terrain_types = ["Rocky", "Sandy", "Clay", "Mixed"]

# Generate random data
data = {
    "Drilling_ID": np.arange(1, num_records + 1),
    "Setup_Time_Hours": np.random.randint(2, 10, num_records),
    "Drilling_Time_Hours": np.random.randint(20, 100, num_records),
    "Maintenance_Time_Hours": np.random.randint(5, 30, num_records),
    "Equipment_MTBF_Hours": np.random.randint(100, 500, num_records),
    "Worker_Shift_Hours": np.random.randint(6, 12, num_records),
    "Worker_Efficiency_Score": np.round(np.random.uniform(60, 100, num_records), 2),
    "Supply_Delivery_Days": np.random.randint(1, 15, num_records),
    "Weather_Condition": [random.choice(weather_conditions) for _ in range(num_records)],
    "Terrain_Type": [random.choice(terrain_types) for _ in range(num_records)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV file
df.to_csv("drilling_operations_data.csv", index=False)

print("✅ Synthetic dataset 'drilling_operations_data.csv' created successfully!")
