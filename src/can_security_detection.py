# AegisCAN Week 8 - CAN Security Detection
#
# Purpose:
# Analyze the simulated CAN security dataset and classify
# normal and anomalous CAN traffic.
#
# Detection scenarios:
# 1. Spoofing
# 2. Replay
# 3. Flooding
# 4. Unauthorized CAN message
#
# Simulation-only cybersecurity analysis.

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "security_dataset.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "security_detection_results.csv"


AUTHORIZED_CAN_IDS = {
    "0x180": "battery_measurements",
    "0x200": "battery_status",
    "0x300": "thermal_status",
    "0x400": "bms_health",
}


FREQUENCY_THRESHOLDS = {
    "0x180": 500.0,
    "0x200": 250.0,
    "0x300": 250.0,
    "0x400": 100.0,
}


class CANSecurityDetector:
    """Detect simulated CAN cybersecurity anomalies."""

    def __init__(self):
        self.results = []

    def detect_unauthorized(self, row):
        """Detect CAN IDs that are not authorized."""

        return row["can_id"] not in AUTHORIZED_CAN_IDS

    def detect_flooding(self, row):
        """Detect excessive CAN message frequency."""

        threshold = FREQUENCY_THRESHOLDS.get(
            row["can_id"],
            100.0
        )

        return row["frequency_hz"] > threshold

    def detect_spoofing(self, row):
        """
        Detect the simulated spoofed battery payload.
        """

        return (
            row["can_id"] == "0x180"
            and row["data"] == "FF FF FF FF FF FF FF FF"
        )

    def find_replay_indices(self, dataframe):
        """
        Detect replay sequences.

        A replay is identified when the same authorized 0x180
        payload appears repeatedly in a short sequence.

        At least three consecutive repeated messages are required
        before the sequence is classified as replay traffic.
        """

        replay_indices = set()

        for i in range(len(dataframe) - 2):

            row1 = dataframe.iloc[i]
            row2 = dataframe.iloc[i + 1]
            row3 = dataframe.iloc[i + 2]

            same_id = (
                row1["can_id"] == "0x180"
                and row2["can_id"] == "0x180"
                and row3["can_id"] == "0x180"
            )

            same_data = (
                row1["data"] == row2["data"]
                and row2["data"] == row3["data"]
            )

            close_timing = (
                row2["timestamp"] - row1["timestamp"] <= 0.02
                and row3["timestamp"] - row2["timestamp"] <= 0.02
            )

            if same_id and same_data and close_timing:

                replay_indices.add(i)
                replay_indices.add(i + 1)
                replay_indices.add(i + 2)

                # Continue forward through the replay sequence.
                j = i + 3

                while j < len(dataframe):

                    previous = dataframe.iloc[j - 1]
                    current = dataframe.iloc[j]

                    if (
                        current["can_id"] == "0x180"
                        and current["data"] == previous["data"]
                        and current["timestamp"] -
                        previous["timestamp"] <= 0.02
                    ):
                        replay_indices.add(j)
                        j += 1
                    else:
                        break

        return replay_indices

    def analyze(self):
        """Analyze the complete security dataset."""

        if not DATA_FILE.exists():
            raise FileNotFoundError(
                f"Security dataset not found: {DATA_FILE}"
            )

        dataframe = pd.read_csv(DATA_FILE)

        replay_indices = self.find_replay_indices(dataframe)

        self.results = []

        for index, row in dataframe.iterrows():

            status = "NORMAL"
            attack = "NONE"
            reason = "Normal authorized CAN traffic"

            if self.detect_unauthorized(row):

                status = "ANOMALOUS"
                attack = "UNAUTHORIZED"

                reason = (
                    "CAN ID is not present in the authorized CAN ID list"
                )

            elif self.detect_flooding(row):

                status = "ANOMALOUS"
                attack = "FLOODING"

                reason = (
                    "CAN message frequency exceeds the configured threshold"
                )

            elif self.detect_spoofing(row):

                status = "ANOMALOUS"
                attack = "SPOOFING"

                reason = (
                    "Authorized CAN ID contains the simulated spoofed payload"
                )

            elif index in replay_indices:

                status = "ANOMALOUS"
                attack = "REPLAY"

                reason = (
                    "Repeated CAN message sequence detected within "
                    "a suspicious interval"
                )

            self.results.append(
                {
                    "timestamp": row["timestamp"],
                    "can_id": row["can_id"],
                    "original_label": row["label"],
                    "detected_status": status,
                    "detected_attack": attack,
                    "detection_reason": reason,
                }
            )

        results = pd.DataFrame(self.results)

        results.to_csv(OUTPUT_FILE, index=False)

        return results

    def print_summary(self, results):
        """Print the security detection summary."""

        print("\nAegisCAN Week 8")
        print("==============================")
        print("CAN Security Detection")
        print("==============================")

        print("\nInput dataset:")
        print(DATA_FILE)

        print("\nDetection results saved to:")
        print(OUTPUT_FILE)

        print("\nDetected status:")
        print(results["detected_status"].value_counts())

        print("\nDetected attack types:")
        print(results["detected_attack"].value_counts())

        print("\nDetection summary:")
        print("------------------")

        for attack in [
            "SPOOFING",
            "REPLAY",
            "FLOODING",
            "UNAUTHORIZED",
        ]:

            count = len(
                results[results["detected_attack"] == attack]
            )

            print(f"{attack:15} : {count} detected")


def main():

    detector = CANSecurityDetector()

    results = detector.analyze()

    detector.print_summary(results)

    print("\nFirst 15 detection results:")
    print("----------------------------")

    print(
        results.head(15).to_string(index=False)
    )

    print(
        "\nWeek 8 CAN security detection completed successfully."
    )


if __name__ == "__main__":
    main()