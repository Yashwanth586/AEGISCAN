# AegisCAN Week 2 - Battery Charging and Discharging Simulation

soc = 50.0
temperature = 30.0

print("AegisCAN Battery Charging and Discharging")
print("------------------------------------------")

# Charging simulation
print("\nCharging:")
for step in range(5):
    soc += 5
    temperature += 0.5
    print(
        f"Step {step + 1}: "
        f"SOC = {soc:.1f}%, "
        f"Temperature = {temperature:.1f} C"
    )

# Discharging simulation
print("\nDischarging:")
for step in range(5):
    soc -= 5
    temperature += 0.3
    print(
        f"Step {step + 1}: "
        f"SOC = {soc:.1f}%, "
        f"Temperature = {temperature:.1f} C"
    )

# Basic battery safety checks
print("\nBattery Safety Checks")
print("---------------------")

voltage = 400.0
current = 120.0

if voltage > 450:
    print("WARNING: Over-voltage detected!")
else:
    print("Voltage: Normal")

if voltage < 300:
    print("WARNING: Under-voltage detected!")
else:
    print("Voltage: Safe")

if temperature > 60:
    print("WARNING: High temperature detected!")
else:
    print("Temperature: Safe")

if current > 200:
    print("WARNING: Excessive current detected!")
else:
    print("Current: Safe")

print("\nBattery charging, discharging and safety simulation completed.")