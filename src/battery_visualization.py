
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Project root and output directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "battery_data.csv"
PLOT_DIR = PROJECT_ROOT / "outputs" / "plots"
PLOT_DIR.mkdir(parents=True, exist_ok=True)

# Load battery data
df = pd.read_csv(DATA_FILE)
df["Time_s"] = range(len(df))

# Plot definitions
plots = [
    ("Voltage_V", "Voltage (V)", "Battery Voltage vs Time", "battery_voltage.png"),
    ("Current_A", "Current (A)", "Battery Current vs Time", "battery_current.png"),
    ("SOC_percent", "SOC (%)", "Battery SOC vs Time", "battery_soc.png"),
    ("Temperature_C", "Temperature (°C)", "Battery Temperature vs Time", "battery_temperature.png"),
]

# Generate and save all plots
for column, ylabel, title, filename in plots:
    plt.figure(figsize=(8, 5))
    plt.plot(df["Time_s"], df[column], marker="o")
    plt.xlabel("Time (s)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(PLOT_DIR / filename, dpi=150)
    plt.show()
    plt.close()

print(f"All four battery plots saved to: {PLOT_DIR}")
