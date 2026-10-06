# AegisCAN Problem Statement

## Problem Statement

Modern Electric Vehicles (EVs) use Controller Area Network (CAN) communication to exchange information between Electronic Control Units (ECUs), Battery Management Systems (BMS), and other vehicle systems.

Although CAN is reliable and widely used, traditional CAN communication has limited built-in security mechanisms. This makes the network vulnerable to cybersecurity attacks.

Potential attacks include:

- Message injection
- Message spoofing
- Denial-of-Service (DoS)
- CAN bus flooding
- Abnormal message transmission

An attacker may send malicious CAN messages that appear similar to legitimate vehicle communication. Detecting such activity manually can be difficult, especially when a large amount of CAN traffic is generated.

## Proposed Solution

AegisCAN is proposed as a CAN cybersecurity and Intrusion Detection System (IDS).

The system will analyze CAN traffic, preprocess the received messages, extract relevant features and identify abnormal or potentially malicious communication.

## Main Objective

The main objective is to develop a prototype capable of detecting suspicious CAN traffic and providing useful information about the detected activity.

## Scope

The project will initially focus on:

1. Understanding CAN communication.
2. Understanding CAN vulnerabilities.
3. Collecting or using CAN datasets.
4. Preprocessing CAN messages.
5. Extracting relevant features.
6. Detecting abnormal traffic.
7. Identifying possible attacks.
8. Visualizing detection results.

## Expected Result

AegisCAN should provide a prototype intrusion detection system that can distinguish normal CAN communication from suspicious or abnormal traffic and present the results in an understandable manner.
