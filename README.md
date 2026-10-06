# AEGISCAN
Intelligent CAN Cybersecurity for EV
An intelligent cybersecurity system for CAN# AegisCAN

## Intelligent CAN Cybersecurity for Electric Vehicles

AegisCAN is a CAN Bus Cybersecurity and Intrusion Detection System designed to analyze Controller Area Network (CAN) communication in Electric Vehicle (EV) systems.

The project aims to identify abnormal and potentially malicious CAN traffic using data processing, feature extraction and intrusion detection techniques.

## Problem

CAN is widely used for communication between Electronic Control Units (ECUs), Battery Management Systems (BMS) and other automotive systems.

Traditional CAN communication has limited built-in security mechanisms, which can make it vulnerable to attacks such as:

- Message Injection
- Message Spoofing
- Denial-of-Service (DoS)
- CAN Bus Flooding
- Abnormal Message Transmission

## AegisCAN Objective

The main objective is to develop a prototype system that can:

- Analyze CAN traffic
- Preprocess CAN messages
- Extract relevant features
- Detect abnormal communication
- Identify potential attacks
- Visualize detection results

## Initial Architecture

```text
Vehicle / EV CAN Network
          |
          v
    CAN Data Capture
          |
          v
    Data Preprocessing
          |
          v
    Feature Extraction
          |
          v
 AegisCAN Detection Engine
          |
     +----+----+
     |         |
     v         v
   Normal   Suspicious
   Traffic    Traffic
                |
                v
       Detection & Visualization