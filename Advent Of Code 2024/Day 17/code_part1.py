


# Load the grid
filename = "Day 17\input.txt"
with open(filename, 'r') as file:
    grid = [line for line in file]


register_A = int(grid[0][:-1].split(":")[1])
register_B = int(grid[1][:-1].split(":")[1])
register_C = int(grid[2][:-1].split(":")[1])



instructions = grid[-1].split()[1].split(',')
temp = []
for i in range(len(instructions)):
    if (i%2 == 0):
        temp.append({
            "opcode": int(instructions[i]),
            "operand": int(instructions[i+1])
        })
instructions = temp



def get_combo_operand_value(operand):
    if (operand == 4):
        return register_A
    elif (operand == 5):
        return register_B
    elif (operand == 6):
        return register_C
    elif (operand == 7):
        return register_C
    
    return operand



def perform_instruction(opcode, operand):
    global register_A, register_B, register_C, jump

    if (opcode == 0):
        numerator = register_A
        operand = get_combo_operand_value(operand)        
        dinominator = 2 ** operand
        result = int(numerator/dinominator)
        register_A = result

    elif (opcode == 1):
        result = register_B ^ operand
        register_B = result

    elif (opcode == 2):
        operand = get_combo_operand_value(operand)
        result = operand % 8
        register_B = result

    elif (opcode == 3):
        if (register_A == 0):
            return
        jump = operand

    elif (opcode == 4):        
        result = register_B ^ register_C
        register_B = result

    elif (opcode == 5):        
        operand = get_combo_operand_value(operand)
        result = operand % 8
        output.append(result)

    elif (opcode == 6):
        operand = get_combo_operand_value(operand)
        numerator = register_A
        dinominator = 2 ** operand
        result = int(numerator/dinominator)
        register_B = result

    elif (opcode == 7):
        operand = get_combo_operand_value(operand)
        numerator = register_A
        dinominator = 2 ** operand
        result = int(numerator/dinominator)
        register_C = result





jump = -1
output = []



instruct = 0
while (instruct < len(instructions)):
    perform_instruction(instructions[instruct]["opcode"], instructions[instruct]["operand"])

    if (jump != -1):
        instruct = jump
        jump = -1
        continue

    instruct += 1

print(",".join(map(str, output)))