import math



# Load the grid
filename = "Day 24\input.txt"
with open(filename, 'r') as file:
    file = [line for line in file]
    file = [x[:-1] if x[-1] == '\n' else x for x in file ]

wires = {}
i = 0
while i < len(file) and file[i] != '':
    wire, state = file[i].split()
    wires[wire[:-1]] = state
    i += 1
i += 1



def perform_operation(input, gate, output):
    global wires
    
    
    input = [wires[input[0]], wires[input[1]] ]

    

    if gate == 'AND':
        if input[0] == '1' and input[1] == '1':            
            result = '1'
        else:
            result = '0'
    if gate == 'OR':
        if input[0] == '1' or input[1] == '1':            
            result = '1'
        else:
            result = '0'
    if gate == 'XOR':
        if input[0] != input[1]:            
            result = '1'
        else:
            result = '0'
    
    wires[output] = result




saved_operations = {}

while i < len(file):
    input, output = file[i].split('->')
    input = input.split()
    gate = input[1]    
    input = [input[0], input[2]]
    output = output.strip()   

    if input[0] not in wires or input[1] not in wires:
        saved_operations[output] = {
            'input': input,
            'gate': gate
        }
        i += 1
        continue

    perform_operation(input, gate, output)
    i += 1




def perform_operation_from_memory(output_wire):
    global wires

    if saved_operations[output_wire]['input'][0] not in wires:
        perform_operation_from_memory(saved_operations[output_wire]['input'][0])

    if saved_operations[output_wire]['input'][1] not in wires:
        perform_operation_from_memory(saved_operations[output_wire]['input'][1])
    
    perform_operation(saved_operations[output_wire]['input'], saved_operations[output_wire]['gate'], output_wire)

    saved_operations.pop(output_wire)




while True:
    if len(saved_operations) == 0:
        break

    first_output = list(saved_operations.keys())[0]
    perform_operation_from_memory(first_output)






z_number = ''
i = 0
while True:
    if i <= 9:
        z_wire = 'z0' + str(i)
    else:
        z_wire = 'z' + str(i)

    if z_wire not in wires:
        break

    z_number = wires[z_wire] + z_number

    i += 1
    
    




print(int(z_number, 2))