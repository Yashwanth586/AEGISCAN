\# AEGISCAN Week 6 – Requirements Traceability Matrix



\## Requirements Traceability



| Requirement ID | Requirement | Test Case | Expected Result | Result |

|---|---|---|---|---|

| REQ-01 | Detect normal battery condition | TC-01 | NORMAL state | PASS |

| REQ-02 | Detect over-voltage | TC-02 | OVER\_VOLTAGE | PASS |

| REQ-03 | Detect under-voltage | TC-03 | UNDER\_VOLTAGE | PASS |

| REQ-04 | Detect over-current | TC-04 | OVER\_CURRENT | PASS |

| REQ-05 | Detect over-temperature | TC-05 | OVER\_TEMPERATURE | PASS |

| REQ-06 | Validate upper voltage boundary | TC-06 | NORMAL at 450 V | PASS |

| REQ-07 | Validate lower voltage boundary | TC-07 | NORMAL at 300 V | PASS |

| REQ-08 | Validate current boundary | TC-08 | NORMAL at 200 A | PASS |

| REQ-09 | Validate temperature boundary | TC-09 | NORMAL at 60 °C | PASS |

| REQ-10 | Open contactor during fault | TC-10 | Contactor OPEN | PASS |

| REQ-11 | Keep contactor closed during normal operation | TC-11 | Contactor CLOSED | PASS |

| REQ-12 | Detect balanced cell condition | TC-12 | Balancing INACTIVE | PASS |

| REQ-13 | Detect cell voltage imbalance | TC-13 | Balancing ACTIVE | PASS |

| REQ-14 | Use correct battery measurement CAN ID | TC-14 | 0x180 | PASS |

| REQ-15 | Use correct battery status CAN ID | TC-15 | 0x200 | PASS |

| REQ-16 | Use correct thermal status CAN ID | TC-16 | 0x300 | PASS |

| REQ-17 | Use correct BMS health CAN ID | TC-17 | 0x400 | PASS |

| REQ-18 | Generate valid CAN payload | TC-18 | 8-byte payload | PASS |

| REQ-19 | Encode/decode voltage and current | TC-19 | Original values recovered | PASS |

| REQ-20 | Encode/decode SOC and SOH | TC-20 | Original values recovered | PASS |

| REQ-21 | Encode temperature and fault code | TC-21 | Correct values recovered | PASS |

| REQ-22 | Report over-temperature fault through CAN | TC-22 | Fault code 4 | PASS |

| REQ-23 | Report normal contactor and balancing status | TC-23 | CLOSED / INACTIVE | PASS |

| REQ-24 | Report fault and open contactor through CAN | TC-24 | OPEN / fault code 4 | PASS |

| REQ-25 | Reject invalid CAN ID | TC-25 | ValueError | PASS |

| REQ-26 | Reject invalid payload length | TC-26 | ValueError | PASS |

| REQ-27 | Validate unsigned 16-bit boundaries | TC-27 | Correct boundary encoding | PASS |

| REQ-28 | Validate signed 16-bit boundaries | TC-28 | Correct boundary encoding | PASS |



\## Summary



| Metric | Result |

|---|---:|

| Requirements covered | 28 |

| Test cases | 28 |

| Passed | 28 |

| Failed | 0 |

| Coverage status | Complete |



All Week 6 validation test cases currently pass successfully.

