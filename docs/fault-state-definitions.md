# AegisCAN Week 3 — BMS Fault State Definitions

## 1. Purpose

This document defines the simplified BMS fault states used in the AegisCAN Week 3 prototype.

The fault states describe how the BMS responds when battery operating parameters exceed predefined safety thresholds.

These thresholds are educational simulation values and are not production EV safety limits.

---

## 2. BMS State Model

```text
                 ┌──────────────┐
                 │    NORMAL    │
                 └──────┬───────┘
                        │
              Parameter exceeds limit
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
 OVER_VOLTAGE     UNDER_VOLTAGE     OVER_CURRENT
        │               │                │
        └───────────────┼────────────────┘
                        │
                        ▼
                ┌───────────────┐
                │     FAULT      │
                └───────┬───────┘
                        │
                        ▼
                CONTACTOR OPEN
                        │
                        ▼
                BATTERY ISOLATED