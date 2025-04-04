import math


connections_dict = {}

# Load the grid
filename = "Day 23\input.txt"
with open(filename, 'r') as file:
    file = [line for line in file]
file = [x[:-1] if x[-1] == '\n' else x for x in file ]
file = [x.split('-') for x in file ]

for conn in file:
    if (conn[0] not in connections_dict):
        connections_dict[conn[0]] = {}
    if (conn[1] not in connections_dict):
        connections_dict[conn[1]] = {}
    

    connections_dict[conn[0]][conn[1]] = None
    connections_dict[conn[1]][conn[0]] = None
    


inter_connected_conns = {}

for computer_1 in connections_dict:
    for computer_2 in connections_dict[computer_1]:
        for computer_3 in connections_dict[computer_1]:
            if (computer_2 == computer_3):
                continue

            if (computer_3 not in connections_dict[computer_2]):
                continue

            if ( (computer_1, computer_2, computer_3) in inter_connected_conns or
                 (computer_1, computer_3, computer_2) in inter_connected_conns or
                 (computer_2, computer_1, computer_3) in inter_connected_conns or
                 (computer_2, computer_3, computer_1) in inter_connected_conns or
                 (computer_3, computer_1, computer_2) in inter_connected_conns or
                 (computer_3, computer_2, computer_1) in inter_connected_conns):
                continue

            inter_connected_conns[(computer_1, computer_2, computer_3)] = None
    
    for computer in connections_dict:
        if (computer_1 in connections_dict[computer]):
            connections_dict[computer].pop(computer_1)


inter_connected_conns = list(inter_connected_conns.keys())
inter_connected_conns = [ conn for conn in inter_connected_conns if conn[0][0] == 't' or conn[1][0] == 't' or conn[2][0] == 't']



print(len(inter_connected_conns))