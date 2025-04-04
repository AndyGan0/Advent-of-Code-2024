import numpy as np



# Load the grid
filename = "Day 15\input.txt"
with open(filename, 'r') as file:
    grid = [line for line in file]


item_new_line = grid.index("\n")
movement = grid[item_new_line+1:]
movement = "".join(movement)
grid = [list(string[:-1]) for string in grid[:item_new_line]]

newGrid =[]
i = 0
for list in grid:    
    newGrid.append([])
    for item in list:
        if (item == '#'):
            newGrid[i].append("#")
            newGrid[i].append("#")
        elif (item == 'O'):
            newGrid[i].append("[")
            newGrid[i].append("]")
        elif (item == '@'):
            newGrid[i].append("@")
            newGrid[i].append(".")
        elif (item == '.'):
            newGrid[i].append(".")
            newGrid[i].append(".")
    
    i += 1



grid = np.array(newGrid)

result =  np.where(grid == "@")
robot_y, robot_x = int(result[0][0]), int(result[1][0]) if len(result[0]) > 0 else (None, None)



def tryPushBoxHorizontally(box_x, box_y, direction):
    if (direction == '<'):
        if box_x == 0:
            return False
        
        temp_x = box_x - 1
        while grid[box_y, temp_x] == ']' or grid[box_y, temp_x] == '[':
            temp_x -= 1

        if grid[box_y, temp_x] != '.':            
            return False
        
        while temp_x != box_x:
            grid[box_y, temp_x] = grid[box_y, temp_x + 1]
            temp_x += 1
            
        grid[box_y, temp_x] = '.'
        return True   


    elif (direction == '>'):
        if box_x == grid.shape[1] - 1:
            return False
        
        temp_x = box_x + 1
        while grid[box_y, temp_x] == ']' or grid[box_y, temp_x] == '[':
            temp_x += 1

        if grid[box_y, temp_x] != '.':            
            return False
        
        while temp_x != box_x:
            grid[box_y, temp_x] = grid[box_y, temp_x - 1]
            temp_x -= 1

        grid[box_y, temp_x] = '.'
        return True




def checkIfCanPushUpOrDown(box_x, box_y, direction):
    if grid[box_y, box_x] == '.':
        return True
    elif grid[box_y, box_x] == '#':
        return False
    

    if (direction == '^'):
        if not checkIfCanPushUpOrDown(box_x, box_y - 1, direction):
                return False
        
        if (grid[box_y, box_x] == '['):            
            if not checkIfCanPushUpOrDown(box_x + 1, box_y - 1, direction):
                return False        
        elif (grid[box_y, box_x] == ']'):            
            if not checkIfCanPushUpOrDown(box_x - 1, box_y - 1, direction):
                return False


    elif (direction == 'v'):
        if not checkIfCanPushUpOrDown(box_x, box_y + 1, direction):
                return False
        
        if (grid[box_y, box_x] == '['):            
            if not checkIfCanPushUpOrDown(box_x + 1, box_y + 1, direction):
                return False        
        elif (grid[box_y, box_x] == ']'):            
            if not checkIfCanPushUpOrDown(box_x - 1, box_y + 1, direction):
                return False


    return True




def pushBoxUpOrDown(box_x, box_y, direction):
    if grid[box_y, box_x] == '.':
        return

    if (direction == '^'):
        if (grid[box_y, box_x] == '['):
            pushBoxUpOrDown(box_x, box_y - 1, direction)
            pushBoxUpOrDown(box_x + 1, box_y - 1, direction)
            grid[box_y - 1, box_x] = '['
            grid[box_y - 1, box_x + 1] = ']'
            grid[box_y, box_x] = '.'
            grid[box_y, box_x + 1] = '.'
        elif (grid[box_y, box_x] == ']'):
            pushBoxUpOrDown(box_x - 1, box_y - 1, direction)
            pushBoxUpOrDown(box_x, box_y - 1, direction)
            grid[box_y - 1, box_x - 1] = '['
            grid[box_y - 1, box_x] = ']'
            grid[box_y, box_x - 1] = '.'
            grid[box_y, box_x] = '.'


    elif (direction == 'v'):        
        if (grid[box_y, box_x] == '['):
            pushBoxUpOrDown(box_x, box_y + 1, direction)
            pushBoxUpOrDown(box_x + 1, box_y + 1, direction)
            grid[box_y + 1, box_x] = '['
            grid[box_y + 1, box_x + 1] = ']'
            grid[box_y, box_x] = '.'
            grid[box_y, box_x + 1] = '.'
        elif (grid[box_y, box_x] == ']'):
            pushBoxUpOrDown(box_x - 1, box_y + 1, direction)
            pushBoxUpOrDown(box_x, box_y + 1, direction)
            grid[box_y + 1, box_x - 1] = '['
            grid[box_y + 1, box_x] = ']'
            grid[box_y, box_x - 1] = '.'
            grid[box_y, box_x] = '.'











def tryMove(direction):
    global robot_x, robot_y

    if (direction == '<'):
        if grid[robot_y, robot_x-1] == ']':
            tryPushBoxHorizontally(robot_x-1, robot_y, direction)

        if grid[robot_y, robot_x-1] == '.':
            grid[robot_y, robot_x-1] = '@'
            grid[robot_y, robot_x] = '.'
            robot_x -= 1


    elif (direction == '>'):
        if grid[robot_y, robot_x+1] == '[':
            tryPushBoxHorizontally(robot_x+1, robot_y, direction)

        if grid[robot_y, robot_x+1] == '.':
            grid[robot_y, robot_x+1] = '@'
            grid[robot_y, robot_x] = '.'
            robot_x += 1

    elif (direction == '^'):
        result = checkIfCanPushUpOrDown(robot_x, robot_y-1, direction)

        if result == False:
            return
        
        pushBoxUpOrDown(robot_x, robot_y-1, direction)
        grid[robot_y - 1, robot_x] = '@'
        grid[robot_y, robot_x] = '.'
        robot_y -= 1


    elif (direction == 'v'):
        result = checkIfCanPushUpOrDown(robot_x, robot_y+1, direction)

        if result == False:
            return
        
        pushBoxUpOrDown(robot_x, robot_y+1, direction)
        grid[robot_y + 1, robot_x] = '@'
        grid[robot_y, robot_x] = '.'
        robot_y += 1











for direction in movement:
    tryMove(direction)
        


total_score = 0
for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        if (grid[y,x] == '['):
            total_score += y * 100 + x



print(total_score)