# AegisCAN Week 2 - Battery Energy Calculation

battery_voltage = 400.0
battery_capacity = 100.0

# Calculate battery energy
energy_wh = battery_voltage * battery_capacity
energy_kwh = energy_wh / 1000

print("AegisCAN Battery Energy Calculation")
print("------------------------------------")

print(f"Battery Voltage: {battery_voltage:.2f} V")
print(f"Battery Capacity: {battery_capacity:.2f} Ah")
print(f"Battery Energy: {energy_wh:.2f} Wh")
print(f"Battery Energy: {energy_kwh:.2f} kWh")