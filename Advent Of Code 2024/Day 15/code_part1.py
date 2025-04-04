import numpy as np



# Load the grid
filename = "Day 15\input.txt"
with open(filename, 'r') as file:
    grid = [line for line in file]


item_new_line = grid.index("\n")
movement = grid[item_new_line+1:]
movement = "".join(movement)
grid = [list(string[:-1]) for string in grid[:item_new_line]]
grid = np.array(grid)

result =  np.where(grid == "@")
robot_y, robot_x = int(result[0][0]), int(result[1][0]) if len(result[0]) > 0 else (None, None)



def tryMove(direction):
    global robot_x, robot_y
    end_path_pos_x, end_path_pos_y = robot_x, robot_y
    boxes_found = False

    if (direction == '<'):
        end_path_pos_x -= 1
        while (grid[end_path_pos_y, end_path_pos_x] == 'O'):
            boxes_found = True
            end_path_pos_x -= 1

        if (grid[end_path_pos_y, end_path_pos_x] == '#'):
            return False
        elif (grid[end_path_pos_y, end_path_pos_x] == '.'):
            if (boxes_found):
                grid[end_path_pos_y, end_path_pos_x] = 'O'
            grid[robot_y, robot_x] = '.'
            grid[robot_y, robot_x - 1] = '@'
            robot_x -= 1
            return True
    
    elif (direction == '^'):
        end_path_pos_y -= 1
        while (grid[end_path_pos_y, end_path_pos_x] == 'O'):
            boxes_found = True
            end_path_pos_y -= 1

        if (grid[end_path_pos_y, end_path_pos_x] == '#'):
            return False
        elif (grid[end_path_pos_y, end_path_pos_x] == '.'):
            if (boxes_found):
                grid[end_path_pos_y, end_path_pos_x] = 'O'
            grid[robot_y, robot_x] = '.'
            grid[robot_y - 1, robot_x] = '@'
            robot_y -= 1
            return True
    
    elif (direction == '>'):
        end_path_pos_x += 1
        while (grid[end_path_pos_y, end_path_pos_x] == 'O'):
            boxes_found = True
            end_path_pos_x += 1

        if (grid[end_path_pos_y, end_path_pos_x] == '#'):
            return False
        elif (grid[end_path_pos_y, end_path_pos_x] == '.'):
            if (boxes_found):
                grid[end_path_pos_y, end_path_pos_x] = 'O'
            grid[robot_y, robot_x] = '.'
            grid[robot_y, robot_x + 1] = '@'
            robot_x += 1
            return True
    
    elif (direction == 'v'):
        end_path_pos_y += 1
        while (grid[end_path_pos_y, end_path_pos_x] == 'O'):
            boxes_found = True
            end_path_pos_y += 1

        if (grid[end_path_pos_y, end_path_pos_x] == '#'):
            return False
        elif (grid[end_path_pos_y, end_path_pos_x] == '.'):
            if (boxes_found):
                grid[end_path_pos_y, end_path_pos_x] = 'O'
            grid[robot_y, robot_x] = '.'
            grid[robot_y + 1, robot_x] = '@'
            robot_y += 1
            return True



for direction in movement:
    tryMove(direction)
        


total_score = 0
for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        if (grid[y,x] == 'O'):
            total_score += y * 100 + x



print(total_score)