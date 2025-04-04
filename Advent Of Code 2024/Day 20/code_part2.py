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



    seen_cheats = set()

    

    while (current_node['X'] != end_x or current_node['Y'] != end_y):

        #   ADD CHEATS
        for cheat_end_x in range(current_node['X'] - 20, current_node['X'] + 21):
            for cheat_end_y in range(current_node['Y'] - 20, current_node['Y'] + 21):                

                if (cheat_end_x < 0 or cheat_end_x >= grid.shape[1] or cheat_end_y < 0 or cheat_end_y >= grid.shape[0]):
                    continue

                if (abs(cheat_end_x - current_node['X']) + abs(cheat_end_y - current_node['Y']) > 20):
                    continue


                if (cheat_end_x == current_node['X'] and cheat_end_y == current_node['Y']):
                    continue

                
                key1 = (current_node['X'] , current_node['Y'] , cheat_end_x, cheat_end_y)
                key2 = (cheat_end_x, cheat_end_y, current_node['X'] , current_node['Y'] )
                if key1 in seen_cheats or key2 in seen_cheats:
                    continue

                if (grid[cheat_end_y, cheat_end_x] != '#'):                    
                    seen_cheats.add(key1)
                    seen_cheats.add(key2)

                    cheat_list.append({
                        'connected_pos_1': {
                            'X':current_node['X'],
                            'Y':current_node['Y']
                        },
                        'connected_pos_2': {
                            'X':cheat_end_x,
                            'Y':cheat_end_y
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






path = {(item['X'], item['Y']): index for index, item in enumerate(path)}


count = 0
for cheat in cheat_list:
    index_in_path_of_connected_pos_1 = path[(cheat['connected_pos_1']['X'], cheat['connected_pos_1']['Y'])]
    index_in_path_of_connected_pos_2 = path[(cheat['connected_pos_2']['X'], cheat['connected_pos_2']['Y'])]

    distance_needed = abs(cheat['connected_pos_2']['X'] - cheat['connected_pos_1']['X']) + abs(cheat['connected_pos_2']['Y'] - cheat['connected_pos_1']['Y'])

    distance_saved = abs(index_in_path_of_connected_pos_2 - index_in_path_of_connected_pos_1) - distance_needed
    cheat['saved'] = distance_saved

    if (distance_saved >= 100):
        count += 1






print(count)