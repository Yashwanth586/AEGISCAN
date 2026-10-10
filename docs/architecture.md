
# AegisCAN Initial Architecture

## 1. System Overview

AegisCAN is an intelligent cybersecurity system designed to monitor
Controller Area Network (CAN) traffic in electric vehicles and identify
abnormal or potentially malicious activity.

## 2. Architecture Flow

```text
EV / VEHICLE CAN NETWORK
          |
          v
    CAN DATA CAPTURE
          |
          v
    DATA PREPROCESSING
          |
          v
     FEATURE EXTRACTION
          |
          v
   AEGISCAN DETECTION ENGINE
          |
          v
   +-----------------------+
   |   Traffic Decision    |
   +-----------------------+
       |              |
       v              v
  NORMAL TRAFFIC   SUSPICIOUS TRAFFIC
                         |
                         v
                 ALERT / VISUALIZATION
```

## 3. Main Components

1. **CAN Network:** Carries messages between vehicle electronic control units.
2. **CAN Data Capture:** Collects CAN messages for analysis.
3. **Data Preprocessing:** Organizes and validates captured data.
4. **Feature Extraction:** Calculates useful properties such as message
   frequency, CAN ID, payload information, and timing.
5. **Detection Engine:** Identifies potentially abnormal traffic using
   detection rules or models.
6. **Alert and Visualization:** Presents suspicious activity for review.

## 4. Project Scope

The initial implementation uses simulated CAN traffic and simulated attack
data. It is a research and learning prototype, not a production-ready
vehicle security system.

## 5. Future Integration

The architecture can be extended to analyze BMS-related CAN messages,
integrate additional detection algorithms, and display detection results
through a monitoring dashboard.
