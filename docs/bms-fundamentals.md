# AegisCAN Week 3 — BMS Fundamentals

## 1. Introduction

A Battery Management System (BMS) is an electronic control system responsible for monitoring, managing, and protecting a battery pack.

In an Electric Vehicle (EV), the BMS continuously monitors battery operating conditions and takes protective actions when unsafe conditions are detected.

The BMS also provides important battery information to other vehicle systems through communication networks such as CAN.

---

## 2. BMS Functions

The major functions of a BMS are:

- Battery sensing
- SOC estimation
- SOH estimation
- State of Power estimation
- Cell balancing
- Battery protection
- Contactor control
- Fault detection
- Fault management
- Communication with other ECUs

---

## 3. BMS Sensing

The BMS continuously measures important battery parameters.

### Voltage sensing

The BMS monitors:

- Individual cell voltage
- Module voltage
- Pack voltage

Voltage monitoring helps detect:

- Over-voltage
- Under-voltage
- Cell imbalance

### Current sensing

Current sensors measure the current flowing into or out of the battery.

Current information is useful for:

- SOC estimation
- Power estimation
- Over-current protection
- Charging/discharging monitoring

### Temperature sensing

Temperature sensors monitor battery temperature.

Temperature monitoring helps detect:

- Over-temperature
- Abnormal heating
- Thermal risks

The simplified AegisCAN BMS model monitors:

```text
Pack Voltage
Current
Temperature
SOC
SOH