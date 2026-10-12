# CAN Fundamentals

## 1. Introduction

Controller Area Network (CAN) is a communication protocol widely used in automotive systems for communication between Electronic Control Units (ECUs).

In AegisCAN, understanding CAN communication is essential because the cybersecurity detection system analyzes CAN traffic to identify abnormal behavior.

---

## 2. Electronic Control Unit (ECU)

An Electronic Control Unit (ECU) is an embedded computer responsible for controlling or monitoring a particular function of a vehicle.

Examples include:

- Battery Management System (BMS)
- Vehicle Control Unit (VCU)
- Motor Control Unit (MCU)
- Other vehicle control modules

These ECUs can exchange information through the CAN network.

---

## 3. CAN Bus

A CAN bus is a shared communication network that allows multiple ECUs to communicate with each other.

Conceptually:

```text
BMS ─────┐
VCU ─────┤
MCU ─────┼──── CAN Bus
ECU ─────┤
Other ───┘


---

## 4. CAN Controller and Transceiver

### CAN Controller
The CAN controller manages CAN communication according to the protocol. It prepares messages for transmission, receives messages, and handles protocol-related tasks.

### CAN Transceiver
The CAN transceiver converts the controller's logic-level signals into electrical signals for the physical CAN bus and converts received bus signals back into logic-level signals.

In simple terms:
- Controller: handles CAN messages and protocol operations.
- Transceiver: connects the controller electrically to the CAN network.

## 5. CAN Arbitration

Multiple ECUs may try to transmit at the same time. CAN uses arbitration to decide which message continues.

- Each message has an identifier.
- During arbitration, a dominant bit overrides a recessive bit.
- The frame with the higher priority wins arbitration.
- Other nodes stop transmitting and retry later.
- The winning frame is not corrupted by this arbitration process.

For standard 11-bit identifiers, a numerically lower identifier generally has higher priority.

## 6. CAN ID, Frame, DLC, and Payload

### CAN ID
The CAN identifier identifies a message and determines its priority during arbitration. It is not cryptographic proof of which ECU sent the message.

### CAN Frame
A CAN frame is the structured unit transmitted on the bus. It contains fields such as the identifier, control information, data, and error-checking information.

### DLC
DLC means Data Length Code. It indicates the payload length according to the CAN frame format.

### Payload
The payload contains the actual bytes representing signals such as battery voltage, current, temperature, or SOC.

For classic CAN, the payload can contain up to 8 bytes.

Example from the AEGISCAN generator:

- CAN ID: `0x180`
- DLC: `8`
- Payload: `A00FF40100000000`

The payload contains the encoded pack voltage and current according to the project-defined message map.

## 7. Signal Scaling and Byte Order

A CAN payload contains bytes, not automatically readable engineering values. A message definition must explain how to decode those bytes.

For AEGISCAN:

- Pack voltage uses a scale of 0.1 V per bit.
- Pack current uses a scale of 0.1 A per bit.
- SOC and SOH use a scale of 0.1 percentage points per bit.
- Temperature uses a scale of 0.1 °C per bit.
- Multi-byte values use little-endian byte order.

Example:

A raw voltage value of `4000` represents:

`4000 × 0.1 = 400.0 V`

The decoder must also know whether a signal is signed or unsigned.

## 8. Message Frequency and Timestamps

Message frequency describes how often a CAN message is transmitted.

Frequency is measured in hertz (Hz), and the message period is measured in seconds.

- Frequency = 1 / period
- A 10 ms period corresponds to 100 messages per second for that message ID.
- Timestamps help measure intervals, delays, and timing anomalies.

The current AEGISCAN generator assigns timestamps 0.01 seconds apart to successive rows. This is a simulated sequence, not yet a periodic schedule for each individual CAN ID.

## 9. CAN FD

CAN FD means CAN with Flexible Data-Rate.

Compared with classic CAN:
- Classic CAN carries up to 8 payload bytes.
- CAN FD carries up to 64 payload bytes.
- CAN FD can use a faster data phase when supported by the network.
- CAN FD retains CAN's arbitration concepts.

CAN FD requires compatible controllers and transceivers across the relevant network. It is an introduction topic in this project; the current generator represents classic CAN frames.

## 10. DBC Files

A DBC file is a database format commonly used to describe CAN messages and signals.

It can define:
- Message identifiers and names
- Signal names and bit positions
- Signal length and byte order
- Signed or unsigned representation
- Scaling and offset
- Physical units

A DBC allows software tools to convert raw CAN payload bytes into readable values and encode values back into payloads.

The AEGISCAN file `docs/can-message-map.md` documents our current project-specific message definitions in Markdown. It is not itself a DBC file.

## 11. CAN and BMS Communication

The BMS measures battery conditions and can communicate selected values to other controllers over a vehicle network.

Example AEGISCAN flow:

Battery measurements
        ↓
BMS model
        ↓
CAN message encoder
        ↓
CAN ID + DLC + payload
        ↓
CAN traffic dataset
        ↓
Analysis and intrusion detection

The Week 4 generator encodes simulated BMS values into four project-defined CAN frame representations.

## 12. CAN Cybersecurity and AEGISCAN

CAN was designed for reliable communication, not as a complete cybersecurity system. Classic CAN does not inherently authenticate each message cryptographically.

Potential concerns include:

- Spoofing: injecting a message that appears to represent a known signal.
- Replay: retransmitting previously captured messages.
- Denial of Service (DoS): disrupting timely communication by flooding or interfering with the bus.
- Anomalous timing: unexpected message intervals or rates.
- Implausible values: signals outside expected ranges or inconsistent with related signals.

An Intrusion Detection System (IDS) analyzes traffic and flags suspicious patterns. An alert does not automatically prove an attack; the system must be tested for false positives and false negatives.

## 13. Current AEGISCAN Generator Limitations

The current `src/can_bms_generator.py`:

- Encodes selected simulated BMS measurements.
- Uses project-defined 11-bit CAN identifiers.
- Creates 8-byte classic CAN payloads.
- Applies documented signal scaling and byte order.
- Saves frame representations to `data/bms_can_frames.csv`.

It does not transmit physical CAN traffic or implement the complete CAN electrical/protocol stack, including actual arbitration, CRC generation, acknowledgements, or bus timing.

## 14. Summary

CAN allows multiple vehicle controllers to exchange messages over a shared network. Understanding identifiers, frames, payloads, signal scaling, arbitration, and message timing is essential for interpreting CAN traffic.

For AEGISCAN, this knowledge supports the next cybersecurity steps: analyzing message behavior, detecting anomalies, and validating detection logic against simulated normal and attack traffic.
