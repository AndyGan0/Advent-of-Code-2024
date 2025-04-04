import numpy as np







# Load the grid
filename = "Day 6\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]

# Count occurrences of the word
grid = [list(string) for string in grid]
grid = np.array(grid)

visited = np.zeros_like(grid, dtype=int)

#   finding original guard location
guardLocationX, guardLocationY = np.where(grid == "^")
guardLocationX = int(guardLocationX[0])
guardLocationY = int(guardLocationY[0])

visited[guardLocationX,guardLocationY] = 1





def guardWillFinishNext(LocationX:int, LocationY:int, guardSign:str):
    rightEdge = False
    leftEdge = False
    UpperEdge = False
    LowerEdge = False

    if (LocationX == 0):
        UpperEdge = True    
    if (LocationY == 0):
        leftEdge = True    
    if (LocationX == grid.shape[0]):
        UpperEdge = True    
    if (LocationY == grid.shape[1]):
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
    
    visited[guardLocationX,guardLocationY] = 1

sum = np.sum(visited)
print(sum)

