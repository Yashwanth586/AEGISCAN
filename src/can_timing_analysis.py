import pandas as pd

# Load simulated CAN data
df = pd.read_csv("data/can_data.csv")

# Calculate time difference between consecutive messages
df["Time_Interval"] = df["Timestamp"].diff()

print("AegisCAN CAN Message Timing Analysis")
print("-------------------------------------")
print(df[["Timestamp", "CAN_ID", "Time_Interval"]])

# Calculate average message interval
average_interval = df["Time_Interval"].dropna().mean()

print("\nAverage message interval:")
print(f"{average_interval:.6f} seconds")