
# AEGISCAN Week 4 - CAN Message Map

## 1. Purpose

This document defines the project-specific CAN message IDs, payload layout,
signal scaling, units, and status codes used by `src/can_bms_generator.py`.

These definitions are for an educational simulation. They are not an
OEM-standard CAN database or a validated production vehicle protocol.

## 2. CAN Configuration

- Protocol: Classic CAN frame representation
- Identifier format: 11-bit standard CAN ID
- Payload length: 8 bytes per frame
- Byte order for multi-byte signals: Little-endian
- Output: `data/bms_can_frames.csv`
- Timestamp unit: Seconds
- Signal scaling: Defined separately for each signal below

## 3. Message Summary

| CAN ID | Message Name | Signals |
|---|---|---|
| 0x180 | Battery Measurements | Pack voltage, pack current |
| 0x200 | Battery Status | SOC, SOH |
| 0x300 | Thermal Status | Temperature, fault code |
| 0x400 | BMS Health | Contactor, balancing, fault code |

## 4. CAN ID 0x180 - Battery Measurements

| Byte(s) | Signal | Data Type | Scale | Unit |
|---|---|---|---|---|
| 0-1 | Pack Voltage | Unsigned 16-bit | 0.1 | V |
| 2-3 | Pack Current | Signed 16-bit | 0.1 | A |
| 4-7 | Reserved | Bytes | — | — |

Decoding:
- Voltage (V) = raw value × 0.1
- Current (A) = signed raw value × 0.1

## 5. CAN ID 0x200 - Battery Status

| Byte(s) | Signal | Data Type | Scale | Unit |
|---|---|---|---|---|
| 0-1 | State of Charge (SOC) | Unsigned 16-bit | 0.1 | % |
| 2-3 | State of Health (SOH) | Unsigned 16-bit | 0.1 | % |
| 4-7 | Reserved | Bytes | — | — |

Decoding:
- SOC (%) = raw value × 0.1
- SOH (%) = raw value × 0.1

## 6. CAN ID 0x300 - Thermal Status

| Byte(s) | Signal | Data Type | Scale | Unit |
|---|---|---|---|---|
| 0-1 | Battery Temperature | Signed 16-bit | 0.1 | °C |
| 2 | Fault Code | Unsigned 8-bit | 1 | Code |
| 3-7 | Reserved | Bytes | — | — |

Decoding:
- Temperature (°C) = signed raw value × 0.1

### Fault Codes

| Code | Meaning |
|---|---|
| 0 | NORMAL |
| 1 | OVER_VOLTAGE |
| 2 | UNDER_VOLTAGE |
| 3 | OVER_CURRENT |
| 4 | OVER_TEMPERATURE |

## 7. CAN ID 0x400 - BMS Health

| Byte | Bit(s) | Signal | Meaning |
|---|---|---|---|
| 0 | Bit 0 | Contactor | 1 = CLOSED, 0 = OPEN |
| 0 | Bit 1 | Balancing | 1 = ACTIVE, 0 = INACTIVE |
| 1 | Bits 0-7 | Fault Code | Uses the fault-code table above |
| 2-7 | — | Reserved | Set to zero |

## 8. Example Values

For the default simulated BMS measurements:

- Pack voltage: 400.0 V
- Pack current: 50.0 A
- SOC: 75.0%
- SOH: 98.0%
- Temperature: 32.0 °C
- Fault state: NORMAL
- Contactor: CLOSED
- Balancing: INACTIVE

The generated payloads should be:

| CAN ID | Payload (hexadecimal) |
|---|---|
| 0x180 | A00FF40100000000 |
| 0x200 | EE02D40300000000 |
| 0x300 | 4001000000000000 |
| 0x400 | 0100000000000000 |

## 9. Message Timing

The generator currently assigns timestamps 0.01 seconds apart to
successive output rows. This is a demonstration sequence, not a validated
periodic schedule for each CAN ID.

A real message-frequency definition should specify the period for each
message ID and be validated against bus load and system requirements.

## 10. Limitations

- Frames are generated in software and are not transmitted over physical CAN hardware.
- CAN CRC, arbitration, acknowledgements, and electrical signaling are not implemented by this CSV generator.
- Reserved bytes are set to zero.
- The IDs and scaling are project-defined for learning purposes.
