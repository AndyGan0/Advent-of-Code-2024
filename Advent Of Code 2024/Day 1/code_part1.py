import numpy as np

# Open the file and read the lines
with open('Day 1\input.txt', 'r') as file:
    column1 = []
    column2 = []
    for line in file:
        # Split each line by spaces and append to the respective list
        values = line.split()
        column1.append(int(values[0]))  # Convert to integer (or float if needed)
        column2.append(int(values[1]))

column1.sort()
column2.sort()

column1 = np.array(column1)
column2 = np.array(column2)

column3 = column2 - column1
column3 = np.abs(column3)

sum_distance = np.sum(column3) 

print(sum_distance)