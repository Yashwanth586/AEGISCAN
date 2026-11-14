"""AEGISCAN Week 5: Decode simulated CAN frames into BMS values."""

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "can_log.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "decoded_can_data.csv"


def decode_uint16(payload, start_byte):
    """Decode a little-endian unsigned 16-bit signal."""
    raw = bytes.fromhex(payload)
    signal_bytes = raw[start_byte:start_byte + 2]
    return int.from_bytes(
        signal_bytes,
        byteorder="little",
        signed=False,
    )


def decode_int16(payload, start_byte):
    """Decode a little-endian signed 16-bit signal."""
    raw = bytes.fromhex(payload)
    signal_bytes = raw[start_byte:start_byte + 2]
    return int.from_bytes(
        signal_bytes,
        byteorder="little",
        signed=True,
    )


def decode_frame(can_id, data):
    """Decode one simulated CAN frame into engineering values."""

    result = {}

    if can_id == "0x180":
        result["Voltage_V"] = decode_uint16(data, 0) * 0.1
        result["Current_A"] = decode_int16(data, 2) * 0.1

    elif can_id == "0x200":
        result["SOC_percent"] = decode_uint16(data, 0) * 0.1
        result["SOH_percent"] = decode_uint16(data, 2) * 0.1

    elif can_id == "0x300":
        result["Temperature_C"] = decode_int16(data, 0) * 0.1
        result["Fault_Code"] = int(bytes.fromhex(data)[2])

    elif can_id == "0x400":
        status_bits = int(bytes.fromhex(data)[0])
        fault_code = int(bytes.fromhex(data)[1])

        result["Contactor"] = (
            "CLOSED" if status_bits & 0x01 else "OPEN"
        )

        result["Balancing"] = (
            "ACTIVE" if status_bits & 0x02 else "INACTIVE"
        )

        result["Health_Fault_Code"] = fault_code

    return result


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"CAN log not found: {INPUT_FILE}"
        )

    df = pd.read_csv(INPUT_FILE)

    decoded_rows = []

    for _, row in df.iterrows():
        decoded = decode_frame(
            str(row["CAN_ID"]),
            str(row["Data"])
        )

        decoded["Timestamp_s"] = row["Timestamp_s"]
        decoded["CAN_ID"] = row["CAN_ID"]

        decoded_rows.append(decoded)

    decoded_df = pd.DataFrame(decoded_rows)

    preferred_columns = [
        "Timestamp_s",
        "CAN_ID",
        "Voltage_V",
        "Current_A",
        "SOC_percent",
        "SOH_percent",
        "Temperature_C",
        "Fault_Code",
        "Contactor",
        "Balancing",
        "Health_Fault_Code",
    ]

    columns = [
        column
        for column in preferred_columns
        if column in decoded_df.columns
    ]

    decoded_df = decoded_df[columns]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    decoded_df.to_csv(OUTPUT_FILE, index=False)

    print("\nAEGISCAN CAN Decoder")
    print("=" * 27)
    print(decoded_df.to_string(index=False))

    print("\nDecoded data saved to:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()