import numpy as np



# Load the grid
filename = "Day 12\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
grid = [list(string) for string in grid]
grid = np.array(grid)

visited = np.zeros_like(grid, dtype= bool)




def findAreaAndPerimeter(i, j):
    visited[i,j] = True
    area = 1
    perimeter = 0

    #   above
    if ( i != 0 and grid[i-1,j] == grid[i,j] and visited[i-1,j] == False):
        area_above, perimeter_above = findAreaAndPerimeter(i-1, j)
        area += area_above
        perimeter += perimeter_above
    elif (i == 0 or grid[i-1,j] != grid[i,j]):        
        perimeter += 1

    #   below
    if ( i < grid.shape[0] - 1 and grid[i+1,j] == grid[i,j] and visited[i+1,j] == False):
        area_below, perimeter_below = findAreaAndPerimeter(i+1, j)
        area += area_below
        perimeter += perimeter_below
    elif (i == grid.shape[0] - 1  or grid[i+1,j] != grid[i,j]):        
        perimeter += 1

    #   left
    if ( j != 0 and grid[i,j-1] == grid[i,j] and visited[i,j-1] == False):
        area_left, perimeter_left = findAreaAndPerimeter(i, j-1)
        area += area_left
        perimeter += perimeter_left
    elif (j == 0  or grid[i,j-1] != grid[i,j]):        
        perimeter += 1

    #   right
    if ( j != grid.shape[1] - 1 and grid[i,j+1] == grid[i,j] and visited[i,j+1] == False):
        area_right, perimeter_right = findAreaAndPerimeter(i, j+1)
        area += area_right
        perimeter += perimeter_right
    elif (j == grid.shape[1] - 1 or grid[i,j+1] != grid[i,j]):        
        perimeter += 1

    return area, perimeter
    

        



    


total_cost = 0


for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):

        if (visited[i,j]):
            continue

        area, perimeter = findAreaAndPerimeter(i,j)
        cost = area * perimeter
        total_cost += cost



print(total_cost)



