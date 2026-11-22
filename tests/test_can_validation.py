"""AEGISCAN Week 6 - CAN validation tests."""

import sys
from pathlib import Path

# Add src/ to Python import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_DIR))

from bms_model import BMS
from can_bms_generator import (
    CAN_IDS,
    FAULT_CODES,
    encode_bms_messages,
    make_frame,
    unsigned_16,
    signed_16,
)
from can_decoder import decode_frame


def test_can_id_battery_measurements():
    """TC-14: Battery measurements should use CAN ID 0x180."""
    assert CAN_IDS["battery_measurements"] == 0x180


def test_can_id_battery_status():
    """TC-15: Battery status should use CAN ID 0x200."""
    assert CAN_IDS["battery_status"] == 0x200


def test_can_id_thermal_status():
    """TC-16: Thermal status should use CAN ID 0x300."""
    assert CAN_IDS["thermal_status"] == 0x300


def test_can_id_bms_health():
    """TC-17: BMS health should use CAN ID 0x400."""
    assert CAN_IDS["bms_health"] == 0x400


def test_generated_frame_has_eight_byte_payload():
    """TC-18: Every generated classic CAN frame must contain 8 data bytes."""
    bms = BMS()
    bms.check_cell_balance()

    frames = encode_bms_messages(bms)

    assert len(frames) == 4

    for frame in frames:
        assert frame["DLC"] == 8
        assert len(frame["Data"]) == 16


def test_battery_measurement_encoding_and_decoding():
    """TC-19: Voltage and current should survive CAN encode/decode."""
    bms = BMS()
    bms.pack_voltage = 400.0
    bms.current = 50.0

    frames = encode_bms_messages(bms)

    frame = next(
        frame for frame in frames
        if frame["CAN_ID"] == "0x180"
    )

    decoded = decode_frame(frame["CAN_ID"], frame["Data"])

    assert decoded["Voltage_V"] == 400.0
    assert decoded["Current_A"] == 50.0


def test_battery_status_encoding_and_decoding():
    """TC-20: SOC and SOH should survive CAN encode/decode."""
    bms = BMS()
    bms.soc = 75.0
    bms.soh = 98.0

    frames = encode_bms_messages(bms)

    frame = next(
        frame for frame in frames
        if frame["CAN_ID"] == "0x200"
    )

    decoded = decode_frame(frame["CAN_ID"], frame["Data"])

    assert decoded["SOC_percent"] == 75.0
    assert decoded["SOH_percent"] == 98.0


def test_temperature_and_fault_encoding():
    """TC-21: Temperature and fault code should be correctly encoded."""
    bms = BMS()
    bms.temperature = 32.0

    frames = encode_bms_messages(bms)

    frame = next(
        frame for frame in frames
        if frame["CAN_ID"] == "0x300"
    )

    decoded = decode_frame(frame["CAN_ID"], frame["Data"])

    assert decoded["Temperature_C"] == 32.0
    assert decoded["Fault_Code"] == FAULT_CODES["NORMAL"]


def test_over_temperature_fault_code():
    """TC-22: Over-temperature should produce fault code 4."""
    bms = BMS()
    bms.temperature = 61.0

    frames = encode_bms_messages(bms)

    frame = next(
        frame for frame in frames
        if frame["CAN_ID"] == "0x300"
    )

    decoded = decode_frame(frame["CAN_ID"], frame["Data"])

    assert decoded["Fault_Code"] == 4


def test_contactor_status_encoding():
    """TC-23: A normal BMS condition should encode a CLOSED contactor."""
    bms = BMS()
    bms.check_cell_balance()

    frames = encode_bms_messages(bms)

    frame = next(
        frame for frame in frames
        if frame["CAN_ID"] == "0x400"
    )

    decoded = decode_frame(frame["CAN_ID"], frame["Data"])

    assert decoded["Contactor"] == "CLOSED"
    assert decoded["Balancing"] == "INACTIVE"


def test_fault_opens_contactor_in_can_health_frame():
    """TC-24: A BMS fault should be reflected as OPEN contactor."""
    bms = BMS()
    bms.temperature = 61.0
    bms.check_cell_balance()

    frames = encode_bms_messages(bms)

    frame = next(
        frame for frame in frames
        if frame["CAN_ID"] == "0x400"
    )

    decoded = decode_frame(frame["CAN_ID"], frame["Data"])

    assert decoded["Contactor"] == "OPEN"
    assert decoded["Health_Fault_Code"] == 4


def test_invalid_can_id_is_rejected():
    """TC-25: CAN IDs above the 11-bit range should be rejected."""
    payload = bytes(8)

    try:
        make_frame(0x800, payload)
        assert False, "Invalid CAN ID was accepted."
    except ValueError:
        assert True


def test_invalid_payload_length_is_rejected():
    """TC-26: CAN payloads other than 8 bytes should be rejected."""
    try:
        make_frame(0x180, bytes(7))
        assert False, "Invalid payload length was accepted."
    except ValueError:
        assert True


def test_unsigned_16_boundary_values():
    """TC-27: uint16 encoder should accept its valid boundaries."""
    assert unsigned_16(0) == b"\x00\x00"
    assert unsigned_16(65535) == b"\xff\xff"


def test_signed_16_boundary_values():
    """TC-28: int16 encoder should accept signed boundary values."""
    assert signed_16(-32768) == b"\x00\x80"
    assert signed_16(32767) == b"\xff\x7f"