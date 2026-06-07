#registers.py
class FourBitRegister:
    def __init__(self, name="Register"):
        self.name = name
        self.value = 0  # Initialize register value to 0

    def tick(self, input_bus, load_enable, clock_signal):
        """Mimics the behavior of a 4-bit register on the rising edge of the clock signal.
            Only updates the register value if load_enable is high (1) and clock_signal is rising (1).
        """
        # In hardware, registers latch on the rising edge of the clock
        if load_enable and clock_signal:
            self.value = input_bus & 0xF  # Ensure only the lower 4 bits are stored
            print(f"{self.name} loaded with value: {self.value:04b} ({self.value})")

        else: 
            #If load_enable is not high, the register retains its value
            pass

    def read(self):
        """Returns the current value of the register."""
        return self.value
    
# Quick local test block to make sure our register works in isolation
if __name__ == "__main__":
    print("--- Testing Hardware Register Simulation ---")
    reg_a = FourBitRegister("Register A")
    
    # 1. Put a value on the wire, but keep Load Enable turned OFF
    print(f"Initial state: {reg_a.read()}")
    reg_a.tick(input_bus=12, load_enable=0, clock_signal=1)
    print(f"State after clock pulse with Load=0: {reg_a.read()} (Should still be 0)")
    
    # 2. Turn Load Enable ON and pulse the clock
    reg_a.tick(input_bus=12, load_enable=1, clock_signal=1)
    print(f"State after clock pulse with Load=1: {reg_a.read()} (Should now be 12!)")