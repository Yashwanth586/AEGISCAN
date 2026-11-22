\# AEGISCAN Week 7 – Root Cause Analysis Worksheet



\## 1. RCA Purpose



The purpose of this worksheet is to document the analysis of controlled faults introduced into the simulated AEGISCAN BMS/CAN system.



The analysis follows:



\*\*Fault Injection → Observation → Diagnosis → Root Cause\*\*



\## 2. RCA Results



| Fault ID | Injected Condition | Observation | Diagnosis | Root Cause | Result |

|---|---|---|---|---|---|

| FI-01 | Pack voltage = 500 V | BMS reports OVER\_VOLTAGE and contactor opens | Voltage exceeded 450 V limit | Controlled voltage injection exceeded BMS threshold | PASS |

| FI-02 | Temperature = 75 °C | BMS reports OVER\_TEMPERATURE and contactor opens | Temperature exceeded 60 °C limit | Controlled temperature injection exceeded BMS threshold | PASS |

| FI-03 | SOC = 120% | CAN encoding raises ValueError | SOC outside valid range rejected | Injected SOC exceeded 0–100% range | PASS |

| FI-04 | CAN ID 0x300 removed | Required message is absent | Missing CAN message detected | Controlled removal of CAN ID 0x300 | PASS |

| FI-05 | CAN ID 0x180 = 1000 Hz | Frequency exceeds 500 Hz threshold | Abnormal CAN frequency detected | Controlled frequency injection exceeded configured threshold | PASS |



\## 3. Evidence Logs



\### FI-01 – Over-Voltage



\- Injection value: 500 V

\- Expected fault: `OVER\_VOLTAGE`

\- Observed fault: `OVER\_VOLTAGE`

\- Contactor: `OPEN`

\- Status: PASS



\### FI-02 – Over-Temperature



\- Injection value: 75 °C

\- Expected fault: `OVER\_TEMPERATURE`

\- Observed fault: `OVER\_TEMPERATURE`

\- Contactor: `OPEN`

\- Status: PASS



\### FI-03 – Invalid SOC



\- Injection value: 120%

\- Expected behaviour: Invalid SOC rejected

\- Observed behaviour: `INVALID\_SOC\_REJECTED`

\- Status: PASS



\### FI-04 – Missing CAN Message



\- Removed CAN ID: `0x300`

\- Expected fault: Missing CAN message

\- Observed fault: `MISSING\_CAN\_MESSAGE`

\- Status: PASS



\### FI-05 – Abnormal CAN Frequency



\- CAN ID: `0x180`

\- Injected frequency: 1000 Hz

\- Threshold: 500 Hz

\- Expected fault: Abnormal CAN frequency

\- Observed fault: `ABNORMAL\_CAN\_FREQUENCY`

\- Status: PASS



\## 4. Overall RCA Conclusion



All five controlled fault scenarios were successfully injected and diagnosed.



The Week 7 implementation demonstrates that the simulated AEGISCAN system can:



\- Inject controlled BMS faults.

\- Detect abnormal operating conditions.

\- Detect invalid CAN-related conditions.

\- Identify missing CAN messages.

\- Detect abnormal CAN message frequency.

\- Report diagnostic information.

\- Identify the root cause of each injected condition.



\*\*Final Result: 5/5 fault scenarios passed.\*\*

