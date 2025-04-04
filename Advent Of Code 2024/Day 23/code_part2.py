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
    


all_conn_parties = {}

for computer_1 in connections_dict:

    all_conn_parties[computer_1] = {}

    nodes_seen = {}
    nodes_seen[computer_1] = None

    for computer_2 in connections_dict[computer_1]:

        if computer_2 in nodes_seen:
            continue

        current_party = {}
        current_party[computer_1] = None
        current_party[computer_2] = None
        nodes_seen[computer_2] = None

        for computer_3 in connections_dict[computer_1]:
            if (computer_3 in nodes_seen):
                continue

            computer_3_is_connected_to_all_party = True
            for pc_in_party in current_party:
                if (pc_in_party not in connections_dict[computer_3]):
                    computer_3_is_connected_to_all_party = False
                    break
            
            if not computer_3_is_connected_to_all_party:
                continue

            current_party[computer_3] = None
            nodes_seen[computer_3] = None

        all_conn_parties[computer_1][computer_2] = current_party
    
    for temp_computer_1 in current_party:
        for temp_computer_2 in current_party:
            if temp_computer_2 in connections_dict[temp_computer_1] :
                connections_dict[temp_computer_1].pop(temp_computer_2)



max_party = []

for node_1 in all_conn_parties:
    nodes_connected_to_1 = list(all_conn_parties[node_1].keys())
    if len(nodes_connected_to_1) == 0:
        continue

    max_key_party = nodes_connected_to_1[0]
    for i in range(1, len(nodes_connected_to_1)):
        node_2 = nodes_connected_to_1[i]
        if len(all_conn_parties[node_1][node_2]) > len(all_conn_parties[node_1][max_key_party]):
            max_key_party = node_2

    if len(all_conn_parties[node_1][max_key_party]) > len(max_party):
        max_party = list(all_conn_parties[node_1][max_key_party].keys())

    
max_party = sorted(max_party)
password = ",".join(max_party)


print(password)