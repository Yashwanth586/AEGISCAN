# AegisCAN Week 3 - Simplified BMS Model

class BMS:
    def __init__(self):
        # Battery measurements
        self.pack_voltage = 400.0
        self.current = 50.0
        self.temperature = 32.0
        self.soc = 75.0
        self.soh = 98.0

        # Cell voltages
        self.cell_voltages = [3.70, 3.71, 3.69, 3.70]

        # BMS states
        self.contactor_closed = True
        self.balancing_active = False
        self.fault_state = "NORMAL"

    def sense_parameters(self):
        """Read battery operating parameters."""
        print("Battery Sensing")
        print("----------------")
        print(f"Pack Voltage : {self.pack_voltage:.2f} V")
        print(f"Current      : {self.current:.2f} A")
        print(f"Temperature  : {self.temperature:.2f} °C")
        print(f"SOC          : {self.soc:.2f}%")
        print(f"SOH          : {self.soh:.2f}%")

    def check_protection(self):
        """Check basic battery protection limits."""

        if self.pack_voltage > 450:
            self.fault_state = "OVER_VOLTAGE"

        elif self.pack_voltage < 300:
            self.fault_state = "UNDER_VOLTAGE"

        elif abs(self.current) > 200:
            self.fault_state = "OVER_CURRENT"

        elif self.temperature > 60:
            self.fault_state = "OVER_TEMPERATURE"

        else:
            self.fault_state = "NORMAL"

    def check_cell_balance(self):
        """Check whether cell voltages are sufficiently balanced."""

        voltage_difference = max(self.cell_voltages) - min(self.cell_voltages)

        if voltage_difference > 0.05:
            self.balancing_active = True
        else:
            self.balancing_active = False

        print("\nCell Balancing")
        print("--------------")
        print(f"Cell voltage difference: {voltage_difference:.3f} V")

        if self.balancing_active:
            print("Balancing required")
        else:
            print("Cells are balanced")

    def control_contactor(self):
        """Control high-voltage battery contactor."""

        if self.fault_state == "NORMAL":
            self.contactor_closed = True
        else:
            self.contactor_closed = False

        print("\nContactor Status")
        print("----------------")
        if self.contactor_closed:
            print("Contactor: CLOSED")
        else:
            print("Contactor: OPEN")

    def display_status(self):
        """Display overall BMS status."""

        print("\nBMS Status")
        print("----------")
        print(f"Fault State: {self.fault_state}")
        print(f"Contactor: {'CLOSED' if self.contactor_closed else 'OPEN'}")
        print(
            f"Balancing: "
            f"{'ACTIVE' if self.balancing_active else 'INACTIVE'}"
        )


# Create BMS instance
if __name__ == "__main__":
    # Create BMS instance
    bms = BMS()

    print("AegisCAN Simplified BMS Model")
    print("==============================")

    # 1. Sense battery parameters
    bms.sense_parameters()

    # 2. Check protection limits
    bms.check_protection()

    # 3. Check cell balancing
    bms.check_cell_balance()

    # 4. Control contactor
    bms.control_contactor()

    # 5. Display final BMS status
    bms.display_status()