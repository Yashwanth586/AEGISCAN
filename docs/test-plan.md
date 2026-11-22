\# AEGISCAN Week 6 – Test Plan



\## 1. Purpose



The purpose of this test plan is to validate the functional behaviour of the simulated Battery Management System (BMS) and Controller Area Network (CAN) communication system developed for AEGISCAN.



The testing focuses on BMS protection logic, contactor control, cell balancing, CAN message generation, CAN encoding/decoding, fault reporting, boundary conditions, and invalid input handling.



\## 2. Test Objectives



The objectives of Week 6 validation are:



\- Verify normal BMS operation.

\- Verify detection of voltage, current, and temperature faults.

\- Verify contactor behaviour during normal and fault conditions.

\- Verify cell balancing behaviour.

\- Verify CAN message identifiers and payload structure.

\- Verify CAN data encoding and decoding.

\- Verify fault information transmitted through CAN.

\- Verify boundary conditions.

\- Verify invalid CAN inputs are rejected.

\- Produce repeatable automated test results.



\## 3. Scope



\### In Scope



\- BMS protection logic

\- Voltage monitoring

\- Current monitoring

\- Temperature monitoring

\- Contactor control

\- Cell balancing

\- CAN message generation

\- CAN message decoding

\- CAN message identifiers

\- CAN payload validation

\- Fault-code transmission

\- Boundary testing

\- Negative testing



\### Out of Scope



\- Physical vehicle CAN hardware

\- Physical battery pack testing

\- Real ECU hardware validation

\- Real-world electromagnetic interference testing



\## 4. Test Environment



| Item | Configuration |

|---|---|

| Operating System | Windows |

| Programming Language | Python |

| Python Version | 3.14.8 |

| Test Framework | pytest |

| Project | AEGISCAN |

| Test Environment | Python virtual environment |



\## 5. Test Methodology



Automated functional tests are implemented using pytest.



Each test:



1\. Creates the required BMS/CAN test condition.

2\. Executes the relevant system function.

3\. Compares the actual result with the expected result.

4\. Reports PASS or FAIL automatically.



\## 6. Test Categories



\### Functional Testing



Normal BMS operation, protection behaviour, contactor operation, cell balancing, CAN generation, and CAN decoding are tested.



\### Boundary Testing



Values at important operating boundaries are tested, including:



\- 300 V and 450 V voltage limits

\- 200 A current limit

\- 60 °C temperature limit

\- Signed and unsigned 16-bit data boundaries



\### Negative Testing



Invalid or fault conditions are tested, including:



\- Over-voltage

\- Under-voltage

\- Over-current

\- Over-temperature

\- Invalid CAN ID

\- Invalid CAN payload length



\## 7. Pass/Fail Criteria



A test is marked PASS when the actual system behaviour matches the expected result.



A test is marked FAIL when the actual behaviour differs from the expected result or when the expected exception/error condition is not produced.



\## 8. Test Execution



The test suite is executed using:



```bash

python -m pytest -v tests/test\_bms\_model.py

python -m pytest -v tests/test\_can\_validation.py

