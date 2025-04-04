import numpy as np



# Load the grid
filename = "Day 10\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
grid = [list(string) for string in grid]
grid = np.array(grid, dtype=int)




def num_of_Paths(i, j):
    currentHeight = grid[i,j]

    if (currentHeight == 9):
        return 1
    
    number_of_paths = 0

    if (i != 0 and grid[i - 1,j] == currentHeight + 1):
        number_of_paths += num_of_Paths(i-1, j)
    
    if (i != grid.shape[0]-1 and grid[i + 1,j] == currentHeight + 1):
        number_of_paths += num_of_Paths(i+1, j)
    
    if (j != 0 and grid[i, j - 1] == currentHeight + 1):
        number_of_paths += num_of_Paths(i, j-1)
    
    if (j != grid.shape[1]-1 and grid[i, j + 1] == currentHeight + 1):
        number_of_paths += num_of_Paths(i, j+1)

    return number_of_paths

         
sum_score = 0

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        # for all items as start find paths
        if (grid[i,j] != 0):
            continue

        score = num_of_Paths(i, j)

        sum_score += score

       




print(sum_score)



