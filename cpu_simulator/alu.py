#alu.py

# The ALU file has no dependencies, so I am starting the simulation here.
# The ALU is the Arithmetic Logic Unit, which performs arithmetic and logical operations on the data.

"""Simulates a 4-bit ALU.

    Inputs:
    - val_a: 4-bit integer (0-15) representing register A
    - val_b: 4-bit integer (0-15) representing register B
    - opcode: 2-bit integer (0-3) representing the operation to perform
        - 00: ADD
        - 01: SUB
        - 10: AND
        - 11: OR

    Outputs:  
    - result: 4-bit integer (0-15) representing the result of the operation
    - carry_out: 1-bit integer (0 or 1) representing the carry out from the operation 'C'
    - zero: 1-bit integer (0 or 1) representing whether the result is zero            'Z'
    - negative: 1-bit integer (0 or 1) representing whether the result is negative    'N'

"""
def simulate_alu(opcode, val_a, val_b):

    # Make sure inputs are within the valid range
    val_a = val_a & 0xF  # Ensure val_a is 4 bits
    val_b = val_b & 0xF  # Ensure val_b is 4 bits
    opcode = opcode & 0x3  # Ensure opcode is 2 bits

    # Initialize tracking variable
    carry_out = 0
    result = 0

    # Logic selection (mimics a multiplexer)
    if opcode == 0:
        result = val_a + val_b

        if(result > 0xF):  # Check for carry out
            carry_out = 1

    elif opcode == 1:
        result = val_a - val_b
        if(result < 0):  # Check for borrow (negative result)
            carry_out = 1

    elif opcode == 2:
        result = val_a & val_b
        carry_out = 0  # AND operation does not produce a carry out

    elif opcode == 3:
        result = val_a | val_b
        carry_out = 0  # OR operation does not produce a carry out

    # Mask the final result to ensure its 4 bits
    result_4bit = result & 0xF

    # Set flags
    flags = {
        'C': carry_out,           # Carry flag
        'Z': 1 if result_4bit == 0 else 0,  # Zero flag
        'N': 1 if (result_4bit & 0x8) != 0 else 0  # Negative flag (check the most significant bit)
    }
    
    return result_4bit, flags



# --- LOCAL TEST BENCH ---
# This only runs if you execute alu.py directly. It won't run when main.py imports it.
if __name__ == "__main__":
    print("=========================================")
    print("       TESTING 4-BIT ALU COMPONENT       ")
    print("=========================================\n")

    # Test Case 1: Simple Addition (5 + 3 = 8)
    out, f = simulate_alu(0, 5, 3)
    print(f"Test 5 + 3 [ADD]:")
    print(f"  Output: {out:04b} ({out}) | Flags: Z={f['Z']}, C={f['C']}, N={f['N']}")
    print("  (Expected: Output=1000, N=1 because the MSB became 1)\n")

    # Test Case 2: Addition with Overflow (12 + 6 = 18 -> 18 - 16 = 2)
    out, f = simulate_alu(0, 12, 6)
    print(f"Test 12 + 6 [ADD with Overflow]:")
    print(f"  Output: {out:04b} ({out}) | Flags: Z={f['Z']}, C={f['C']}, N={f['N']}")
    print("  (Expected: Output=0010, C=1 due to math wrapping around)\n")

    # Test Case 3: Subtraction resulting in Zero (7 - 7 = 0)
    out, f = simulate_alu(1, 7, 7)
    print(f"Test 7 - 7 [SUB]:")
    print(f"  Output: {out:04b} ({out}) | Flags: Z={f['Z']}, C={f['C']}, N={f['N']}")
    print("  (Expected: Output=0000, Z=1)\n")

    # Test Case 4: Bitwise AND (12 AND 5 -> 1100 & 0101 = 0100)
    out, f = simulate_alu(2, 12, 5)
    print(f"Test 12 AND 5 [LOGIC AND]:")
    print(f"  Output: {out:04b} ({out}) | Flags: Z={f['Z']}, C={f['C']}, N={f['N']}")
    print("  (Expected: Output=0100, All flags 0)\n")
