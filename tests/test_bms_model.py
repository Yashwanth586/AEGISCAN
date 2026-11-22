"""AEGISCAN Week 6 - Automated BMS Validation Tests."""

import sys
from pathlib import Path

# Add src/ to Python import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from bms_model import BMS


def test_normal_battery_condition():
    """TC-01: Normal battery parameters should produce NORMAL state."""
    bms = BMS()

    bms.pack_voltage = 400.0
    bms.current = 50.0
    bms.temperature = 32.0

    bms.check_protection()

    assert bms.fault_state == "NORMAL"


def test_over_voltage_detection():
    """TC-02: Voltage above 450 V should trigger over-voltage."""
    bms = BMS()
    bms.pack_voltage = 451.0

    bms.check_protection()

    assert bms.fault_state == "OVER_VOLTAGE"


def test_under_voltage_detection():
    """TC-03: Voltage below 300 V should trigger under-voltage."""
    bms = BMS()
    bms.pack_voltage = 299.0

    bms.check_protection()

    assert bms.fault_state == "UNDER_VOLTAGE"


def test_over_current_detection():
    """TC-04: Current above 200 A should trigger over-current."""
    bms = BMS()
    bms.current = 201.0

    bms.check_protection()

    assert bms.fault_state == "OVER_CURRENT"


def test_over_temperature_detection():
    """TC-05: Temperature above 60 °C should trigger over-temperature."""
    bms = BMS()
    bms.temperature = 61.0

    bms.check_protection()

    assert bms.fault_state == "OVER_TEMPERATURE"


def test_voltage_upper_boundary():
    """TC-06: Voltage exactly at 450 V should remain NORMAL."""
    bms = BMS()
    bms.pack_voltage = 450.0

    bms.check_protection()

    assert bms.fault_state == "NORMAL"


def test_voltage_lower_boundary():
    """TC-07: Voltage exactly at 300 V should remain NORMAL."""
    bms = BMS()
    bms.pack_voltage = 300.0

    bms.check_protection()

    assert bms.fault_state == "NORMAL"


def test_current_upper_boundary():
    """TC-08: Current exactly at 200 A should remain NORMAL."""
    bms = BMS()
    bms.current = 200.0

    bms.check_protection()

    assert bms.fault_state == "NORMAL"


def test_temperature_upper_boundary():
    """TC-09: Temperature exactly at 60 °C should remain NORMAL."""
    bms = BMS()
    bms.temperature = 60.0

    bms.check_protection()

    assert bms.fault_state == "NORMAL"


def test_contactor_opens_during_fault():
    """TC-10: A detected fault should open the contactor."""
    bms = BMS()
    bms.temperature = 75.0

    bms.check_protection()
    bms.control_contactor()

    assert bms.fault_state == "OVER_TEMPERATURE"
    assert bms.contactor_closed is False


def test_contactor_closed_during_normal_operation():
    """TC-11: Normal operation should keep the contactor closed."""
    bms = BMS()

    bms.check_protection()
    bms.control_contactor()

    assert bms.fault_state == "NORMAL"
    assert bms.contactor_closed is True


def test_cell_balancing_inactive_when_cells_are_balanced():
    """TC-12: Small cell voltage difference should not activate balancing."""
    bms = BMS()
    bms.cell_voltages = [3.70, 3.71, 3.69, 3.70]

    bms.check_cell_balance()

    assert bms.balancing_active is False


def test_cell_balancing_active_when_difference_exceeds_threshold():
    """TC-13: Cell voltage difference above 0.05 V should activate balancing."""
    bms = BMS()
    bms.cell_voltages = [3.70, 3.80, 3.69, 3.70]

    bms.check_cell_balance()

    assert bms.balancing_active is True