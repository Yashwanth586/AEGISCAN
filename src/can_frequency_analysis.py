import pandas as pd
from pathlib import Path


INPUT_FILE = Path("data/can_log.csv")
OUTPUT_FILE = Path("data/can_frequency_analysis.csv")


def analyze_frequency():
    print("AEGISCAN CAN Message Frequency Analysis")
    print("=" * 45)

    df = pd.read_csv(INPUT_FILE)

    required_columns = {"Timestamp_s", "CAN_ID"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    results = []

    for can_id, group in df.groupby("CAN_ID"):
        timestamps = group["Timestamp_s"].sort_values()

        count = len(timestamps)

        if count > 1:
            duration = timestamps.iloc[-1] - timestamps.iloc[0]

            if duration > 0:
                frequency_hz = (count - 1) / duration
            else:
                frequency_hz = 0.0
        else:
            duration = 0.0
            frequency_hz = 0.0

        results.append(
            {
                "CAN_ID": can_id,
                "Frame_Count": count,
                "Start_Time_s": timestamps.iloc[0],
                "End_Time_s": timestamps.iloc[-1],
                "Duration_s": duration,
                "Frequency_Hz": frequency_hz,
            }
        )

    result_df = pd.DataFrame(results)
    result_df = result_df.sort_values("CAN_ID")

    result_df.to_csv(OUTPUT_FILE, index=False)

    print("\nMessage Frequency Analysis")
    print(result_df.to_string(index=False))

    print("\nFrequency analysis saved to:")
    print(OUTPUT_FILE.resolve())


if __name__ == "__main__":
    analyze_frequency()