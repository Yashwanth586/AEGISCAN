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