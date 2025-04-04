import numpy as np



def guardWillFinishNext(LocationX:int, LocationY:int, guardSign:str):
    rightEdge = False
    leftEdge = False
    UpperEdge = False
    LowerEdge = False

    if (LocationX == 0):
        UpperEdge = True    
    if (LocationY == 0):
        leftEdge = True    
    if (LocationX == grid.shape[0] - 1):
        LowerEdge = True    
    if (LocationY == grid.shape[1] - 1):
        rightEdge = True    


    if (guardSign == "^" and UpperEdge):
        return True
    elif (guardSign == "<" and leftEdge):
        return True
    elif (guardSign == ">" and rightEdge):
        return True
    elif (guardSign == "v" and LowerEdge):
        return True
    
    return False



def checkIfGuardCanEscape(grid):
    shape = grid.shape
    visited = np.empty(shape, dtype=object)
    for i in range(visited.shape[0]):
        for j in range(visited.shape[1]):
            visited[i, j] = []



    #   finding original guard location
    guardLocationX, guardLocationY = np.where(grid == "^")
    guardLocationX = int(guardLocationX[0])
    guardLocationY = int(guardLocationY[0])

    visited[guardLocationX,guardLocationY].append(grid[guardLocationX, guardLocationY]) 

    while(guardWillFinishNext(guardLocationX, guardLocationY, grid[guardLocationX, guardLocationY]) == False):

        

        if (grid[guardLocationX, guardLocationY] == "^"):
            if (grid[guardLocationX - 1, guardLocationY] == "."):
                grid[guardLocationX, guardLocationY] = "."
                grid[guardLocationX - 1, guardLocationY] = "^"
                guardLocationX -= 1
            else:
                grid[guardLocationX, guardLocationY] = ">"

        elif (grid[guardLocationX, guardLocationY] == ">"):
            if (grid[guardLocationX, guardLocationY + 1] == "."):
                grid[guardLocationX, guardLocationY] = "."
                grid[guardLocationX, guardLocationY + 1] = ">"
                guardLocationY += 1
            else:
                grid[guardLocationX, guardLocationY] = "v"

        elif (grid[guardLocationX, guardLocationY] == "v"):
            if (grid[guardLocationX + 1, guardLocationY] == "."):
                grid[guardLocationX, guardLocationY] = "."
                grid[guardLocationX + 1, guardLocationY] = "v"
                guardLocationX += 1
            else:
                grid[guardLocationX, guardLocationY] = "<"

        elif (grid[guardLocationX, guardLocationY] == "<"):
            if (grid[guardLocationX, guardLocationY - 1] == "."):
                grid[guardLocationX, guardLocationY] = "."
                grid[guardLocationX, guardLocationY - 1] = "<"
                guardLocationY -= 1
            else:
                grid[guardLocationX, guardLocationY] = "^"
        
        if ( grid[guardLocationX, guardLocationY] in visited[guardLocationX,guardLocationY]):
            return False



        visited[guardLocationX,guardLocationY].append(grid[guardLocationX, guardLocationY]) 

    return True







# Load the grid
filename = "Day 6\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]

# Count occurrences of the word
grid = [list(string) for string in grid]
grid = np.array(grid)






originalvisited = np.zeros_like(grid, dtype=int)

#   finding original guard location
guardLocationX, guardLocationY = np.where(grid == "^")
guardLocationX = int(guardLocationX[0])
guardLocationY = int(guardLocationY[0])

originalvisited[guardLocationX,guardLocationY] = 1
while(guardWillFinishNext(guardLocationX, guardLocationY, grid[guardLocationX, guardLocationY]) == False):

    if (grid[guardLocationX, guardLocationY] == "^"):
        if (grid[guardLocationX - 1, guardLocationY] == "."):
            grid[guardLocationX, guardLocationY] = "."
            grid[guardLocationX - 1, guardLocationY] = "^"
            guardLocationX -= 1
        else:
            grid[guardLocationX, guardLocationY] = ">"

    elif (grid[guardLocationX, guardLocationY] == ">"):
        if (grid[guardLocationX, guardLocationY + 1] == "."):
            grid[guardLocationX, guardLocationY] = "."
            grid[guardLocationX, guardLocationY + 1] = ">"
            guardLocationY += 1
        else:
            grid[guardLocationX, guardLocationY] = "v"

    elif (grid[guardLocationX, guardLocationY] == "v"):
        if (grid[guardLocationX + 1, guardLocationY] == "."):
            grid[guardLocationX, guardLocationY] = "."
            grid[guardLocationX + 1, guardLocationY] = "v"
            guardLocationX += 1
        else:
            grid[guardLocationX, guardLocationY] = "<"

    elif (grid[guardLocationX, guardLocationY] == "<"):
        if (grid[guardLocationX, guardLocationY - 1] == "."):
            grid[guardLocationX, guardLocationY] = "."
            grid[guardLocationX, guardLocationY - 1] = "<"
            guardLocationY -= 1
        else:
            grid[guardLocationX, guardLocationY] = "^"
    
    originalvisited[guardLocationX,guardLocationY] = 1















# Load the grid
filename = "Day 6\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]

# Count occurrences of the word
grid = [list(string) for string in grid]
grid = np.array(grid)





sum = 0
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if (grid[i,j] == "#" or grid[i,j] == "^"):
            continue

        if (originalvisited[i,j] == 0):
            continue

        modifiedGrid = grid.copy()
        modifiedGrid[i,j] = "#"
        if (checkIfGuardCanEscape(modifiedGrid) == False):
            sum += 1

print(sum)

