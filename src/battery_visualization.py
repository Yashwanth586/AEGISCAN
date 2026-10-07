import pandas as pd
import matplotlib.pyplot as plt

# Load battery data
df = pd.read_csv("data/battery_data.csv")

# Create time/sample values
df["Time_s"] = [0, 1, 2, 3, 4]

# Voltage vs Time
plt.figure()
plt.plot(df["Time_s"], df["Voltage_V"], marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Battery Voltage vs Time")
plt.grid(True)
plt.show()

# Current vs Time
plt.figure()
plt.plot(df["Time_s"], df["Current_A"], marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("Battery Current vs Time")
plt.grid(True)
plt.show()

# SOC vs Time
plt.figure()
plt.plot(df["Time_s"], df["SOC_percent"], marker="o")
plt.xlabel("Time (s)")
plt.ylabel("SOC (%)")
plt.title("Battery SOC vs Time")
plt.grid(True)
plt.show()

# Temperature vs Time
plt.figure()
plt.plot(df["Time_s"], df["Temperature_C"], marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Battery Temperature vs Time")
plt.grid(True)
plt.show()