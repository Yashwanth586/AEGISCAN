
# AEGISCAN - BESS Architecture Diagram

## Architecture

```text
      +----------------------------+
      | Grid / Solar / Wind Source |
      +-------------+--------------+
                    |
                    v
      +----------------------------+
      | PCS - Power Conversion     |
      | System (AC / DC)           |
      +-------------+--------------+
                    |
                    v
      +----------------------------+
      | Battery System             |
      | Racks -> Modules -> Cells  |
      +-------------+--------------+
                    |
          +---------+---------+
          |                   |
          v                   v
+------------------+  +--------------------+
| BMS              |  | Thermal Management |
| Monitoring       |  | Cooling / Heating  |
| Protection       |  | Temperature Control|
+--------+---------+  +--------------------+
         |
         v
+----------------------------+
| EMS - Energy Management    |
| Charging / Discharging     |
| Energy Scheduling          |
+-------------+--------------+
              |
              v
+----------------------------+
| Monitoring / SCADA          |
| Status, Alarms, Data Logs   |
+----------------------------+
```

## Component Functions

- **Battery racks:** Store electrical energy.
- **BMS:** Monitors battery conditions and manages battery protection.
- **PCS:** Converts power between AC and DC and controls power flow.
- **EMS:** Supervises energy scheduling and charging/discharging.
- **Thermal management:** Controls battery temperature.
- **Monitoring / SCADA:** Displays operating status, alarms, and historical data.

## Operation

During charging, electrical energy passes through the PCS to the battery.
During discharging, battery energy passes through the PCS to the grid or load.
The BMS monitors battery conditions, while the EMS supervises overall system operation.

Note: This is a conceptual architecture. The components communicate and coordinate; they do not necessarily operate in one physical sequence.
