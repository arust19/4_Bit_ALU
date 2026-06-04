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
    
    return result_4bit, carry_out
