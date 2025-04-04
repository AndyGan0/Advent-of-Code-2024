import numpy as np



# Load the grid
filename = "Day 11\input.txt"
with open(filename, 'r') as file:
        file = [line.split() for line in file]
file = np.int64(file[0])



def blink(line):
    newLine = []

    for stone in line:
        if (stone == 0):
             newLine.append(1)
             continue
        
        number_of_digits = len(str(stone))
        if ( number_of_digits % 2 == 0 ):
            first_half = str(stone)[:number_of_digits//2]
            second_half = str(stone)[number_of_digits//2:]
            first_half.lstrip('0')
            second_half.lstrip('0')
            if (len(first_half) == 0):
                first_half = '0'
            if (len(second_half) == 0):
                second_half = '0'
            
            newLine.append(int(first_half))
            newLine.append(int(second_half))
            continue

        newLine.append(stone * 2024)        

        
    return newLine




for i in range(25):     
    file = blink(file)

print(len(file))



