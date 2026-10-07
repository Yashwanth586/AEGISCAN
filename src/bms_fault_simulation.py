# AegisCAN Week 3 - BMS Fault Simulation

from bms_model import BMS


print("AegisCAN BMS Fault Simulation")
print("=============================")

# Create a normal BMS
bms = BMS()

print("\n--- NORMAL OPERATION ---")

bms.sense_parameters()
bms.check_protection()
bms.check_cell_balance()
bms.control_contactor()
bms.display_status()


# Simulate an over-temperature fault
print("\n--- SIMULATED FAULT ---")

bms.temperature = 75.0

print(f"Temperature increased to: {bms.temperature:.2f} °C")

# Run BMS protection logic again
bms.check_protection()
bms.control_contactor()

print("\nFault Detection Result")
print("----------------------")
print(f"Fault State: {bms.fault_state}")

if bms.fault_state == "OVER_TEMPERATURE":
    print("WARNING: Over-temperature fault detected!")
    print("Safety action: Contactor OPEN")
else:
    print("No fault detected.")

bms.display_status()