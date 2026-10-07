import pandas as pd

# Simulated EV battery data
battery_data = {
    "Voltage_V": [400, 398, 402, 401, 399],
    "Current_A": [50, 52, 48, 51, 49],
    "Temperature_C": [32, 33, 34, 32, 35],
    "SOC_percent": [75, 73, 71, 69, 67],
    "SOH_percent": [98, 98, 97, 97, 96]
}

# Create a DataFrame
df = pd.DataFrame(battery_data)

# Display the battery data
print("AegisCAN Battery Data")
print(df)

# Save the data as a CSV file
df.to_csv("data/battery_data.csv", index=False)

print("\nBattery data saved successfully!")