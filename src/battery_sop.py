# AegisCAN Week 2 - Battery State of Power (SOP)

battery_voltage = 400.0
maximum_current = 150.0

# Calculate maximum available power
maximum_power_w = battery_voltage * maximum_current
maximum_power_kw = maximum_power_w / 1000

print("AegisCAN Battery State of Power")
print("---------------------------------")

print(f"Battery Voltage: {battery_voltage:.2f} V")
print(f"Maximum Safe Current: {maximum_current:.2f} A")
print(f"Available Power: {maximum_power_w:.2f} W")
print(f"Available Power: {maximum_power_kw:.2f} kW")