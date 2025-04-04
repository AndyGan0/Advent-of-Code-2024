import numpy as np



# Load the grid
filename = "Day 10\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
grid = [list(string) for string in grid]
grid = np.array(grid, dtype=int)




def continuePath(i, j, visited, NinesReachableArray):
    currentHeight = grid[i,j]    
    visited[i, j] = 1

    if (currentHeight == 9):
        NinesReachableArray[i,j] = 1
        return

    if (i != 0 and visited[i - 1,j] == 0 and grid[i - 1,j] == currentHeight + 1):
        continuePath(i-1, j, visited, NinesReachableArray)
    
    if (i != grid.shape[0]-1 and visited[i + 1,j] == 0 and grid[i + 1,j] == currentHeight + 1):
        continuePath(i+1, j, visited, NinesReachableArray)
    
    if (j != 0 and visited[i, j - 1] == 0 and grid[i, j - 1] == currentHeight + 1):
        continuePath(i, j-1, visited, NinesReachableArray)
    
    if (j != grid.shape[1]-1 and visited[i, j + 1] == 0 and grid[i, j + 1] == currentHeight + 1):
        continuePath(i, j+1, visited, NinesReachableArray)

    return NinesReachableArray

         
sum_score = 0

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        # for all items as start find paths
        if (grid[i,j] != 0):
            continue

        visited = np.zeros_like(grid, dtype=int)
        NinesReachableArray = np.zeros_like(grid, dtype=int)
        continuePath(i,j, visited, NinesReachableArray)

        score = np.sum(NinesReachableArray == 1)
        sum_score += score

       




print(sum_score)



