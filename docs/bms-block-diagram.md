
# AEGISCAN - BMS Block Diagram

## Block Diagram

```text
          +----------------------+
          |     Battery Pack     |
          |  Cells / Modules     |
          +----------+-----------+
                     |
                     v
          +----------------------+
          |  Sensing & Data      |
          |  Acquisition         |
          | Voltage, Current,    |
          | Temperature          |
          +----------+-----------+
                     |
                     v
          +----------------------+
          |    BMS Controller    |
          | SOC / SOH Estimation |
          | Fault Diagnosis      |
          +----------+-----------+
                     |
          +----------+-----------+
          |                      |
          v                      v
+------------------+   +------------------+
|    Protection    |   | Cell Balancing   |
| OV / UV / OC /   |   | Voltage / SOC    |
| Overtemperature  |   | Equalization     |
+--------+---------+   +------------------+
          |
          v
+--------------------------+
| Control and Safety       |
| Contactor / Power Limits |
| Fault Logging            |
+------------+-------------+
             |
             v
+--------------------------+
| CAN Communication        |
| Vehicle ECU / Charger    |
| / Other Controllers      |
+--------------------------+
```

## Explanation

1. **Battery pack:** Stores electrical energy in cells and modules.
2. **Sensing:** Measures cell voltage, pack voltage, current, and temperature.
3. **BMS controller:** Processes measurements and estimates SOC and SOH.
4. **Protection:** Detects abnormal conditions such as overvoltage, undervoltage, overcurrent, and overtemperature.
5. **Cell balancing:** Reduces differences between cells.
6. **Control:** Applies the required response, including contactor control and operating limits.
7. **CAN communication:** Exchanges battery status and fault information with other controllers.

Note: This is a simplified conceptual diagram. Actual BMS architectures vary by design.
