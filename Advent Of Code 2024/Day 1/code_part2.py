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


column1 = np.array(column1, dtype=int)
column2 = np.array(column2, dtype=int)

# Count occurrences
second_column_occurrences = {}
for i in column2:
    if (i in second_column_occurrences):
        second_column_occurrences[i] += 1
    else:
        second_column_occurrences[i] = 1

for index,value in enumerate(column1):
    left_column_item = int(value)
    right_column_times = second_column_occurrences.get(left_column_item)
    if (right_column_times is None):
        right_column_times = 0
    column1[index] = left_column_item * right_column_times

similarity_score = column1.sum()

print(similarity_score)