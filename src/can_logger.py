import pandas as pd
from pathlib import Path


INPUT_FILE = Path("data/bms_can_frames.csv")
OUTPUT_FILE = Path("data/can_log.csv")

CYCLES = 10
CYCLE_INTERVAL_S = 0.04


def load_can_frames():
    df = pd.read_csv(INPUT_FILE)

    required_columns = {"Timestamp_s", "CAN_ID", "DLC", "Data"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if not (df["DLC"] == 8).all():
        raise ValueError("Unexpected DLC detected.")

    if df["Data"].astype(str).str.len().ne(16).any():
        raise ValueError("Invalid CAN payload length detected.")

    return df


def generate_repeated_log(df):
    records = []

    frame_offsets = (
        df["Timestamp_s"] - df["Timestamp_s"].iloc[0]
    ).tolist()

    for cycle in range(CYCLES):
        cycle_start = cycle * CYCLE_INTERVAL_S

        for _, row in df.iterrows():
            frame_index = len(records) % len(frame_offsets)

            timestamp = cycle_start + frame_offsets[frame_index]

            records.append(
                {
                    "Timestamp_s": round(timestamp, 4),
                    "CAN_ID": row["CAN_ID"],
                    "DLC": int(row["DLC"]),
                    "Data": row["Data"],
                }
            )

    return pd.DataFrame(records)


def calculate_timing(log_df):
    log_df["Delta_t_s"] = log_df["Timestamp_s"].diff()

    total_duration = (
        log_df["Timestamp_s"].iloc[-1]
        - log_df["Timestamp_s"].iloc[0]
    )

    if total_duration > 0:
        frame_rate = (len(log_df) - 1) / total_duration
    else:
        frame_rate = 0.0

    log_df["Frame_Rate_Hz"] = round(frame_rate, 3)

    return log_df, frame_rate


def main():
    print("AEGISCAN CAN Logger")
    print("=" * 30)

    source_df = load_can_frames()
    log_df = generate_repeated_log(source_df)
    log_df, frame_rate = calculate_timing(log_df)

    log_df.to_csv(OUTPUT_FILE, index=False)

    print("\nGenerated CAN log:")
    print(log_df.to_string(index=False))

    print(f"\nFrames logged: {len(log_df)}")
    print(f"Start time: {log_df['Timestamp_s'].iloc[0]:.4f} s")
    print(f"End time: {log_df['Timestamp_s'].iloc[-1]:.4f} s")
    print(f"Average frame rate: {frame_rate:.3f} Hz")

    print(f"\nSaved to: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()