import math


connections_dict = {}

# Load the grid
filename = "Day 25\input.txt"
with open(filename, 'r') as file:
    file = [line for line in file]
file = [x[:-1] if x[-1] == '\n' else x for x in file ]
file = [list(string) for string in file]


locks = []
keys = []


row = 0
while row < len(file):
    current_grid = []

    while row < len(file) and len(file[row]) != 0 :
        current_grid.append(file[row])
        row += 1
    
    if current_grid[0][0] == '#':
        converted_lock = []

        for j in range(0, len(current_grid[0])):
            pins = 0
            for i in range(1, len(current_grid) - 1):
                if current_grid[i][j] == '#':
                    pins += 1
                else:
                    break
            converted_lock.append(pins)
        
        locks.append(converted_lock)

    else:
        converted_key = []

        for j in range(0, len(current_grid[0])):
            pins = 0
            for i in range(len(current_grid) - 2, 0, -1):
                if current_grid[i][j] == '#':
                    pins += 1
                else:
                    break
            converted_key.append(pins)
        
        keys.append(converted_key)
        


    row += 1




def does_key_fit_in_lock(lock: list, key: list):
    for j in range(len(lock)):
        if lock[j] + key[j] > 5:
            return False
    return True




count_pairs = 0
for lock in locks:
    for key in keys:
        if does_key_fit_in_lock(lock, key):
            count_pairs += 1
        
        





    


print(count_pairs)