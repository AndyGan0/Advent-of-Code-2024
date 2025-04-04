import numpy as np



# Load the grid
filename = "Day 12\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
grid = [list(string) for string in grid]
grid = np.array(grid)

visited = np.empty_like(grid, dtype=object)
for i in range(visited.shape[0]):
    for j in range(visited.shape[1]):
        visited[i, j] = { }
        visited[i, j]["self"] = False
        visited[i, j]["hasPerimeter_above"] = False
        visited[i, j]["hasPerimeter_below"] = False
        visited[i, j]["hasPerimeter_right"] = False
        visited[i, j]["hasPerimeter_left"] = False




def findAreaAndPerimeter(i, j):
    visited[i,j]["self"] = True
    area = 1
    perimeter = 0

    #   above
    if ( i != 0 and grid[i-1,j] == grid[i,j] and visited[i-1,j]["self"] == False):
        area_above, perimeter_above = findAreaAndPerimeter(i-1, j)
        area += area_above
        perimeter += perimeter_above

    #   right
    if ( j != grid.shape[1] - 1 and grid[i,j+1] == grid[i,j] and visited[i,j+1]["self"] == False):
        area_right, perimeter_right = findAreaAndPerimeter(i, j+1)
        area += area_right
        perimeter += perimeter_right

    #   below
    if ( i < grid.shape[0] - 1 and grid[i+1,j] == grid[i,j] and visited[i+1,j]["self"] == False):
        area_below, perimeter_below = findAreaAndPerimeter(i+1, j)
        area += area_below
        perimeter += perimeter_below

    #   left
    if ( j != 0 and grid[i,j-1] == grid[i,j] and visited[i,j-1]["self"] == False):
        area_left, perimeter_left = findAreaAndPerimeter(i, j-1)
        area += area_left
        perimeter += perimeter_left



    #   above
    if (i == 0 or grid[i-1,j] != grid[i,j]):
        #   checking if side has been counted before
        if ( (j == 0 or grid[i,j-1] != grid[i,j] or visited[i,j-1]["hasPerimeter_above"] == False) and (j == grid.shape[1] - 1 or grid[i,j+1] != grid[i,j] or  visited[i,j+1]["hasPerimeter_above"] == False) ):
            perimeter += 1
        elif ( j != 0 and j != grid.shape[1] - 1 and grid[i,j-1] == grid[i,j] and grid[i,j+1] == grid[i,j] and visited[i,j-1]["hasPerimeter_above"] == True and visited[i,j+1]["hasPerimeter_above"] == True ):
            perimeter -= 1
        visited[i,j]["hasPerimeter_above"] = True


    #   right
    if (j == grid.shape[1] - 1 or grid[i,j+1] != grid[i,j]):
        #   checking if side has been counted before
        if ( (i == 0 or grid[i-1,j] != grid[i,j] or visited[i-1,j]["hasPerimeter_right"] == False) and (i == grid.shape[0] - 1 or grid[i+1,j] != grid[i,j] or visited[i+1,j]["hasPerimeter_right"] == False) ):
            perimeter += 1
        elif ( i != 0 and i != grid.shape[0] - 1 and grid[i-1,j] == grid[i,j] and grid[i+1,j] == grid[i,j] and visited[i-1,j]["hasPerimeter_right"] == True and visited[i+1,j]["hasPerimeter_right"] == True ):
            perimeter -= 1
        visited[i,j]["hasPerimeter_right"] = True

    #   below
    if (i == grid.shape[0] - 1  or grid[i+1,j] != grid[i,j]):
        #   checking if side has been counted before
        if ( (j == 0 or grid[i,j-1] != grid[i,j] or visited[i,j-1]["hasPerimeter_below"] == False) and (j == grid.shape[1] - 1  or grid[i,j+1] != grid[i,j] or visited[i,j+1]["hasPerimeter_below"] == False) ):
            perimeter += 1
        elif ( j != 0 and j != grid.shape[1] - 1 and grid[i,j-1] == grid[i,j] and grid[i,j+1] == grid[i,j] and visited[i,j-1]["hasPerimeter_below"] == True and visited[i,j+1]["hasPerimeter_below"] == True ):
            perimeter -= 1
        visited[i,j]["hasPerimeter_below"] = True         

    #   left
    if (j == 0  or grid[i,j-1] != grid[i,j]):
        #   checking if side has been counted before
        if ( (i == 0 or grid[i-1,j] != grid[i,j] or visited[i-1,j]["hasPerimeter_left"] == False) and (i == grid.shape[0] - 1 or grid[i+1,j] != grid[i,j]  or visited[i+1,j]["hasPerimeter_left"] == False) ):
            perimeter += 1
        elif ( i != 0 and i != grid.shape[0] - 1 and grid[i-1,j] == grid[i,j] and grid[i+1,j] == grid[i,j] and visited[i-1,j]["hasPerimeter_left"] == True and visited[i+1,j]["hasPerimeter_left"] == True ):
            perimeter -= 1
        visited[i,j]["hasPerimeter_left"] = True


    return area, perimeter
    

        



    


total_cost = 0


for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):

        if (visited[i,j]["self"]):
            continue

        area, perimeter = findAreaAndPerimeter(i,j)
        cost = area * perimeter
        total_cost += cost



print(total_cost)



