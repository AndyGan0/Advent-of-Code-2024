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






saved_operations = {}

while i < len(file):
    input, output = file[i].split('->')
    input = input.split()
    gate = input[1]    
    input = [input[0], input[2]]
    output = output.strip()   

    saved_operations[output] = {
        'input': input,
        'gate': gate
    }

    i += 1




already_seen_wires = {}
main_z_operations = {}

def add_operations_to_main_z_operations(z_wire, operation_to_add, add_as_root=True):
    if (add_as_root):
        main_z_operations[z_wire] = saved_operations[operation_to_add].copy()
        main_z_operations[z_wire]['needed_wires'] = {}
    else:
        main_z_operations[z_wire]['needed_wires'][operation_to_add] = saved_operations[operation_to_add].copy()
    already_seen_wires[operation_to_add] = None

    
    for input in saved_operations[operation_to_add]['input']:
        if input[0] != 'x' and input[0] != 'y':
            if input not in already_seen_wires:
                add_operations_to_main_z_operations(z_wire, input, add_as_root=False)




i = 0
while True:
    if i <= 9:
        z_wire = 'z0' + str(i)
    else:
        z_wire = 'z' + str(i)

    if z_wire not in saved_operations:
        break
    
    add_operations_to_main_z_operations(z_wire, z_wire)
    i += 1
    
    


#   C0 = X0 AND Y0
#   Z1 = C0 XOR X1 XOR X2


#   Ck = (Xk AND Yk) OR ((Xk XOR Yk) AND Ck-1)
#   Zk = Xk XOR Yk XOR Ck-1




print('\n')
print('\n')
print('problematic wires:')
for z_wire in main_z_operations:
    gate = main_z_operations[z_wire]['gate']
    if gate != 'XOR' :
        print(z_wire)


#   based on the output, these wires are problematic.
#   z06
#   z31
#   z37
#   z45
    



#   finding the error visually from the txt file





for z_wire in main_z_operations:
    print(z_wire, "     ", main_z_operations[z_wire]['gate'] ,"     ", main_z_operations[z_wire]['input'])
    for input_needed in main_z_operations[z_wire]['needed_wires']:
        print("          ",input_needed, "       ", main_z_operations[z_wire]['needed_wires'][input_needed]['input'],"   ",  main_z_operations[z_wire]['needed_wires'][input_needed]['gate'] )

    print('\n')




#   z06 swap with hwk
#   z31 swap with hpc
#   z37 swap with cgr

#   z45 IS NOT wrong because its last thats why it appears with OR

#   z25 has no XOR while z26 has 2 XORS. thus one pair inside them must be swapped
#   A XOR from z26 must be swapped with an AND of z25

#   qmd swap with tnt



#   pairs are:
#   z06 with hwk    -   z31 with  hpc   -   z37 with cgr    -   qmd with tnt
#   in alphabetical order:

#   cgr,hpc,hwk,qmd,tnt,z06,z31,z37

