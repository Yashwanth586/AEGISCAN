import pandas as pd

# Simulated CAN bus traffic
can_data = {
    "Timestamp": [0.001, 0.004, 0.006, 0.009, 0.012, 0.015, 0.018, 0.021],
    "CAN_ID": [
        "0x180",
        "0x200",
        "0x180",
        "0x300",
        "0x180",
        "0x200",
        "0x180",
        "0x300"
    ],
    "DLC": [8, 8, 8, 8, 8, 8, 8, 8],
    "Data": [
        "19002C014B000000",
        "2A00100000000000",
        "1A002D014C000000",
        "0F00150000000000",
        "1B002E014D000000",
        "2B00110000000000",
        "1C002F014E000000",
        "1000160000000000"
    ]
}

# Create a DataFrame
df = pd.DataFrame(can_data)

# Display CAN traffic
print("AegisCAN Simulated CAN Traffic")
print(df)

# Save the CAN traffic to a CSV file
df.to_csv("data/can_data.csv", index=False)

print("\nCAN data saved successfully!")