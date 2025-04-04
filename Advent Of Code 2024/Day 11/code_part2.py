import numpy as np



# Load the grid
filename = "Day 11\input.txt"
with open(filename, 'r') as file:
        file = [line.split() for line in file]
file = np.int64(file[0])


#   dict for dynamic programming
#   it has the stones as keys
#   each value is another dict that maps number of blinks to number of stones
dynamic_dict = {}




def calculate_number_of_children_after_blink(stone, num_of_blinks):

    if (num_of_blinks == 0):
        return
    
    if stone not in dynamic_dict:
        dynamic_dict[stone] = {}
    
    if num_of_blinks in dynamic_dict[stone]:
        return
    

    children_after_1_blink = []

    if (stone == 0):
        children_after_1_blink.append(1)
    elif (len(str(stone)) % 2 == 0):
        first_half = str(stone)[:len(str(stone))//2]
        second_half = str(stone)[len(str(stone))//2:]
        first_half.lstrip('0')
        second_half.lstrip('0')
        if (len(first_half) == 0):
            first_half = '0'
        if (len(second_half) == 0):
            second_half = '0'
        
        children_after_1_blink.append(int(first_half))
        children_after_1_blink.append(int(second_half))    
    else:
        children_after_1_blink.append(stone * 2024)
    


    for child in children_after_1_blink:
        calculate_number_of_children_after_blink(child, num_of_blinks-1)


    if num_of_blinks == 1:
        dynamic_dict[stone][num_of_blinks] = len(children_after_1_blink)
    else:
        dynamic_dict[stone][num_of_blinks] = 0
        for child in children_after_1_blink:
            dynamic_dict[stone][num_of_blinks] += dynamic_dict[child][num_of_blinks - 1]




        
        


sum_of_final_stones = 0
number_of_blinks = 75
for stone in file:    
    calculate_number_of_children_after_blink(stone, number_of_blinks)
    sum_of_final_stones += dynamic_dict[stone][number_of_blinks]



print(sum_of_final_stones)



