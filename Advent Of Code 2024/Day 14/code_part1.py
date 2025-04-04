import numpy as np



# Load the grid
filename = "Day 14\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
grid = [string.split(" ") for string in grid]


tiles_x = 101
tiles_y = 103

robot_list = []


for robot in range(len(grid)):
    p_x, p_y = grid[robot][0].split(",")
    v_x, v_y = grid[robot][1].split(",")

    p_x = int(p_x[2:])
    p_y = int(p_y)
    v_x = int(v_x[2:])
    v_y = int(v_y)
    
    robot_list.append({
        "p_x" : p_x,
        "p_y" : p_y,
        "v_x" : v_x,
        "v_y" : v_y
    })


    

for second in range(100):
    for robot in robot_list:
        robot["p_x"] = robot["p_x"] + robot["v_x"]
        robot["p_y"] = robot["p_y"] + robot["v_y"]

        if (robot["p_x"] < 0):
            robot["p_x"] = tiles_x + robot["p_x"]
        elif (robot["p_x"] >= tiles_x):
            robot["p_x"] = robot["p_x"] - tiles_x
        
        if (robot["p_y"] < 0):
            robot["p_y"] = tiles_y + robot["p_y"]
        elif (robot["p_y"] >= tiles_y):
            robot["p_y"] = robot["p_y"] - tiles_y



quadrant_top_left = 0
quadrant_top_right = 0
quadrant_bottom_left = 0
quadrant_bottom_right = 0


middle_tile_x = int(tiles_x/2)
middle_tile_y = int(tiles_y/2)
        
for robot in robot_list:
    if (robot["p_x"] == middle_tile_x or robot["p_y"] == middle_tile_y):
        continue

    if (robot["p_x"] < middle_tile_x and robot["p_y"] < middle_tile_y):
        quadrant_top_left += 1
    elif (robot["p_x"] > middle_tile_x and robot["p_y"] < middle_tile_y):
        quadrant_top_right += 1
    elif (robot["p_x"] < middle_tile_x and robot["p_y"] > middle_tile_y):
        quadrant_bottom_left += 1
    elif (robot["p_x"] > middle_tile_x and robot["p_y"] > middle_tile_y):
        quadrant_bottom_right += 1


final = quadrant_top_left * quadrant_top_right * quadrant_bottom_left * quadrant_bottom_right
print(final)