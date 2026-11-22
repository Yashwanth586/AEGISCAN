# AegisCAN Week 8 - CAN Security Tests
#
# Purpose:
# Validate the CAN cybersecurity detection system.
#
# Tests:
# 1. Security dataset exists
# 2. Detection results contain expected columns
# 3. Normal traffic is correctly detected
# 4. Spoofing is detected
# 5. Replay is detected
# 6. Flooding is detected
# 7. Unauthorized messages are detected
# 8. All 20 anomalous messages are detected

from pathlib import Path
import pandas as pd

from src.can_security_detection import CANSecurityDetector


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "security_dataset.csv"
)

RESULTS_FILE = (
    PROJECT_ROOT
    / "data"
    / "security_detection_results.csv"
)


def test_security_dataset_exists():
    """Verify that the Week 8 security dataset exists."""

    assert DATA_FILE.exists()


def test_detection_results_exist():
    """Verify that security detection results exist."""

    assert RESULTS_FILE.exists()


def test_detection_result_columns():
    """Verify the required detection result columns."""

    detector = CANSecurityDetector()
    results = detector.analyze()

    expected_columns = {
        "timestamp",
        "can_id",
        "original_label",
        "detected_status",
        "detected_attack",
        "detection_reason",
    }

    assert expected_columns.issubset(set(results.columns))


def test_normal_traffic_detection():
    """Verify that all normal traffic is classified correctly."""

    detector = CANSecurityDetector()
    results = detector.analyze()

    normal_count = (
        results["detected_attack"] == "NONE"
    ).sum()

    assert normal_count == 40


def test_spoofing_detection():
    """Verify that all spoofing messages are detected."""

    detector = CANSecurityDetector()
    results = detector.analyze()

    spoofing_count = (
        results["detected_attack"] == "SPOOFING"
    ).sum()

    assert spoofing_count == 5


def test_replay_detection():
    """Verify that all replay messages are detected."""

    detector = CANSecurityDetector()
    results = detector.analyze()

    replay_count = (
        results["detected_attack"] == "REPLAY"
    ).sum()

    assert replay_count == 5


def test_flooding_detection():
    """Verify that all flooding messages are detected."""

    detector = CANSecurityDetector()
    results = detector.analyze()

    flooding_count = (
        results["detected_attack"] == "FLOODING"
    ).sum()

    assert flooding_count == 5


def test_unauthorized_detection():
    """Verify that all unauthorized messages are detected."""

    detector = CANSecurityDetector()
    results = detector.analyze()

    unauthorized_count = (
        results["detected_attack"] == "UNAUTHORIZED"
    ).sum()

    assert unauthorized_count == 5


def test_total_anomalies_detected():
    """Verify that all 20 anomalous messages are detected."""

    detector = CANSecurityDetector()
    results = detector.analyze()

    anomalous_count = (
        results["detected_status"] == "ANOMALOUS"
    ).sum()

    assert anomalous_count == 20


def test_total_message_count():
    """Verify that the security dataset contains 60 messages."""

    detector = CANSecurityDetector()
    results = detector.analyze()

    assert len(results) == 60