\# AegisCAN Week 8 - Attack Surface



\## 1. Overview



The attack surface of AegisCAN consists of the components and communication points that could potentially be targeted by an attacker.



For Week 8, the focus is on the simulated Electric Vehicle (EV) Battery Management System (BMS) and its Controller Area Network (CAN) communication.



The attack surface is analysed to identify where unauthorized or abnormal CAN traffic could enter the system and how AegisCAN can monitor and detect such activity.



\---



\## 2. AegisCAN Attack Surface



The main components considered in the Week 8 attack surface are:



1\. Battery Management System (BMS)

2\. CAN message generation

3\. CAN communication

4\. CAN message decoding

5\. Security monitoring

6\. Security detection

7\. Security dataset and analysis



\---



\## 3. System Components



\### 3.1 Battery Management System



The BMS is responsible for monitoring battery-related parameters such as:



\- Battery voltage

\- Battery current

\- Battery temperature

\- State of Charge (SOC)

\- State of Health (SOH)

\- Contactor status

\- Cell balancing

\- Fault status



The BMS generates information that is communicated through CAN messages.



\---



\### 3.2 CAN Communication



The simulated CAN network carries messages between the BMS and other vehicle-related systems.



AegisCAN uses the following simulated CAN IDs:



| CAN ID | Function |

|---|---|

| 0x180 | Battery measurements |

| 0x200 | Battery status |

| 0x300 | Thermal status |

| 0x400 | BMS health |



These CAN IDs form an important part of the monitored communication surface.



\---



\### 3.3 CAN Message Generator



The CAN message generator converts BMS information into simulated CAN messages.



An attacker could potentially target this communication by:



\- Modifying payload values

\- Injecting unauthorized messages

\- Repeating valid messages

\- Increasing message transmission frequency



AegisCAN therefore monitors the generated CAN traffic for abnormal behaviour.



\---



\### 3.4 CAN Message Decoder



The CAN decoder interprets CAN IDs and payload data to recover the corresponding BMS information.



Incorrect or malicious CAN messages may result in incorrect decoded information.



Therefore, CAN message decoding is included in the monitoring path of the system.



\---



\## 4. Security Attack Entry Points



The main simulated attack entry points are:



\### 4.1 Authorized CAN ID with Malicious Payload



An attacker may use a legitimate CAN ID but transmit a fabricated payload.



Example:



```text

CAN ID: 0x180

Payload: FF FF FF FF FF FF FF FF

```



This represents the simulated spoofing scenario.



\---



\### 4.2 Repeated CAN Messages



An attacker may retransmit previously observed CAN messages.



AegisCAN simulates repeated 0x180 messages with the same payload and short time intervals.



This represents the replay attack scenario.



\---



\### 4.3 Excessive CAN Message Frequency



An attacker may transmit CAN messages at an abnormally high frequency.



For example:



```text

Normal 0x180 frequency: 100 Hz

Simulated flooding frequency: 1000 Hz

```



This represents the flooding attack scenario.



\---



\### 4.4 Unauthorized CAN ID



An attacker may inject a CAN message using an unknown or unauthorized CAN ID.



AegisCAN uses:



```text

CAN ID: 0x555

```



as the simulated unauthorized message.



The authorized CAN IDs are:



```text

0x180

0x200

0x300

0x400

```



Therefore, 0x555 is classified as unauthorized.



\---



\## 5. Attack Surface Diagram



The Week 8 simulated attack surface can be represented as follows:



```text

&#x20;                ┌──────────────────────┐

&#x20;                │     EV Battery       │

&#x20;                │        System        │

&#x20;                └──────────┬───────────┘

&#x20;                           │

&#x20;                           ▼

&#x20;                ┌──────────────────────┐

&#x20;                │         BMS          │

&#x20;                │ Battery Measurements │

&#x20;                │ Status / Thermal /   │

&#x20;                │ Health Information   │

&#x20;                └──────────┬───────────┘

&#x20;                           │

&#x20;                           ▼

&#x20;                ┌──────────────────────┐

&#x20;                │   CAN Message        │

&#x20;                │     Generator       │

&#x20;                └──────────┬───────────┘

&#x20;                           │

&#x20;                           ▼

&#x20;                ┌──────────────────────┐

&#x20;                │    CAN Network       │

&#x20;                │  0x180  0x200        │

&#x20;                │  0x300  0x400        │

&#x20;                └──────────┬───────────┘

&#x20;                           │

&#x20;             ┌─────────────┼─────────────┐

&#x20;             │             │             │

&#x20;             ▼             ▼             ▼

&#x20;       ┌──────────┐  ┌──────────┐  ┌──────────┐

&#x20;       │ Spoofing │  │  Replay  │  │ Flooding │

&#x20;       └────┬─────┘  └────┬─────┘  └────┬─────┘

&#x20;            │             │             │

&#x20;            └─────────────┼─────────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;                 ┌──────────────────┐

&#x20;                 │   Unauthorized   │

&#x20;                 │    CAN Message   │

&#x20;                 │      0x555       │

&#x20;                 └────────┬─────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;                ┌──────────────────────┐

&#x20;                │ AegisCAN Security    │

&#x20;                │      Detection       │

&#x20;                ├──────────────────────┤

&#x20;                │ CAN ID Check         │

&#x20;                │ Frequency Analysis   │

&#x20;                │ Payload Analysis     │

&#x20;                │ Sequence Analysis    │

&#x20;                └──────────┬───────────┘

&#x20;                           │

&#x20;                           ▼

&#x20;                ┌──────────────────────┐

&#x20;                │ Traffic Classification│

&#x20;                │                      │

&#x20;                │ NORMAL               │

&#x20;                │ ANOMALOUS            │

&#x20;                │                      │

&#x20;                │ SPOOFING             │

&#x20;                │ REPLAY               │

&#x20;                │ FLOODING             │

&#x20;                │ UNAUTHORIZED        │

&#x20;                └──────────────────────┘

```



\---



\## 6. Attack Surface Mapping



| Component | Potential Attack | AegisCAN Monitoring |

|---|---|---|

| BMS CAN data | Fabricated values | Payload analysis |

| CAN ID | Unauthorized ID | CAN ID validation |

| CAN traffic rate | Flooding | Frequency analysis |

| CAN message sequence | Replay | Sequence and timing analysis |

| CAN payload | Spoofing | Payload analysis |

| Security dataset | Incorrect classification | Automated testing |



\---



\## 7. Security Monitoring Points



AegisCAN monitors the CAN traffic at multiple points:



\### CAN ID Validation



Checks whether the received CAN ID belongs to the authorized BMS CAN ID list.



\### Frequency Monitoring



Checks whether the message frequency exceeds the configured threshold.



