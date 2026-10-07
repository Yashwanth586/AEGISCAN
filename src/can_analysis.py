import pandas as pd

# Load simulated CAN data
df = pd.read_csv("data/can_data.csv")

# Count how many times each CAN ID appears
can_id_counts = df["CAN_ID"].value_counts()

print("AegisCAN CAN ID Frequency Analysis")
print("-----------------------------------")
print(can_id_counts)

# Identify the most frequent CAN ID
most_frequent_id = can_id_counts.idxmax()
frequency = can_id_counts.max()

print("\nMost frequent CAN ID:", most_frequent_id)
print("Number of messages:", frequency)