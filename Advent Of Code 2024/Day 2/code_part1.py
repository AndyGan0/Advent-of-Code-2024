import numpy as np


safety_array = []


# Open the file and read the lines
with open('Day 2\input.txt', 'r') as file:
    for line in file:
        # Split each line by spaces and append to the respective list
        values = [int(num) for num in line.split()]
        safe = True

        if (values[0] > values[1]):
            accending = False
        elif (values[0] < values[1]):
            accending = True
        else:
            continue       

        for index in range(len(values)-1):
            if (values[index] > values[index+1]):
                if (accending == True or values[index] - values[index+1] > 3):
                    safe = False
                    break
            elif (values[index] < values[index+1]):
                if (accending == False or values[index+1] - values[index] > 3):
                    safe = False
                    break
            else:                
                safe = False
                break
        
        if (safe):
            safety_array.append(1)
            
sum = np.sum(safety_array)
print(sum)



