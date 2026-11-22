\# AEGISCAN Week 7 – Fault Catalogue



\## 1. Purpose



This fault catalogue documents the controlled fault conditions implemented in the AEGISCAN simulated BMS/CAN system.



The catalogue records the injected condition, expected system behaviour, observed behaviour, diagnostic result, and root cause.



\## 2. Fault Catalogue



| Fault ID | Fault Type | Injection | Expected Behaviour | Observed Result | Status |

|---|---|---|---|---|---|

| FI-01 | Over-Voltage | Pack voltage = 500 V | BMS detects over-voltage and opens contactor | OVER\_VOLTAGE, Contactor OPEN | PASS |

| FI-02 | Over-Temperature | Temperature = 75 °C | BMS detects over-temperature and opens contactor | OVER\_TEMPERATURE, Contactor OPEN | PASS |

| FI-03 | Invalid SOC | SOC = 120% | CAN encoding rejects invalid SOC | INVALID\_SOC\_REJECTED | PASS |

| FI-04 | Missing CAN Message | Remove CAN ID 0x300 | Missing required CAN message is detected | MISSING\_CAN\_MESSAGE | PASS |

| FI-05 | Abnormal CAN Frequency | 0x180 at 1000 Hz | Frequency above threshold is detected | ABNORMAL\_CAN\_FREQUENCY | PASS |



\## 3. Fault Details



\### FI-01 – Over-Voltage



\*\*Injected condition:\*\* Pack voltage increased to 500 V.



\*\*Configured limit:\*\* 450 V.



\*\*Observed fault:\*\* `OVER\_VOLTAGE`



\*\*Safety response:\*\* Contactor opened.



\*\*Root cause:\*\* Controlled injection increased pack voltage above the BMS over-voltage threshold.



\### FI-02 – Over-Temperature



\*\*Injected condition:\*\* Battery temperature increased to 75 °C.



\*\*Configured limit:\*\* 60 °C.



\*\*Observed fault:\*\* `OVER\_TEMPERATURE`



\*\*Safety response:\*\* Contactor opened.



\*\*Root cause:\*\* Controlled injection increased battery temperature above the BMS over-temperature threshold.



\### FI-03 – Invalid SOC



\*\*Injected condition:\*\* SOC increased to 120%.



\*\*Valid range:\*\* 0–100%.



\*\*Observed fault:\*\* `INVALID\_SOC\_REJECTED`



\*\*Diagnostic response:\*\* CAN encoding rejected the invalid SOC value.



\*\*Root cause:\*\* Injected SOC exceeded the valid 0–100% range.



\### FI-04 – Missing CAN Message



\*\*Injected condition:\*\* CAN message with ID `0x300` removed from simulated traffic.



\*\*Expected message:\*\* Thermal status CAN message.



\*\*Observed fault:\*\* `MISSING\_CAN\_MESSAGE`



\*\*Root cause:\*\* Controlled fault injection removed the required CAN message with ID `0x300`.



\### FI-05 – Abnormal CAN Frequency



\*\*Injected condition:\*\* CAN ID `0x180` frequency increased to 1000 Hz.



\*\*Configured threshold:\*\* 500 Hz.



\*\*Observed fault:\*\* `ABNORMAL\_CAN\_FREQUENCY`



\*\*Root cause:\*\* Controlled injection generated CAN messages at an excessively high frequency.



\## 4. Summary



Five controlled fault scenarios were implemented and executed successfully.



\*\*Total fault scenarios:\*\* 5  

\*\*Passed:\*\* 5  

\*\*Failed:\*\* 0



The fault injection module demonstrates the sequence:



\*\*Inject Fault → Observe Behaviour → Diagnose → Identify Root Cause\*\*

