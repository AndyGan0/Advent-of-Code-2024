import numpy as np



rulesDict = {}


def addRule(lineString: str):
    # Dimensions of the grid
    firstNum, secNum = lineString.split("|")

    value = rulesDict.get(firstNum)
    if value is not None:
        # key exists
        rulesDict[firstNum].append(secNum)
        
    else:
        # key doesnt exists        
        rulesDict[firstNum] = [secNum]





def is_update_valid(update):
    past_updated = []

    for value in update:
        values_after = rulesDict[value]
        for after_v in values_after:
            if (after_v in past_updated):
                return False
        past_updated.append(value)
    
    return True





#   loading the file
with open("Day 5\input.txt", 'r') as file:
    grid = [line.strip() for line in file if line.strip()]

i = 0
while ( "|" in grid[i] ):
    addRule(grid[i])
    i += 1


sum = 0

while (i < len(grid)):    

    currentUpdate = grid[i].split(",")

    
    if (is_update_valid(currentUpdate)):
        middleNum = currentUpdate[len(currentUpdate) // 2]

        sum += int(middleNum)
    
    i += 1

print(sum)
        
    



