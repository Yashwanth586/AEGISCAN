\# AegisCAN Week 8 - Security Requirements



\## 1. Overview



This document defines the cybersecurity requirements for the AegisCAN Week 8 implementation.



The requirements focus on protecting the simulated Battery Management System (BMS) CAN communication from common CAN-based security threats.



The requirements are derived from the Week 8 threat model and attack surface analysis.



\---



\## 2. Security Objectives



AegisCAN shall:



1\. Identify unauthorized CAN messages.

2\. Detect abnormal CAN message frequencies.

3\. Detect simulated spoofed CAN payloads.

4\. Detect replayed CAN message sequences.

5\. Classify CAN traffic as normal or anomalous.

6\. Identify the type of detected attack.

7\. Provide a security reason for detected anomalies.

8\. Validate the security detection system using automated tests.



\---



\## 3. Functional Security Requirements



\### SR-01: CAN ID Authorization



The system shall maintain a list of authorized BMS CAN IDs.



The authorized CAN IDs are:



```text

0x180

0x200

0x300

0x400

```



Any CAN message using an ID outside this list shall be considered potentially unauthorized.



\---



\### SR-02: Unauthorized Message Detection



The system shall detect CAN messages using unauthorized CAN IDs.



For the Week 8 simulation:



```text

Unauthorized CAN ID: 0x555

```



The detected attack type shall be classified as:



```text

UNAUTHORIZED

```



\---



\### SR-03: Message Frequency Monitoring



The system shall monitor the frequency of CAN messages.



The configured frequency thresholds are:



| CAN ID | Function | Threshold |

|---|---|---:|

| 0x180 | Battery measurements | 500 Hz |

| 0x200 | Battery status | 250 Hz |

| 0x300 | Thermal status | 250 Hz |

| 0x400 | BMS health | 100 Hz |



A message frequency above the configured threshold shall be considered anomalous.



\---



\### SR-04: Flooding Detection



The system shall detect excessive CAN message transmission rates.



The Week 8 flooding simulation uses:



```text

Normal frequency: 100 Hz

Flooding frequency: 1000 Hz

```



When the configured frequency threshold is exceeded, the traffic shall be classified as:



```text

FLOODING

```



\---



\### SR-05: Spoofing Detection



The system shall detect simulated fabricated CAN payloads.



The Week 8 spoofing scenario uses:



```text

CAN ID: 0x180

Payload: FF FF FF FF FF FF FF FF

```



The simulated spoofed traffic shall be classified as:



```text

SPOOFING

```



\---



\### SR-06: Replay Detection



The system shall identify repeated CAN message sequences that indicate simulated replay behaviour.



The detection mechanism shall consider:



\- Repeated CAN ID

\- Repeated payload

\- Message sequence

\- Short message intervals



A detected replay sequence shall be classified as:



```text

REPLAY

```



\---



\## 4. Traffic Classification Requirements



\### SR-07: Normal Traffic Classification



The system shall classify valid CAN traffic that does not violate the configured security checks as:



```text

NORMAL

```



\---



\### SR-08: Anomalous Traffic Classification



The system shall classify traffic that violates one or more security conditions as:



```text

ANOMALOUS

```



\---



\### SR-09: Attack Type Classification



The system shall identify the specific simulated attack type when an anomaly is detected.



Supported attack classifications are:



```text

SPOOFING

REPLAY

FLOODING

UNAUTHORIZED

```



\---



\## 5. Dataset Requirements



\### SR-10: Security Dataset Generation



The system shall generate a controlled security dataset containing both normal and anomalous CAN traffic.



The Week 8 dataset contains:



```text

Total messages: 60

Normal messages: 40

Anomalous messages: 20

```



The anomalous messages contain:



```text

Spoofing: 5

Replay: 5

Flooding: 5

Unauthorized: 5

```



The dataset shall be stored at:



```text

data/security\_dataset.csv

```



\---



\### SR-11: Detection Results



The system shall generate a detection results dataset containing the security classification for each simulated CAN message.



The results shall be stored at:



```text

data/security\_detection\_results.csv

```



\---



\## 6. Detection Requirements



\### SR-12: Detection Result



For every CAN message processed by the security detector, the system shall generate a security classification.



The classification shall identify whether the message is:



```text

NORMAL

```



or:



```text

ANOMALOUS

```



\---



\### SR-13: Attack Identification



For anomalous messages, the detector shall identify the associated simulated attack type.



The supported values are:



```text

SPOOFING

REPLAY

FLOODING

UNAUTHORIZED

```



Normal traffic shall be represented by:



```text

NONE

```



\---



\### SR-14: Detection Accuracy



The Week 8 detection system shall successfully detect all simulated anomalous messages in the generated security dataset.



Expected result:



```text

Normal: 40

Anomalous: 20

```



Expected attack classification:



```text

SPOOFING: 5

REPLAY: 5

FLOODING: 5

UNAUTHORIZED: 5

```



\---



\## 7. Validation Requirements



\### SR-15: Automated Testing



The Week 8 security implementation shall be validated using automated pytest tests.



The security test suite shall verify:



\- Security dataset creation

\- Detection result creation

\- Required result columns

\- Normal traffic detection

\- Spoofing detection

\- Replay detection

\- Flooding detection

\- Unauthorized message detection

\- Total anomaly detection

\- Total message count



\---



\### SR-16: Test Execution



The Week 8 security tests shall be executable using:



```powershell

python -m pytest -v tests/test\_can\_security.py

```



The complete AegisCAN test suite shall be executable using:



```powershell

python -m pytest -v tests

```



\---



\## 8. Traceability



| Requirement | Security Feature | Validation |

|---|---|---|

| SR-01 | Authorized CAN ID list | Unauthorized detection test |

| SR-02 | Unauthorized CAN detection | Unauthorized test |

| SR-03 | Frequency monitoring | Flooding detection test |

| SR-04 | Flooding detection | Flooding test |

| SR-05 | Spoofing detection | Spoofing test |

| SR-06 | Replay detection | Replay test |

| SR-07 | Normal classification | Normal traffic test |

| SR-08 | Anomaly classification | Anomaly count test |

| SR-09 | Attack classification | Detection tests |

| SR-10 | Security dataset | Dataset test |

| SR-11 | Detection results | Results file test |

| SR-12 | Message classification | Detection tests |

| SR-13 | Attack identification | Attack classification tests |

| SR-14 | Detection accuracy | Anomaly count test |

| SR-15 | Automated testing | pytest |

| SR-16 | Test execution | Full test suite |



\---



\## 9. Security Requirement Limitations



The current Week 8 security requirements apply to the simulated AegisCAN environment.



They do not yet define complete requirements for:



\- Real CAN hardware

\- Hardware security modules

\- Secure boot

\- Cryptographic authentication

\- CAN message encryption

\- Automotive IDS deployment

\- Real-time ECU response

\- Vehicle gateway security

\- Diagnostic security

\- Wireless attack protection



These requirements can be expanded during future AegisCAN development.



\---



\## 10. Conclusion



The Week 8 security requirements define the expected security behaviour of AegisCAN against four simulated CAN threats:



1\. Spoofing

2\. Replay

3\. Flooding

4\. Unauthorized CAN messages



The requirements provide measurable security objectives for CAN ID validation, frequency monitoring, payload analysis, sequence analysis, attack classification, dataset generation, and automated validation.



These requirements establish the security baseline for the next stages of AegisCAN development.

