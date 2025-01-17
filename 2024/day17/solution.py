from tqdm import tqdm
import sys

if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = "input"

# Input processing
with open(path) as f:
    data = f.read()
    registers, program = data.split("\n\n")
    registers = registers.split("\n")
    registerA = int(registers[0].split(":")[1])
    registerB = int(registers[1].split(":")[1])
    registerC = int(registers[2].split(":")[1])
    program = program.split(":")[1].lstrip().split(",")
    program = [int(x) for x in program]


# solution - part2
outputs = []
currentRegisterA = bin(0)
currentRegisterB = registerB
currentRegisterC = registerC

for n in range(len(program)):
    subprogram = program[-(n+1):]

    print("n=", n)
    # Add three bits to the right
    currentRegisterA = bin(int(currentRegisterA, 2) * 8)

    try_index = 0
    while True:
        i = 0
        registerA = int(currentRegisterA, 2)
        registerB = currentRegisterB
        registerC = currentRegisterC

        outputs = []

        while i < len(program):
            opcod = program[i]
            operand = program[i+1]

            # get combo operand
            if 0 <= operand <= 3:
                combo_operand = operand
            elif operand == 4:
                combo_operand = registerA
            elif operand == 5:
                combo_operand = registerB
            elif operand == 6:
                combo_operand = registerC
            else:
                combo_operand = None
            i +=2 
            match opcod:
                case 0:
                    # The adv instruction (opcode 0) performs division. 
                    # The numerator is the value in the A register. 
                    # The denominator is found by raising 2 to the power of the instruction's combo operand. 
                    # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) 
                    # The result of the division operation is truncated to an integer and then written to the A register.
                    result = registerA / (2 ** combo_operand)
                    registerA = int(result)
                case 1:
                    # The bxl instruction (opcode 1) calculates the 
                    # bitwise XOR of register B and the instruction's literal operand
                    # then stores the result in register B.
                    result = registerB ^ operand
                    registerB = result
                case 2:
                    # The bst instruction (opcode 2) calculates the value 
                    # of its combo operand modulo 8 (thereby keeping only its lowest 3 bits),
                    #  then writes that value to the B register.
                    result = combo_operand % 8
                    registerB = result
                case 3:
                    # The jnz instruction (opcode 3) does nothing if the A register is 0. 
                    # However, if the A register is not zero, 
                    # it jumps by setting the instruction pointer to the value of its literal operand; 
                    # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
                    if registerA != 0:
                        i = operand
                case 4:
                    # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C
                    # then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
                    result = registerB ^ registerC
                    registerB = result
                case 5:
                    # The out instruction (opcode 5) calculates the value of its combo operand modulo 8
                    # then outputs that value. (If a program outputs multiple values, they are separated by commas.)
                    result = combo_operand % 8
                    outputs.append(result)
                case 6:
                    # The bdv instruction (opcode 6) works exactly like the adv instruction 
                    # except that the result is stored in the B register. (The numerator is still read from the A register.)
                    result = registerA / (2 ** combo_operand)
                    registerB = int(result)
                case 7:
                    # The cdv instruction (opcode 7) works exactly like the adv instruction 
                    # except that the result is stored in the C register. (The numerator is still read from the A register.)
                    result = registerA / (2 ** combo_operand)
                    registerC = int(result)


        if subprogram == outputs:
            print(currentRegisterA, subprogram, try_index)
            break      
        else:  
            # print(int(currentRegisterA,2), currentRegisterA, subprogram)
            # print(int(currentRegisterA,2), currentRegisterA, outputs, try_index)
            try_index += 1
            currentRegisterA = bin(int(currentRegisterA, 2) + 1)
