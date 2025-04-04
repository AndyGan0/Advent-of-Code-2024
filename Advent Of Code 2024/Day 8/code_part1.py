import numpy as np


def findAntinode(node1, node2):
    node1_i, node1_j = node1
    node2_i, node2_j = node2

    dif_i = node1_i - node2_i
    dif_j = node1_j - node2_j

    return node1_i + dif_i, node1_j + dif_j




# Load the grid
filename = "Day 8\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
grid = [list(string) for string in grid]
grid = np.array(grid)



differentFreqNodes = {}
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if (grid[i,j] == "." or grid[i,j] == "#"):
            continue
        if (grid[i,j] in differentFreqNodes):
            differentFreqNodes[grid[i,j]].append([i,j])
        else:
            differentFreqNodes[grid[i,j]] = [[i,j]]


locationsWithAthinodes = grid.copy()
for freq in differentFreqNodes.keys():
    for i in range(len(differentFreqNodes[freq])):
        for j in range(len(differentFreqNodes[freq])):
            if (i != j):
                antinode_i, antinode_j = findAntinode(differentFreqNodes[freq][i], differentFreqNodes[freq][j])
                if (antinode_i >= 0 and antinode_j >= 0 and antinode_i < locationsWithAthinodes.shape[0] and antinode_j < locationsWithAthinodes.shape[1]):
                    locationsWithAthinodes[antinode_i, antinode_j] = "#"


count = int(np.sum(locationsWithAthinodes == '#'))
print(count)