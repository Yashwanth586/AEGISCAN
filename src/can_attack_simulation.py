import pandas as pd

# Normal CAN traffic
normal_traffic = [
    [0.001, "0x180", 8, "19002C014B000000"],
    [0.004, "0x200", 8, "2A00100000000000"],
    [0.007, "0x180", 8, "1A002D014C000000"],
    [0.010, "0x300", 8, "0F00150000000000"],
    [0.013, "0x180", 8, "1B002E014D000000"],
]

# Simulated high-frequency suspicious traffic
attack_traffic = [
    [0.0131, "0x666", 8, "FFFFFFFFFFFFFFFF"],
    [0.0132, "0x666", 8, "FFFFFFFFFFFFFFFF"],
    [0.0133, "0x666", 8, "FFFFFFFFFFFFFFFF"],
    [0.0134, "0x666", 8, "FFFFFFFFFFFFFFFF"],
    [0.0135, "0x666", 8, "FFFFFFFFFFFFFFFF"],
    [0.0136, "0x666", 8, "FFFFFFFFFFFFFFFF"],
    [0.0137, "0x666", 8, "FFFFFFFFFFFFFFFF"],
    [0.0138, "0x666", 8, "FFFFFFFFFFFFFFFF"],
]

# Combine normal and suspicious traffic
all_traffic = normal_traffic + attack_traffic

df = pd.DataFrame(
    all_traffic,
    columns=["Timestamp", "CAN_ID", "DLC", "Data"]
)

print("AegisCAN Simulated Attack Traffic")
print("---------------------------------")
print(df)

# Save attack dataset
df.to_csv("data/can_attack_data.csv", index=False)

print("\nAttack simulation data saved successfully!")