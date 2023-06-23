# ProcessorSimulation
A single cycle MIPS datapath. The process parses through the machine code and simulates the instructions and outputs the register values for every instruction call.

# Input
The input file contains lines of 32 ASCII ones or zeros. The valid instructions are add, sub, addi, lw, sw, beq, and bne. There will only be 8 registers labelled from 0 to 7.

# Output
control.txt will show what the control line is for each clock cycle in the following order.
RegDst, ALUScr, MemtoReg, RegWrite, MemRead, MemWrite, branch, ALUOp1, ALUOp2, and the Zero bit from ALU

register.txt will show the updated values of the registers and the program will check of the PC goes out of bounds.
