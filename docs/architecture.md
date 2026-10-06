# AegisCAN Initial Architecture

## System Overview

AegisCAN will monitor CAN communication and analyze CAN messages to identify abnormal or potentially malicious activity.

## Architecture Flow

```text
                 VEHICLE / EV CAN NETWORK
                          │
                          ▼
                  ┌─────────────────┐
                  │   CAN Traffic   │
                  │      Data       │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   CAN Data      │
                  │    Capture      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Data             │
                  │ Preprocessing    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Feature          │
                  │ Extraction       │
                  └────────┬────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │ AEGISCAN DETECTION      │
              │        ENGINE           │
              └────────────┬────────────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
          ┌─────────────┐     ┌─────────────┐
          │ Normal CAN  │     │ Suspicious  │
          │   Traffic   │     │   Traffic   │
          └─────────────┘     └──────┬──────┘
                                     │
                                     ▼
                              ┌─────────────┐
                              │ Detection & │
                              │ Visualization│
                              └─────────────┘