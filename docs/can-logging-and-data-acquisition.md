# Week 5 — CAN Monitoring & Data Acquisition

## 1. Objective

The objective of Week 5 is to implement CAN monitoring and data acquisition for the AEGISCAN project.

The system performs the following operations:

1. Log raw CAN frames.
2. Preserve timestamps, CAN IDs, DLC and payload data.
3. Decode raw CAN payloads into engineering BMS values.
4. Analyze CAN message frequency.
5. Generate CSV files for further analysis.

---

## 2. CAN Data Acquisition Flow

The Week 5 data flow is:

BMS Data
→ CAN Frames
→ CAN Logger
→ Raw CAN CSV Log
→ CAN Decoder
→ Decoded BMS Values

The frequency-analysis stage uses the CAN log to determine the transmission frequency of each CAN ID.

---

## 3. CAN Logger

Source file:

`src/can_logger.py`

The CAN logger reads the simulated BMS CAN frames and generates a repeated CAN data-acquisition log.

Each logged frame contains:

- Timestamp
- CAN ID
- DLC
- CAN payload
- Time difference from the previous frame
- Aggregate frame rate

The generated file is:

`data/can_log.csv`

The simulation contains:

- 40 total CAN frames
- 10 cycles
- 4 CAN messages per cycle
- 0.01 s between consecutive frames
- 0.04 s cycle period

The aggregate simulated CAN frame rate is:

**100 Hz**

---

## 4. CAN Message Logging

The simulated CAN IDs are:

| CAN ID | Message | Purpose |
|---|---|---|
| 0x180 | Battery Measurements | Voltage and current |
| 0x200 | Battery Status | SOC and SOH |
| 0x300 | Thermal Status | Temperature and fault code |
| 0x400 | BMS Health | Contactor, balancing and health fault |

Each message uses:

- DLC = 8 bytes
- Classic CAN-style payload representation

---

## 5. CAN Decoder

Source file:

`src/can_decoder.py`

The decoder converts raw hexadecimal CAN payloads into engineering values using the signal definitions from the CAN message map.

Examples:

| CAN ID | Decoded Signal | Value |
|---|---|---:|
| 0x180 | Voltage | 400.0 V |
| 0x180 | Current | 50.0 A |
| 0x200 | SOC | 75.0 % |
| 0x200 | SOH | 98.0 % |
| 0x300 | Temperature | 32.0 °C |
| 0x300 | Fault Code | 0 |
| 0x400 | Contactor | CLOSED |
| 0x400 | Balancing | INACTIVE |
| 0x400 | Health Fault Code | 0 |

The decoded output is stored in:

`data/decoded_can_data.csv`

---

## 6. Message Frequency Analysis

Source file:

`src/can_frequency_analysis.py`

The frequency analyzer groups CAN frames by CAN ID and calculates the message transmission frequency.

The analysis produced:

| CAN ID | Frame Count | Duration | Frequency |
|---|---:|---:|---:|
| 0x180 | 10 | 0.36 s | 25 Hz |
| 0x200 | 10 | 0.36 s | 25 Hz |
| 0x300 | 10 | 0.36 s | 25 Hz |
| 0x400 | 10 | 0.36 s | 25 Hz |

Each CAN message therefore has a simulated transmission frequency of:

**25 Hz**

The combined stream contains four messages at 25 Hz each:

**4 × 25 Hz = 100 Hz aggregate frame rate**

The frequency-analysis output is stored in:

`data/can_frequency_analysis.csv`

---

## 7. Week 5 Demonstration

The Week 5 demonstration successfully shows:

**Raw CAN frames → CAN logging → CAN decoding → Engineering BMS values**

and:

**CAN log → Message grouping → Frequency calculation**

This demonstrates basic CAN monitoring and engineering data acquisition using simulated BMS data.

---

## 8. Generated Files

### Source code

- `src/can_logger.py`
- `src/can_decoder.py`
- `src/can_frequency_analysis.py`

### Data

- `data/can_log.csv`
- `data/decoded_can_data.csv`
- `data/can_frequency_analysis.csv`

---

## 9. Week 5 Outcome

Week 5 successfully implemented a simulated CAN monitoring and data acquisition pipeline.

The system can:

- Capture CAN frames.
- Preserve CAN timestamps.
- Record CAN IDs and payloads.
- Decode CAN payloads.
- Convert raw data into engineering values.
- Calculate message frequencies.
- Store acquisition and analysis results in CSV format.

This provides the foundation for the next phase of AEGISCAN, which focuses on CAN testing, fault injection and cybersecurity threat analysis.