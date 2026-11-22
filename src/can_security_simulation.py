# AegisCAN Week 8 - CAN Cybersecurity Simulation
#
# Purpose:
# Simulate normal and abnormal CAN traffic for cybersecurity analysis.
#
# Security scenarios:
# 1. Spoofing
# 2. Replay
# 3. Flooding
# 4. Unauthorized CAN message
#
# This module is simulation-only and does not interact with a real CAN bus.

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_FILE = DATA_DIR / "security_dataset.csv"


AUTHORIZED_CAN_IDS = {
    "0x180": "battery_measurements",
    "0x200": "battery_status",
    "0x300": "thermal_status",
    "0x400": "bms_health",
}


class CANSecuritySimulation:
    """Generate controlled normal and abnormal CAN security scenarios."""

    def __init__(self):
        self.rows = []

    def add_message(
        self,
        timestamp,
        can_id,
        data,
        frequency_hz,
        label,
        attack_type,
        description,
    ):
        message_type = AUTHORIZED_CAN_IDS.get(can_id, "unknown")

        self.rows.append(
            {
                "timestamp": timestamp,
                "can_id": can_id,
                "data": data,
                "frequency_hz": frequency_hz,
                "message_type": message_type,
                "label": label,
                "attack_type": attack_type,
                "description": description,
            }
        )

    def generate_normal_traffic(self):
        """Generate normal authorized CAN traffic."""

        normal_messages = [
            ("0x180", "64 00 C4 09 20 00 00 00", 100.0),
            ("0x200", "DC 02 20 03 00 00 00 00", 50.0),
            ("0x300", "40 01 00 00 00 00 00 00", 50.0),
            ("0x400", "01 00 00 00 00 00 00 00", 10.0),
        ]

        timestamp = 0.01

        for cycle in range(10):
            for can_id, data, frequency in normal_messages:
                self.add_message(
                    timestamp=round(timestamp, 2),
                    can_id=can_id,
                    data=data,
                    frequency_hz=frequency,
                    label="NORMAL",
                    attack_type="NONE",
                    description="Expected authorized CAN message",
                )

                timestamp += 0.01

    def simulate_spoofing(self):
        """
        Simulate spoofing.

        The CAN ID appears legitimate, but the payload contains
        suspicious battery information.
        """

        spoofed_data = "FF FF FF FF FF FF FF FF"

        for i in range(5):
            self.add_message(
                timestamp=round(1.01 + (i * 0.01), 2),
                can_id="0x180",
                data=spoofed_data,
                frequency_hz=100.0,
                label="ANOMALOUS",
                attack_type="SPOOFING",
                description="Authorized CAN ID with abnormal payload",
            )

    def simulate_replay(self):
        """
        Simulate replay.

        Previously observed valid CAN data is repeatedly transmitted.
        """

        replayed_data = "64 00 C4 09 20 00 00 00"

        for i in range(5):
            self.add_message(
                timestamp=round(1.06 + (i * 0.01), 2),
                can_id="0x180",
                data=replayed_data,
                frequency_hz=100.0,
                label="ANOMALOUS",
                attack_type="REPLAY",
                description="Previously observed message transmitted again",
            )

    def simulate_flooding(self):
        """
        Simulate CAN flooding.

        The message frequency becomes much higher than the
        expected normal operating frequency.
        """

        for i in range(5):
            self.add_message(
                timestamp=round(1.11 + (i * 0.001), 3),
                can_id="0x180",
                data="64 00 C4 09 20 00 00 00",
                frequency_hz=1000.0,
                label="ANOMALOUS",
                attack_type="FLOODING",
                description="CAN message frequency exceeds expected threshold",
            )

    def simulate_unauthorized_message(self):
        """
        Simulate an unauthorized CAN message.

        CAN ID 0x555 is not present in the authorized CAN ID list.
        """

        for i in range(5):
            self.add_message(
                timestamp=round(1.12 + (i * 0.01), 2),
                can_id="0x555",
                data="AA BB CC DD EE FF 11 22",
                frequency_hz=20.0,
                label="ANOMALOUS",
                attack_type="UNAUTHORIZED",
                description="CAN ID is not authorized for the BMS network",
            )

    def generate_dataset(self):
        """Generate complete normal + abnormal security dataset."""

        self.rows = []

        self.generate_normal_traffic()
        self.simulate_spoofing()
        self.simulate_replay()
        self.simulate_flooding()
        self.simulate_unauthorized_message()

        dataframe = pd.DataFrame(self.rows)

        DATA_DIR.mkdir(parents=True, exist_ok=True)
        dataframe.to_csv(OUTPUT_FILE, index=False)

        return dataframe

    def print_summary(self, dataframe):
        """Display a summary of the generated security dataset."""

        print("\nAegisCAN Week 8")
        print("==============================")
        print("CAN Cybersecurity Simulation")
        print("==============================")

        print(f"\nDataset saved to:")
        print(OUTPUT_FILE)

        print("\nTotal messages:", len(dataframe))

        print("\nTraffic classification:")
        print(dataframe["label"].value_counts())

        print("\nAttack type distribution:")
        print(dataframe["attack_type"].value_counts())

        print("\nCAN ID distribution:")
        print(dataframe["can_id"].value_counts())

        print("\nSecurity scenario summary:")
        print("--------------------------")

        for attack_type in [
            "SPOOFING",
            "REPLAY",
            "FLOODING",
            "UNAUTHORIZED",
        ]:
            count = len(
                dataframe[dataframe["attack_type"] == attack_type]
            )

            print(f"{attack_type:15} : {count} messages")


def main():
    simulation = CANSecuritySimulation()

    dataframe = simulation.generate_dataset()

    simulation.print_summary(dataframe)

    print("\nFirst 10 dataset records:")
    print("-------------------------")
    print(dataframe.head(10).to_string(index=False))

    print("\nWeek 8 security dataset generation completed successfully.")


if __name__ == "__main__":
    main()