
"""Test BMS fault encoding in the AEGISCAN CAN generator."""

from bms_model import BMS
from can_bms_generator import encode_bms_messages


def main():
    bms = BMS()

    # Inject a simulated overtemperature fault.
    bms.temperature = 75.0
    bms.check_cell_balance()

    frames = encode_bms_messages(bms)
    by_id = {frame["CAN_ID"]: frame for frame in frames}

    thermal_payload = bytes.fromhex(by_id["0x300"]["Data"])
    health_payload = bytes.fromhex(by_id["0x400"]["Data"])

    # Temperature is a signed little-endian value, scaled by 0.1 °C.
    raw_temperature = int.from_bytes(
        thermal_payload[0:2], byteorder="little", signed=True
    )
    decoded_temperature = raw_temperature * 0.1

    # Byte 2 contains the fault code.
    fault_code = thermal_payload[2]

    # Byte 0 bit 0: contactor closed; bit 1: balancing active.
    contactor_closed = bool(health_payload[0] & 0b00000001)
    health_fault_code = health_payload[1]

    assert abs(decoded_temperature - 75.0) < 0.001
    assert fault_code == 4, f"Unexpected thermal fault code: {fault_code}"
    assert contactor_closed is False, "Contactor should be OPEN"
    assert health_fault_code == 4, "Health frame should report fault code 4"

    print("\nCAN Fault Test")
    print("==============")
    print(f"Temperature: {decoded_temperature:.1f} °C")
    print(f"Thermal fault code: {fault_code} (OVER_TEMPERATURE)")
    print(f"Contactor: {'CLOSED' if contactor_closed else 'OPEN'}")
    print(f"Health fault code: {health_fault_code}")
    print("\nPASS: BMS fault is correctly represented in CAN frames.")


if __name__ == "__main__":
    main()
