import numpy as np



# Load the grid
filename = "Day 20\input.txt"
with open(filename, 'r') as file:
    grid = [line for line in file]
grid = [list(string) for string in grid]
grid = [x[:-1] if x[-1] == '\n' else x for x in grid ]
grid = np.array(grid)


start_y, start_x = np.where(grid == 'S')
start_y, start_x = int(start_y[0]), int(start_x[0])
end_y, end_x = np.where(grid == 'E')
end_y, end_x = int(end_y[0]), int(end_x[0])




def find_path_and_cheats(grid, start_x, start_y, end_x, end_y):

    previous_node = {
        'X': start_x,
        'Y':start_y
    } 

    current_node = {
        'X': start_x,
        'Y':start_y
    } 

    normal_path = []
    cheat_list = []

    

    while (current_node['X'] != end_x or current_node['Y'] != end_y):

        #   ADD CHEATS
        if (current_node['Y'] - 2 >= 0 and grid[current_node['Y'] - 1, current_node['X']] == '#' and grid[current_node['Y'] - 2, current_node['X']] != '#'):
            cheat_list.append({
                'connected_pos_1': {
                    'X':current_node['X'],
                    'Y':current_node['Y']
                },
                'connected_pos_2': {
                    'X':current_node['X'],
                    'Y':current_node['Y'] - 2
                },
            })

        if (current_node['Y'] + 2 < grid.shape[0] and grid[current_node['Y'] + 1, current_node['X']] == '#' and grid[current_node['Y'] + 2, current_node['X']] != '#'):
            cheat_list.append({
                'connected_pos_1': {
                    'X':current_node['X'],
                    'Y':current_node['Y']
                },
                'connected_pos_2': {
                    'X':current_node['X'],
                    'Y':current_node['Y'] + 2
                },
            })

        
        if (current_node['X'] - 2 >= 0 and grid[current_node['Y'], current_node['X'] - 1] == '#'and grid[current_node['Y'], current_node['X'] - 2] != '#'):
            cheat_list.append({
                'connected_pos_1': {
                    'X':current_node['X'],
                    'Y':current_node['Y']
                },
                'connected_pos_2': {
                    'X':current_node['X'] - 2,
                    'Y':current_node['Y']
                },
            })

        if (current_node['X'] + 2 < grid.shape[1] and grid[current_node['Y'], current_node['X'] + 1] == '#' and grid[current_node['Y'], current_node['X'] + 2] != '#'):
            cheat_list.append({
                'connected_pos_1': {
                    'X':current_node['X'],
                    'Y':current_node['Y']
                },
                'connected_pos_2': {
                    'X':current_node['X'] + 2,
                    'Y':current_node['Y']
                },
            })


        
        

        if (current_node['Y'] - 1 != previous_node['Y']  and  current_node['Y'] - 1 >= 0 and grid[current_node['Y'] - 1, current_node['X']] != '#'):            
            previous_node['X'] = current_node['X']
            previous_node['Y'] = current_node['Y']
            current_node['Y'] -= 1 
        elif (current_node['Y'] + 1 != previous_node['Y']  and  current_node['Y'] + 1 < grid.shape[0] and grid[current_node['Y'] + 1, current_node['X']] != '#'):            
            previous_node['X'] = current_node['X']
            previous_node['Y'] = current_node['Y']
            current_node['Y'] += 1 
        elif (current_node['X'] - 1 != previous_node['X']  and  current_node['X'] - 1 >= 0 and grid[current_node['Y'], current_node['X'] - 1] != '#'):            
            previous_node['X'] = current_node['X']
            previous_node['Y'] = current_node['Y']
            current_node['X'] -= 1 
        elif (current_node['X'] + 1 != previous_node['X']  and  current_node['X'] + 1 < grid.shape[1] and grid[current_node['Y'], current_node['X'] + 1] != '#'):            
            previous_node['X'] = current_node['X']
            previous_node['Y'] = current_node['Y']
            current_node['X'] += 1 

        

        

        
        normal_path.append(previous_node.copy())
                
    normal_path.append(current_node.copy())
    
    return normal_path, cheat_list




path, cheat_list = find_path_and_cheats(grid, start_x, start_y, end_x, end_y)



seen = set()
unique_cheats = {}
for cheat in cheat_list:    
    if cheat['connected_pos_1']['X'] == cheat['connected_pos_2']['X']:
        in_between_box_x = cheat['connected_pos_1']['X'] 
    else:
        in_between_box_x = int (( cheat['connected_pos_1']['X'] + cheat['connected_pos_2']['X'] ) / 2)

    if cheat['connected_pos_1']['Y'] == cheat['connected_pos_2']['Y']:
        in_between_box_y = cheat['connected_pos_1']['Y'] 
    else:
        in_between_box_y = int(( cheat['connected_pos_1']['Y'] + cheat['connected_pos_2']['Y'] ) / 2)

    cheat['in_between_box'] = {
        'X':in_between_box_x,
        'Y':in_between_box_y
    }
    

    key = (in_between_box_x, in_between_box_y)
    if key not in seen:
        unique_cheats[key] = cheat
        seen.add(key)

cheat_list = list(unique_cheats.values())




values = {}


count = 0
for cheat in cheat_list:
    index_in_path_of_connected_pos_1 = path.index(cheat['connected_pos_1'])
    index_in_path_of_connected_pos_2 = path.index(cheat['connected_pos_2'])

    distance_saved = abs(index_in_path_of_connected_pos_2 - index_in_path_of_connected_pos_1) - 2
    cheat['saved'] = distance_saved


    if (distance_saved not in values):
        values[distance_saved] = 1
    else:
        values[distance_saved] += 1

    if (distance_saved >= 100):
        count += 1






print(count)