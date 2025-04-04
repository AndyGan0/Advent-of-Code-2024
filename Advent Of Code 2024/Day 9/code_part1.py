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




frontPointer = 0
BackPointer = len(disk_representation) - 1 

while (frontPointer != BackPointer):
    if (disk_representation[BackPointer] == "."):
        BackPointer -= 1
        continue

    while (disk_representation[frontPointer] != "."):
        frontPointer += 1    
    if (frontPointer >= BackPointer):
        break

    disk_representation[frontPointer] = disk_representation[BackPointer]
    disk_representation[BackPointer] = "."



sum = 0
for index in range(len(disk_representation)):
    if (disk_representation[index] == "."):
        break

    sum += index * disk_representation[index]

print(sum)