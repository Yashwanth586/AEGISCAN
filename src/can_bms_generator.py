
"""AEGISCAN Week 4: Encode BMS measurements as simulated CAN frames."""

from pathlib import Path
import pandas as pd

from bms_model import BMS

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = PROJECT_ROOT / "data" / "bms_can_frames.csv"

# Project-defined CAN IDs for this educational simulation.
CAN_IDS = {
    "battery_measurements": 0x180,
    "battery_status": 0x200,
    "thermal_status": 0x300,
    "bms_health": 0x400,
}

FAULT_CODES = {
    "NORMAL": 0,
    "OVER_VOLTAGE": 1,
    "UNDER_VOLTAGE": 2,
    "OVER_CURRENT": 3,
    "OVER_TEMPERATURE": 4,
}


def unsigned_16(value):
    """Encode an unsigned 16-bit integer in little-endian order."""
    if not 0 <= value <= 65535:
        raise ValueError(f"Value outside uint16 range: {value}")
    return value.to_bytes(2, byteorder="little", signed=False)


def signed_16(value):
    """Encode a signed 16-bit integer in little-endian order."""
    if not -32768 <= value <= 32767:
        raise ValueError(f"Value outside int16 range: {value}")
    return value.to_bytes(2, byteorder="little", signed=True)


def make_frame(can_id, payload):
    """Create a classic CAN frame representation."""
    if not 0 <= can_id <= 0x7FF:
        raise ValueError("CAN ID must be an 11-bit standard identifier.")
    if len(payload) != 8:
        raise ValueError("Classic CAN payload must contain 8 bytes.")

    return {
        "CAN_ID": f"0x{can_id:03X}",
        "DLC": len(payload),
        "Data": payload.hex().upper(),
    }


def encode_bms_messages(bms):
    """Convert selected BMS values into four simulated CAN frames."""

    # Run the simplified BMS diagnostic logic first.
    bms.check_protection()
    bms.control_contactor()

    # Scale physical values into integer representations.
    voltage_raw = round(bms.pack_voltage * 10)  # 0.1 V/bit
    current_raw = round(bms.current * 10)        # 0.1 A/bit
    soc_raw = round(bms.soc * 10)                # 0.1 %/bit
    soh_raw = round(bms.soh * 10)                # 0.1 %/bit
    temperature_raw = round(bms.temperature * 10)  # 0.1 °C/bit

    if not 0 <= soc_raw <= 1000:
        raise ValueError("SOC must be between 0 and 100%.")
    if not 0 <= soh_raw <= 1000:
        raise ValueError("SOH must be between 0 and 100%.")
    if not -400 <= temperature_raw <= 1250:
        raise ValueError("Temperature is outside the configured demo range.")

    fault_code = FAULT_CODES.get(bms.fault_state)
    if fault_code is None:
        raise ValueError(f"Unknown fault state: {bms.fault_state}")

    # 0x180: bytes 0-1 voltage; bytes 2-3 signed current.
    frame_battery = (
        unsigned_16(voltage_raw)
        + signed_16(current_raw)
        + bytes(4)
    )

    # 0x200: bytes 0-1 SOC; bytes 2-3 SOH.
    frame_status = (
        unsigned_16(soc_raw)
        + unsigned_16(soh_raw)
        + bytes(4)
    )

    # 0x300: bytes 0-1 signed temperature; byte 2 fault code.
    frame_thermal = (
        signed_16(temperature_raw)
        + bytes([fault_code])
        + bytes(5)
    )

    # 0x400: byte 0 bit 0 = contactor closed;
    #        byte 0 bit 1 = balancing active; byte 1 = fault code.
    status_bits = (
        (1 if bms.contactor_closed else 0)
        | (2 if bms.balancing_active else 0)
    )
    frame_health = bytes([status_bits, fault_code]) + bytes(6)

    return [
        make_frame(CAN_IDS["battery_measurements"], frame_battery),
        make_frame(CAN_IDS["battery_status"], frame_status),
        make_frame(CAN_IDS["thermal_status"], frame_thermal),
        make_frame(CAN_IDS["bms_health"], frame_health),
    ]


def main():
    bms = BMS()
    bms.check_cell_balance()

    frames = encode_bms_messages(bms)

    # This is simulated frame data, not a live physical CAN bus capture.
    for index, frame in enumerate(frames):
        frame["Timestamp_s"] = round(index * 0.01, 3)

    columns = ["Timestamp_s", "CAN_ID", "DLC", "Data"]
    df = pd.DataFrame(frames)[columns]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("\nAEGISCAN BMS-to-CAN Generator")
    print("=" * 36)
    print(df.to_string(index=False))
    print(f"\nSaved {len(df)} simulated frames to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()
