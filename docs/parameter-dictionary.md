# AegisCAN Week 2 — Battery Parameter Dictionary

## Purpose

This parameter dictionary defines the important battery parameters used in the AegisCAN Week 2 battery fundamentals study and simulation.

| Parameter | Symbol | Unit | Description | Example Value | AegisCAN Relevance |
|---|---|---|---|---:|---|
| Voltage | V | V | Electrical potential difference of the battery | 400 V | Can be monitored through BMS/CAN messages |
| Current | I | A | Electrical current flowing into or out of the battery | 50 A | Useful for detecting abnormal current-related messages |
| Capacity | C | Ah | Amount of electrical charge the battery can store | 100 Ah | Used for energy and C-rate calculations |
| Energy | E | Wh / kWh | Amount of electrical energy stored in the battery | 40 kWh | Represents available battery energy |
| State of Charge | SOC | % | Percentage of usable charge remaining | 75% | Important battery status parameter |
| State of Health | SOH | % | Relative condition of the battery compared with its reference condition | 98% | Indicates battery degradation |
| State of Power | SOP | kW | Power that can safely be delivered or accepted under current conditions | 60 kW | Useful for monitoring battery power limits |
| Temperature | T | °C | Operating temperature of the battery | 32 °C | Important for battery safety and monitoring |
| C-rate | C-rate | C | Charge/discharge current relative to battery capacity | 1C | Indicates charging or discharging rate |
| DLC | DLC | bytes | Number of data bytes carried by a CAN frame | 8 | Relevant when battery data is transmitted through CAN |
| CAN ID | ID | hexadecimal | Identifier of a CAN message | 0x180 | Used to identify and analyze CAN messages |
| Timestamp | t | seconds | Time at which a measurement or CAN message occurs | 0.001 s | Used for message timing and frequency analysis |

---

## 1. Voltage

**Unit:** Volt (V)

Voltage represents the electrical potential difference of the battery.

Example:

```text
Battery Voltage = 400 V