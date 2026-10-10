
from pathlib import Path

import pandas as pd

from bms_model import BMS


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "battery_data.csv"


def main():
    # Load simulator data
    df = pd.read_csv(DATA_FILE)

    # Use the first sample as the baseline
    row = df.iloc[0]

    bms = BMS()
    bms.pack_voltage = float(row["Voltage_V"])
    bms.current = float(row["Current_A"])
    bms.temperature = float(row["Temperature_C"])
    bms.soc = float(row["SOC_percent"])
    bms.soh = float(row["SOH_percent"])

    print("AegisCAN Integrated BMS Fault Test")
    print("==================================")

    # Inject a simulated over-temperature fault
    bms.temperature = 75.0

    print(f"Injected temperature: {bms.temperature:.2f} °C")

    bms.check_protection()
    bms.control_contactor()
    bms.display_status()

    # Verify expected safety response
    assert bms.fault_state == "OVER_TEMPERATURE"
    assert bms.contactor_closed is False

    print("\nPASS: Over-temperature detected.")
    print("PASS: Contactor opened.")


if __name__ == "__main__":
    main()
