


# Load the grid
filename = "Day 17\input.txt"
with open(filename, 'r') as file:
    grid = [line for line in file]


initial_register_A = int(grid[0][:-1].split(":")[1])
initial_register_B = int(grid[1][:-1].split(":")[1])
initial_register_C = int(grid[2][:-1].split(":")[1])



instructions = grid[-1].split()[1].split(',')
temp = []
for i in range(len(instructions)):
    if (i%2 == 0):
        temp.append({
            "opcode": int(instructions[i]),
            "operand": int(instructions[i+1])
        })
instructions = temp





target_output = grid[-1].split()[1].split(',')
target_output = [int(x) for x in target_output]





#   code of part 1 does the same as this code for this specific input
def calculateOutput():
    output = []
    register_A = initial_register_A
    register_B = initial_register_B
    register_C = initial_register_C    

    while (register_A != 0):

        register_B = (register_A % 8) ^ 3
        register_C = int(register_A / (2 ** register_B))
        register_B = ((register_B ^ register_C) ^ 5) % 8

        output.append(register_B)
        
        register_A = int(register_A / 8)

    return output



#   the whole loop is dependant on register A
#   so we reverse the logic of the program to find the input




target_output.reverse()
valid = [0]

register_A = 0
register_B = initial_register_B
register_C = initial_register_C


while (len(target_output) != 0 ):

    new_valid = []


    for valid_number in valid:
        for remainder in range(8):

            register_A = valid_number * 8 + remainder

            register_B = (register_A % 8) ^ 3
            register_C = int(register_A / (2 ** register_B))
            register_B = ((register_B ^ register_C) ^ 5) % 8

            if (target_output[0] == register_B):
                new_valid.append(register_A)
    
    valid = new_valid
    target_output.pop(0)



print(min(valid))
