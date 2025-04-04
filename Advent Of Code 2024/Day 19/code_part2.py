import numpy as np



# Load the grid
filename = "Day 19\input.txt"
with open(filename, 'r') as file:
    file = [line for line in file]


towel_patterns = []
line = 0
for line in range(len (file)):
    if (file[line] == '\n'):
        break
    towel_patterns.append(file[line].split(','))
towel_patterns = towel_patterns[0]
towel_patterns[-1] = towel_patterns[-1][:-1]
towel_patterns = { x.strip(): None for x in towel_patterns}

desired_patterns = []
for line in range(line + 1, len(file)):
    desired_patterns.append(file[line])
for i in range(len(desired_patterns)):    
    if (desired_patterns[i][-1] == '\n'):
        desired_patterns[i] = desired_patterns[i][:-1]





def find_all_occurrences(desired, pattern):
    positions = []
    start = 0
    
    while True:
        start = desired.find(pattern, start)  # Find from the current position
        if start == -1:  # No more occurrences
            break
        positions.append(start)
        start += 1  # Move past the current match to avoid infinite loop
    
    return positions




def TrycreatePatterns(can_be_made: np.array):
    help_dict = {}
    for i in range(can_be_made.shape[0]):
        for j in range(can_be_made.shape[1]):
            if (can_be_made[i,j]):
                if i not in help_dict:
                    help_dict[i] = {}
                help_dict[i][j] = 1

    if (0 not in help_dict):
        return False

    while (len(help_dict[0]) != 0 and any(key != can_be_made.shape[0] - 1 for key in help_dict[0])):
        smallest_key = min(help_dict[0])        
        
        ways_to_get = help_dict[0].pop(smallest_key)
        if (smallest_key+1) in help_dict:
            for next in help_dict[smallest_key+1]:
                if next in help_dict[0]:
                    help_dict[0][next] += ways_to_get
                else:
                    help_dict[0][next] = ways_to_get


    if (len(help_dict[0]) == 0):
        return 0


    return help_dict[0][can_be_made.shape[0] - 1]






count = 0
for desired in desired_patterns:

    can_be_made = np.zeros(shape=(len(desired), len(desired)) , dtype=bool)

    for pattern in towel_patterns:
        positions = find_all_occurrences(desired, pattern)

        for pos in positions:
            last_pos = pos + len(pattern) - 1
            can_be_made[pos, last_pos] = True


    count += TrycreatePatterns(can_be_made)





print(count)