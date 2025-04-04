import numpy as np
from PIL import Image



# Load the grid
filename = "Day 14\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
grid = [string.split(" ") for string in grid]


tiles_x = 101
tiles_y = 103
middle_tile_x = int(tiles_x/2)
middle_tile_y = int(tiles_y/2)

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





def saveTreeInFolder(robot_list, seconds):

     shape = (tiles_y, tiles_x)
     image = np.full(shape, 0, dtype=int)

     for robot in robot_list:
        image[robot["p_y"],robot["p_x"]] = 255

     image_file = Image.fromarray(image)
     image_file = image_file.convert("L")
     image_file.save("Day 14/images/file_" + str(seconds) + ".png")


     

        




for seconds in range(10000):
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



    saveTreeInFolder(robot_list, seconds+1)

#   answer is in the folder (file 6752)

