import numpy as np


#   Rules
rulesDict = {}
def addRule(lineString: str):
    # Dimensions of the grid
    firstNum, secNum = lineString.split("|")

    if firstNum in rulesDict:
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
                return False, [after_v, value]
        past_updated.append(value)
    
    return True, None





def get_correct_order(update: list, problematic_nodes):
    first_problematic_value_index = update.index(problematic_nodes[0])

    update.remove(problematic_nodes[1])
    update.insert(first_problematic_value_index, problematic_nodes[1])


    return update






#   loading the file
with open("Day 5\input.txt", 'r') as file:
    grid = [line.strip() for line in file if line.strip()]

i = 0
while ( "|" in grid[i] ):
    addRule(grid[i])
    i += 1

updates_list = []
while i < len(grid):
    updates_list.append(grid[i].split(","))
    i += 1







sum = 0
for update in updates_list:
    is_valid, problematic_nodes = is_update_valid(update)

    if is_valid:
        continue

    while not is_valid:
        update = get_correct_order(update, problematic_nodes)
        is_valid, problematic_nodes = is_update_valid(update)


    middleNum = update[len(update) // 2]
    sum += int(middleNum)





print(sum)
        
    



