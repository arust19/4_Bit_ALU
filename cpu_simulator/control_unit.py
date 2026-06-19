# control_unit.py

class ControlUnit:
    def __init__(self):
        # Initialize the internal state of the control unit
        self.current_instruction = 0

    def decode(self, instruction_word):
        """
        Decodes the 10-bit instruction word and generates control signals.
        For simplicity, let's assume the instruction format is as follows:
        
        Bits 9-8: Opcode (2 bits)
        Bits 7-6: Register A (2 bits) - can be expanded
        Bits 5-4: Register B (2 bits)
        Bit 3   : Load Enable for Register A (1 to load, 0 to ignore)
        Bit 2   : Load Enable for Register B

        This is just an example. You can design your own instruction format.
        """
        opcode = (instruction_word >> 8) & 0x3  # Extract bits 9-8
        reg_a = (instruction_word >> 6) & 0x3   # Extract bits 7-6
        reg_b = (instruction_word >> 4) & 0x3   # Extract bits 5-4
        load_a = (instruction_word >> 3) & 0x1   # Extract bit 3
        load_b = (instruction_word >> 2) & 0x1   # Extract bit 2

        print(f"Decoded Instruction: Opcode={opcode}, RegA={reg_a}, RegB={reg_b}, LoadA={load_a}, LoadB={load_b}")

        # Dictionary representing the state of the control bus lines
        control_signals = {
            "ALU_OPCODE": opcode,
            "REG_A_SELECT": reg_a,
            "REG_B_SELECT": reg_b,
            "LOAD_REG_A": load_a,
            "LOAD_REG_B": load_b
        }
        return control_signals
    
    def print_signal_status(self, signals):
        """Helper method to print what the control wires are doing."""
        print("\n--- Control Unit Signal Bus Status ---")
        print(f"  ALU Opcode Line : {signals['ALU_OPCODE']:02b}")
        print(f"  Load Register A : {'ENABLED (1)' if signals['LOAD_REG_A'] else 'DISABLED (0)'}")
        print(f"  Load Register B : {'ENABLED (1)' if signals['LOAD_REG_B'] else 'DISABLED (0)'}")
        print("---------------------------------------")


# --- LOCAL TEST BENCH ---
if __name__ == "__main__":
    print("--- Testing Control Unit Isolation ---")
    cu = ControlUnit()
    
    # Test case: Opcode 00 (ADD), Load Reg A enabled, Load Reg B disabled
    test_instruction = 0b00_00_00_1_0_00 
    signals = cu.decode(test_instruction)
    cu.print_signal_status(signals)