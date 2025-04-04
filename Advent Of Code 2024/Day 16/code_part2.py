import heapq
import numpy as np



# Load the grid
filename = "Day 16\input.txt"
with open(filename, 'r') as file:
    grid = [line.strip() for line in file if line.strip()]
grid = [list(string) for string in grid]
grid = np.array(grid)

result =  np.where(grid == "S")
location_y, location_x = int(result[0][0]), int(result[1][0]) if len(result[0]) > 0 else (None, None)
grid[location_y,location_x] = "."

result =  np.where(grid == "E")
finalY, finalX =  int(result[0][0]), int(result[1][0]) if len(result[0]) > 0 else (None, None)
grid[finalY,finalX] = "."



def BestFS(grid, start_x, start_y, end_x, end_y):

  
    def produce_children(state):
        children = []

        new_child_template = {
                'X': state['X'],
                'Y': state['Y'],
                "direction": state["direction"],
                "score": state["score"],
                "came_from": state
            }


        if state["direction"] == "right" or state["direction"] == "left":
            if state["direction"] == "right" and grid[state['Y'], state['X'] + 1] == ".":
                temp1 = new_child_template.copy()
                temp1['X'] += 1 
                temp1["score"] += 1 
                children.append(temp1)
            elif state["direction"] == "left" and grid[state['Y'], state['X'] - 1] == ".":
                temp1 = new_child_template.copy()
                temp1['X'] -= 1 
                temp1["score"] += 1 
                children.append(temp1)

            temp2 = new_child_template.copy()
            temp2["direction"] = "up"
            temp2["score"] += 1000
            children.append(temp2)

            temp3 = new_child_template.copy()
            temp3["direction"] = "down"
            temp3["score"] += 1000
            children.append(temp3)


        else: # direction is up or down
            if state["direction"] == "up" and grid[state['Y'] - 1, state['X']] == ".":
                temp1 = new_child_template.copy()
                temp1['Y'] -= 1 
                temp1["score"] += 1 
                children.append(temp1)
            elif state["direction"] == "down" and grid[state['Y'] + 1, state['X']] == ".":
                temp1 = new_child_template.copy()
                temp1['Y'] += 1 
                temp1["score"] += 1
                children.append(temp1)

            temp2 = new_child_template.copy()
            temp2["direction"] = "left"
            temp2["score"] += 1000
            children.append(temp2)

            temp3 = new_child_template.copy()
            temp3["direction"] = "right"
            temp3["score"] += 1000
            children.append(temp3)

        
        return children


    first_position = {  'X' : start_x,
                        'Y' : start_y,
                        'direction' : "right",
                        'score' : 0,
                        'came_from': None}
    
    open_set = []    
    heapq.heappush(open_set, (0, id(first_position), first_position ) )

    closed_set = {}


    best_score = None
    best_paths = []


    while open_set: #   if open set is not empty

        score, _, current_node = heapq.heappop(open_set)


        if best_score is not None and score > best_score:
            return best_paths, best_score
        

        if (current_node['X'], current_node['Y'], current_node['direction']) in closed_set:
            if current_node['score'] > closed_set[(current_node['X'], current_node['Y'], current_node['direction'])] ['score']:                
                continue        


        if (current_node['X'] == end_x and current_node['Y'] == end_y):
            #   final position
            if best_score is None:
                best_score = current_node["score"]

            path = []
            while current_node is not None:
                path.append( current_node )
                current_node = current_node['came_from']            
            path.reverse()
            best_paths.append(path)
            continue



        closed_set[(current_node['X'], current_node['Y'], current_node['direction'])] = current_node
        children = produce_children(current_node)


        for child in children:
            heapq.heappush(open_set, (child['score'], id(child), child) )

                

    
    return [], -1 # no path















best_path_list, score = BestFS(grid, location_x, location_y, finalX, finalY)

set_of_tiles = set()
for path in best_path_list:
    for tile in path:
        set_of_tiles.add( (tile['X'], tile['Y'] ) )


print(len(set_of_tiles))