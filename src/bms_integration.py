
# AegisCAN: Battery Simulator + BMS Integration

from pathlib import Path

import pandas as pd

from bms_model import BMS


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "battery_data.csv"


def main():
    # Load the battery simulator output
    df = pd.read_csv(DATA_FILE)

    print("AegisCAN Battery Simulator + BMS Integration")
    print("=" * 48)

    # Process each simulated battery sample
    for index, row in df.iterrows():
        bms = BMS()

        # Feed simulator measurements into the BMS
        bms.pack_voltage = float(row["Voltage_V"])
        bms.current = float(row["Current_A"])
        bms.temperature = float(row["Temperature_C"])
        bms.soc = float(row["SOC_percent"])
        bms.soh = float(row["SOH_percent"])

        print(f"\n--- Sample {index + 1} ---")

        # BMS sensing, protection, and safety response
        bms.sense_parameters()
        bms.check_protection()
        bms.check_cell_balance()
        bms.control_contactor()
        bms.display_status()


if __name__ == "__main__":
    main()
