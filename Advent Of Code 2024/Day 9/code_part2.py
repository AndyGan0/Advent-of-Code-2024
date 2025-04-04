import numpy as np





filename = "Day 9\input.txt"
with open(filename, 'r') as file:
        file = [line.strip() for line in file if line.strip()]
file = list(file[0])
file = np.array(file, dtype=int)




disk_representation = []
isFile = True
File_id = 0
for item in file:
    if (isFile):
        for blocks in range(item):
            disk_representation.append(File_id)
        isFile = False
        File_id += 1
    else:
        for blocks in range(item):
            disk_representation.append(".")        
        isFile = True




#   find empty spaces and map them to size
empty_spaces = {}
i = 0
empty_space_size = 0
while i < len(disk_representation):
     
    if disk_representation[i] == '.':
        empty_space_size += 1
    else:
        if empty_space_size != 0:
            if empty_space_size not in empty_spaces:
                empty_spaces[empty_space_size] = []
            empty_spaces[empty_space_size].append(i - empty_space_size)
        empty_space_size = 0
    
    i += 1








#   moving blocks
i = len(disk_representation) - 1
while i >= 0:

    while disk_representation[i] == '.':        
        i -= 1

    #   move i to beginning of block and calculate block size
    block_size = 1
    block_id = disk_representation[i]
    while disk_representation[i-1] == block_id:
        block_size += 1
        i -= 1

    
    #   find the first free space that this block can fit
    first_free_block = len(disk_representation)
    first_free_block_size = -1

    for key in empty_spaces:
        if key >= block_size and empty_spaces[key][0] < first_free_block:
            first_free_block = empty_spaces[key][0]
            first_free_block_size = key

    if first_free_block_size == -1 or first_free_block >= i:
        i -= 1
        continue

    empty_spaces[first_free_block_size].pop(0)
    if len(empty_spaces[first_free_block_size]) == 0:
        empty_spaces.pop(first_free_block_size)
    disk_representation[i : i+block_size] = ['.'] * block_size
    disk_representation[first_free_block : first_free_block+block_size] = [block_id] * block_size

    if first_free_block_size > block_size:
        empty_space_created_SIZE = first_free_block_size - block_size
        empty_space_created_INDEX = first_free_block + block_size

        #   insert new empty space sorted
        if empty_space_created_SIZE not in empty_spaces:
            empty_spaces[empty_space_created_SIZE] = [empty_space_created_INDEX]
        else:
            j = 0
            while empty_spaces[empty_space_created_SIZE][j] < empty_space_created_INDEX:
                j += 1
            empty_spaces[empty_space_created_SIZE].insert(j, empty_space_created_INDEX)

    
    i -= 1














sum = 0
for index in range(len(disk_representation)):
    if (disk_representation[index] == "."):
        continue

    sum += index * disk_representation[index]

print(sum)