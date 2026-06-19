import config
from clock import HardwareClock
from alu import simulate_alu
from registers import FourBitRegister
from contriol_unit import ControlUnit

if __name__ == "__main__":
    # 1. Initialize all pieces of our system
    cpu_clock = HardwareClock()
    control_unit = ControlUnit()
    register_a = FourBitRegister("Register A")
    register_b = FourBitRegister("Register B")
    
    # Preset starting data
    register_a.value = 5
    register_b.value = 3
    
    # 2. Fetch an instruction (e.g., ADD and store in Reg A)
    instruction = 0b00_00_00_1_0_00 
    
    # 3. Let the control unit decode the instruction into a control bus
    control_bus = control_unit.decode(instruction)
    control_unit.print_signal_status(control_bus)
    
    # 4. Feed the control lines directly into the ALU and Registers
    # Combinational math happens immediately:
    alu_out, flags = simulate_alu(
        opcode=control_bus["ALU_OPCODE"], 
        val_a=register_a.read(), 
        val_b=register_b.read()
    )
    
    # 5. Pulse the clock to trigger the sequential elements (the registers)
    clock_state = cpu_clock.toggle() # Goes HIGH
    
    # The registers look directly at the control lines coming out of the Control Unit
    register_a.tick(alu_out, load_enable=control_bus["LOAD_REG_A"], clock_signal=clock_state)
    register_b.tick(alu_out, load_enable=control_bus["LOAD_REG_B"], clock_signal=clock_state)
    
    cpu_clock.toggle() # Reset clock to LOW