"""
AEGISCAN Week 7 - Fault Injection and Root Cause Analysis

This module provides controlled fault injection for the simulated
BMS/CAN system and returns observations and diagnostic information.
"""

from pathlib import Path
import pandas as pd

from .bms_model import BMS


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class FaultInjection:

    def inject_voltage_fault(self, voltage=500.0):
        """Inject an over-voltage condition into the BMS."""

        bms = BMS()
        bms.pack_voltage = voltage

        bms.check_protection()
        bms.control_contactor()

        return {
            "fault": "OVER_VOLTAGE",
            "injected_value": voltage,
            "observed_fault": bms.fault_state,
            "contactor": (
                "CLOSED" if bms.contactor_closed else "OPEN"
            ),
            "diagnosis": (
                "Pack voltage exceeded the configured upper limit "
                "of 450 V."
            ),
            "root_cause": (
                "Controlled injection increased pack voltage above "
                "the BMS over-voltage threshold."
            ),
        }

    def inject_temperature_fault(self, temperature=75.0):
        """Inject an over-temperature condition into the BMS."""

        bms = BMS()
        bms.temperature = temperature

        bms.check_protection()
        bms.control_contactor()

        return {
            "fault": "OVER_TEMPERATURE",
            "injected_value": temperature,
            "observed_fault": bms.fault_state,
            "contactor": (
                "CLOSED" if bms.contactor_closed else "OPEN"
            ),
            "diagnosis": (
                "Battery temperature exceeded the configured "
                "upper limit of 60 °C."
            ),
            "root_cause": (
                "Controlled injection increased battery temperature "
                "above the BMS over-temperature threshold."
            ),
        }

    def inject_invalid_soc(self, soc=120.0):
        """Inject an invalid SOC value and verify CAN validation."""

        bms = BMS()
        bms.soc = soc

        result = {
            "fault": "INVALID_SOC",
            "injected_value": soc,
        }

        try:
            # Import the CAN generator directly from the src directory.
            # This avoids changing the existing Week 4 CAN generator.
            import sys

            src_path = str(PROJECT_ROOT / "src")

            if src_path not in sys.path:
                sys.path.insert(0, src_path)

            from can_bms_generator import encode_bms_messages

            encode_bms_messages(bms)

            result["observed_fault"] = "NOT_DETECTED"
            result["diagnosis"] = (
                "Invalid SOC was not rejected during CAN encoding."
            )
            result["root_cause"] = (
                "SOC validation did not reject the injected value."
            )

        except ValueError as error:
            result["observed_fault"] = "INVALID_SOC_REJECTED"
            result["diagnosis"] = (
                f"Invalid SOC rejected during CAN encoding: {error}"
            )
            result["root_cause"] = (
                "Injected SOC exceeded the valid 0–100% range."
            )

        return result

    def inject_missing_can_message(self, missing_can_id="0x300"):
        """Remove a required CAN message and diagnose the missing frame."""

        can_file = PROJECT_ROOT / "data" / "can_data.csv"

        if not can_file.exists():
            raise FileNotFoundError(
                f"CAN data file not found: {can_file}"
            )

        df = pd.read_csv(can_file)

        required_ids = {
            "0x180",
            "0x200",
            "0x300",
            "0x400",
        }

        observed_ids = set(
            df["CAN_ID"].astype(str)
        )

        if missing_can_id in observed_ids:
            modified_df = df[
                df["CAN_ID"].astype(str) != missing_can_id
            ]
        else:
            modified_df = df.copy()

        modified_ids = set(
            modified_df["CAN_ID"].astype(str)
        )

        missing_ids = required_ids - modified_ids

        if missing_ids:
            diagnosis = (
                f"Required CAN message {missing_can_id} is missing "
                "from the simulated traffic."
            )

            root_cause = (
                "The controlled fault injection removed the required "
                f"CAN message with ID {missing_can_id}."
            )

            observed_fault = "MISSING_CAN_MESSAGE"

        else:
            diagnosis = (
                "No required CAN message is missing."
            )

            root_cause = (
                "No missing-message condition was injected."
            )

            observed_fault = "NORMAL"

        return {
            "fault": "MISSING_CAN_MESSAGE",
            "injected_can_id": missing_can_id,
            "observed_fault": observed_fault,
            "diagnosis": diagnosis,
            "root_cause": root_cause,
        }

    def inject_abnormal_frequency(
        self,
        can_id="0x180",
        normal_frequency_hz=100.0,
        abnormal_frequency_hz=1000.0,
        threshold_hz=500.0,
    ):
        """Inject and diagnose an abnormally high CAN message frequency."""

        abnormal = (
            abnormal_frequency_hz > threshold_hz
        )

        if abnormal:
            observed_fault = "ABNORMAL_CAN_FREQUENCY"

            diagnosis = (
                f"CAN ID {can_id} frequency of "
                f"{abnormal_frequency_hz:.1f} Hz exceeds the "
                f"configured threshold of "
                f"{threshold_hz:.1f} Hz."
            )

            root_cause = (
                "Controlled injection generated CAN messages "
                "at an excessively high frequency."
            )

        else:
            observed_fault = "NORMAL"

            diagnosis = (
                f"CAN ID {can_id} frequency is within the "
                "configured range."
            )

            root_cause = (
                "No abnormal frequency condition was injected."
            )

        return {
            "fault": "ABNORMAL_CAN_FREQUENCY",
            "can_id": can_id,
            "normal_frequency_hz": normal_frequency_hz,
            "injected_frequency_hz": abnormal_frequency_hz,
            "threshold_hz": threshold_hz,
            "observed_fault": observed_fault,
            "diagnosis": diagnosis,
            "root_cause": root_cause,
        }


def main():
    injector = FaultInjection()

    print("AEGISCAN Week 7 - Fault Injection")
    print("=" * 40)

    scenarios = [
        injector.inject_voltage_fault(),
        injector.inject_temperature_fault(),
        injector.inject_invalid_soc(),
        injector.inject_missing_can_message(),
        injector.inject_abnormal_frequency(),
    ]

    for result in scenarios:
        print("\n--- Fault Injection Result ---")

        for key, value in result.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()