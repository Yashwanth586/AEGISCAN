# AegisCAN Week 2 - Battery Series and Parallel Configuration

cell_voltage = 3.7
cell_capacity = 2.0

series_cells = 3
parallel_cells = 3

# Series configuration
series_voltage = cell_voltage * series_cells
series_capacity = cell_capacity

# Parallel configuration
parallel_voltage = cell_voltage
parallel_capacity = cell_capacity * parallel_cells

print("AegisCAN Battery Configuration")
print("--------------------------------")

print("\nSeries Configuration")
print(f"Number of cells: {series_cells}")
print(f"Pack Voltage: {series_voltage:.2f} V")
print(f"Pack Capacity: {series_capacity:.2f} Ah")

print("\nParallel Configuration")
print(f"Number of cells: {parallel_cells}")
print(f"Pack Voltage: {parallel_voltage:.2f} V")
print(f"Pack Capacity: {parallel_capacity:.2f} Ah")