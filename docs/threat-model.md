\# AegisCAN Week 8 - Threat Model



\## 1. Overview



AegisCAN is an intelligent CAN cybersecurity system for Electric Vehicles (EVs).



The Week 8 threat model focuses on cybersecurity risks affecting the Battery Management System (BMS) and Controller Area Network (CAN) communication.



The system uses controlled simulation to generate normal and anomalous CAN traffic and demonstrates detection of common CAN security threats.



\## 2. Security Objectives



The main security objectives of AegisCAN are:



1\. Detect unauthorized CAN messages.

2\. Detect abnormal CAN message frequencies.

3\. Detect spoofed CAN payloads.

4\. Detect replayed CAN messages.

5\. Distinguish normal CAN traffic from anomalous traffic.

6\. Identify the type of detected security attack.

7\. Provide a reason for each detected security anomaly.

8\. Validate the detection system using automated tests.



\## 3. System Assets



\### 3.1 Battery Management System (BMS)



The BMS monitors important battery parameters such as:



\- Battery voltage

\- Battery current

\- Battery temperature

\- State of Charge (SOC)

\- State of Health (SOH)

\- Contactor status

\- Cell balancing status

\- Battery fault status



\### 3.2 CAN Communication



The simulated AegisCAN system uses the following CAN IDs:



| CAN ID | Function |

|---|---|

| 0x180 | Battery measurements |

| 0x200 | Battery status |

| 0x300 | Thermal status |

| 0x400 | BMS health |



\## 4. Threat Actors



The Week 8 threat model considers an attacker capable of injecting or manipulating CAN traffic.



The simulated attacker may:



\- Send unauthorized CAN frames.

\- Send CAN messages at an abnormally high frequency.

\- Inject fabricated payload values.

\- Replay previously observed CAN messages.



The current implementation is a controlled software simulation and does not model physical access to a real vehicle CAN bus.



\## 5. Threat Scenarios



\### 5.1 Spoofing Attack



In a spoofing attack, an attacker creates a fabricated CAN message using an authorized CAN ID.



The AegisCAN simulation uses:



```text

CAN ID: 0x180

Payload: FF FF FF FF FF FF FF FF

