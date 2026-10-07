import pandas as pd

# Load simulated CAN attack data
df = pd.read_csv("data/can_attack_data.csv")

# Calculate message frequency for each CAN ID
can_id_counts = df["CAN_ID"].value_counts()

# Calculate time interval between messages
df["Time_Interval"] = df["Timestamp"].diff()

# Detection thresholds for this simulation
frequency_threshold = 5
timing_threshold = 0.001

print("AegisCAN CAN Attack Detection")
print("--------------------------------")

# Detect unusually frequent CAN IDs
suspicious_ids = can_id_counts[
    can_id_counts > frequency_threshold
]

if not suspicious_ids.empty:
    print("\n⚠️ Suspicious CAN IDs detected:")

    for can_id, count in suspicious_ids.items():
        print(f"{can_id} → {count} messages")

else:
    print("\nNo unusually frequent CAN IDs detected.")

# Detect very short message intervals
short_intervals = df[
    df["Time_Interval"] < timing_threshold
]

if not short_intervals.empty:
    print("\n⚠️ Suspicious high-frequency traffic detected!")
    print(
        f"Number of short intervals: {len(short_intervals)}"
    )

else:
    print("\nNo unusually short message intervals detected.")

print("\nDetection analysis completed.")