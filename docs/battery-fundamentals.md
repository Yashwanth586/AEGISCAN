# AegisCAN Week 2 — Battery Fundamentals

## 1. Introduction

Electric Vehicles (EVs) use high-voltage battery packs as their primary energy source. The battery system must be continuously monitored and controlled to ensure safe and efficient vehicle operation.

AegisCAN focuses on cybersecurity monitoring of vehicle communication networks. Understanding battery parameters is important because battery-related information is commonly exchanged between the Battery Management System (BMS) and other vehicle Electronic Control Units (ECUs) through the CAN network.

This document covers the fundamental battery concepts required for the AegisCAN project.

---

## 2. Battery Cell

A battery cell is the basic electrochemical unit of a battery.

A typical lithium-ion cell has a nominal voltage of approximately 3.6–3.7 V.

Important cell parameters include:

- Voltage
- Current
- Capacity
- Temperature
- State of Charge (SOC)
- State of Health (SOH)

---

## 3. Battery Module

A battery module is a group of individual cells connected together.

Cells can be connected in:

- Series
- Parallel
- Series-parallel combinations

Modules provide a higher voltage and/or capacity than a single cell.

---

## 4. Battery Pack

A battery pack consists of multiple battery modules connected together.

An EV battery pack typically contains:

- Multiple cells
- Battery modules
- Battery Management System (BMS)
- Temperature sensors
- Voltage monitoring circuits
- Current sensors
- Contactors
- Protection systems

The complete battery pack supplies electrical energy to the vehicle powertrain.

---

## 5. Series Connection

When battery cells are connected in series:

- Voltage increases
- Capacity remains approximately the same

For example, three 3.7 V, 2 Ah cells connected in series:

```text
Voltage = 3.7 + 3.7 + 3.7
        = 11.1 V

Capacity = 2 Ah
