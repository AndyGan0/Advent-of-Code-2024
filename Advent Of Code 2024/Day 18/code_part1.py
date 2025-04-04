import numpy as np



# Load the grid
filename = "Day 18\input.txt"
with open(filename, 'r') as file:
    bytes_list = [line for line in file]
bytes_list = [x[:-1] if x.endswith("\n") else x for x in bytes_list ]
bytes_list = [x.split(',') for x in bytes_list]
bytes_list = [ { "X": int(x[0]), "Y": int(x[1]) } for x in bytes_list]

shape = (71,71)
grid = np.full(shape, ".")


count = 0
for b in bytes_list:

    grid[b["Y"], b["X"] ] = "#"

    count += 1
    if (count == 1024):
        break





def a_star(grid):


    def calculate_heuristic(state):
        result = grid.shape[0] - 1 - state['X'] + grid.shape[1] - 1 - state['Y'] + state['g_score']
        state['heuristic'] = result
        return result
    


    def insert_state_in_open_set(state):
        #   states are inserted sorted based on heuristic score
        i = 0
        while i < len(open_set) and open_set[i]['heuristic'] < state['heuristic']:
            i += 1
        open_set.insert(i, state)



    def produce_children(state: dict):

        children = []

        if ( state['Y'] - 1 >= 0 and grid[state['Y'] - 1, state['X']] != '#'):
            newChild = state.copy()
            newChild['Y'] -= 1            
            children.append(newChild)
        
        if ( state['Y'] + 1 < grid.shape[0] and grid[state['Y'] + 1, state['X']] != '#'):
            newChild = state.copy()
            newChild['Y'] += 1
            children.append(newChild)

        if ( state['X'] - 1 >= 0 and grid[state['Y'], state['X'] - 1] != '#'):
            newChild = state.copy()
            newChild['X'] -= 1
            children.append(newChild)

        if ( state['X'] + 1 < grid.shape[1] and grid[state['Y'], state['X'] + 1] != '#'):
            newChild = state.copy()
            newChild['X'] += 1
            children.append(newChild)

        for child in children:            
            child['g_score'] += 1
            child['came_from'] = state
            calculate_heuristic(child)

        return children



    open_set = [ {  'X': 0, 
                    'Y': 0,
                    'g_score': 0,
                    'came_from': None   } ]
    calculate_heuristic(open_set[0])
    

    #   closed set will have as keys the closed set. Specifically a tuple (x,y)
    closed_set = {}




    while open_set: #   if open set is not empty

        current_node = open_set[0]

        if (current_node['X'] == grid.shape[0]-1 and current_node['Y'] == grid.shape[0]-1):
            #   final position
            path = []
            while current_node is not None:
                path.append( [current_node['X'], current_node['Y']] )
                current_node = current_node['came_from']
            
            path.reverse()
            return path


        open_set.pop(0)
        closed_set[(current_node['X'], current_node['Y'])] = current_node


        children = produce_children(current_node)

        for child in children:
            #   if child is not in closed set then continue
            if (child['X'], child['Y']) not in closed_set:
                insert_state_in_open_set(child)

                

    
    return [] # no path




path = a_star(grid)



print(len(path) - 1)