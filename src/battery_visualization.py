import pandas as pd
import matplotlib.pyplot as plt

# Load battery data
df = pd.read_csv("data/battery_data.csv")

# Plot SOC and SOH
plt.plot(
    df.index,
    df["SOC_percent"],
    marker="o",
    label="SOC (%)"
)

plt.plot(
    df.index,
    df["SOH_percent"],
    marker="o",
    label="SOH (%)"
)

plt.xlabel("Sample")
plt.ylabel("Percentage (%)")
plt.title("AegisCAN Battery SOC and SOH")
plt.legend()
plt.grid(True)

plt.show()