import config
from clock import HardwareClock
from alu import simulate_alu

def simulate_pi_gpio_outputs(instruction_word):
    """
    Simulates sending a 10-bit instruction out over the Raspberry Pi GPIO pins.
    """
    # Enforce a 10-bit limit (values 0 to 1023)
    sanitized_instruction = instruction_word & 0x3FF
    
    # Convert to a 10-character wide binary string (e.g., 25 -> "0000011001")
    binary_string = f"{sanitized_instruction:010b}"
    
    print("\n--- Physical GPIO Signal Map ---")
    # Loop through each bit and see which pin it maps to
    for index, bit_char in enumerate(binary_string):
        pin_number = config.INSTRUCTION_BUS_PINS[index]
        bit_value = int(bit_char)
        print(f"  [GPIO {pin_number:02d}] driving line Bit {9 - index} -> {'HIGH (1)' if bit_value else 'LOW (0)'}")


if __name__ == "__main__":
    # Create our simulation components
    cpu_clock = HardwareClock()
    
    # Example: An instruction opcode you want to send out (e.g., 0b1011001101 = 717)
    test_instruction = 717 
    
    # 1. Visualize how the 10-bit bus splits across your physical pins
    simulate_pi_gpio_outputs(test_instruction)
    
    # 2. Simulate a clock cycle pulsing
    old_clock_state = cpu_clock.state
    new_clock_state = cpu_clock.toggle()
    
    if cpu_clock.is_rising_edge(old_clock_state):
        print(f"\n[Clock Edge] Rising edge detected ({old_clock_state} -> {new_clock_state}). Hardware registers latching data!")