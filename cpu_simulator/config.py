# config.py

# --- CLOCK PIN ---
# This pin will drive the clock signal for the CPU
PIN_CLOCK = 21  # Example: Using GPIO 21 (Physical Pin 40)

# --- INSTRUCTION BUS (10 Bits) ---
# 10 GPIO pins in order from Most Significant Bit (MSB) to Least Significant Bit (LSB)
# This represents the 10-bit instruction word layout
INSTRUCTION_BUS_PINS = [
    2,  # Bit 9 (MSB)
    3,  # Bit 8
    4,  # Bit 7
    17, # Bit 6
    27, # Bit 5
    22, # Bit 4
    10, # Bit 3
    9,  # Bit 2
    11, # Bit 1
    5   # Bit 0 (LSB) -> Example: GPIO 5
]