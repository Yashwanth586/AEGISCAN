"""
AEGISCAN Week 7 - Fault Injection Tests

Automated validation of the five controlled fault scenarios
required for Week 7.
"""

from src.fault_injection import FaultInjection


def test_voltage_fault_injection():
    injector = FaultInjection()

    result = injector.inject_voltage_fault(500.0)

    assert result["observed_fault"] == "OVER_VOLTAGE"
    assert result["contactor"] == "OPEN"


def test_temperature_fault_injection():
    injector = FaultInjection()

    result = injector.inject_temperature_fault(75.0)

    assert result["observed_fault"] == "OVER_TEMPERATURE"
    assert result["contactor"] == "OPEN"


def test_invalid_soc_injection():
    injector = FaultInjection()

    result = injector.inject_invalid_soc(120.0)

    assert result["observed_fault"] == "INVALID_SOC_REJECTED"


def test_missing_can_message_injection():
    injector = FaultInjection()

    result = injector.inject_missing_can_message("0x300")

    assert result["observed_fault"] == "MISSING_CAN_MESSAGE"
    assert result["injected_can_id"] == "0x300"


def test_abnormal_can_frequency_injection():
    injector = FaultInjection()

    result = injector.inject_abnormal_frequency(
        can_id="0x180",
        abnormal_frequency_hz=1000.0,
        threshold_hz=500.0,
    )

    assert result["observed_fault"] == "ABNORMAL_CAN_FREQUENCY"
    assert result["injected_frequency_hz"] > result["threshold_hz"]