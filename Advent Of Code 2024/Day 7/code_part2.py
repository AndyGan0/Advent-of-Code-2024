import numpy as np


# Load the grid
filename = "Day 7\input.txt"
with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]


def tryCombinations(equation_numbers: np.ndarray, testValue: int):
    if (equation_numbers.shape[0] == 1):
        return [ int(equation_numbers[0])]
    
    resultsFromNext = tryCombinations(equation_numbers[:-1] , testValue)
    NewResults = []
    for item in resultsFromNext:
        temp1 = item * int(equation_numbers[-1])
        temp2 = item + int(equation_numbers[-1])
        temp3 = int(str(item) + str(equation_numbers[-1]))

        if (temp1 <= testValue):
            NewResults.append(temp1)
        if (temp2 <= testValue):
            NewResults.append(temp2)
        if (temp3 <= testValue):
            NewResults.append(temp3)

    return NewResults
    



sum = 0

for line in grid:
    test_value , equation_numbers = line.split(":")
    test_value = int(test_value)
    equation_numbers = equation_numbers[1:].split(" ")
    equation_numbers = [int(x) for x in equation_numbers]
    equation_numbers = np.array(equation_numbers, dtype=int)

    results = tryCombinations(equation_numbers, test_value)

    if (test_value in results):
         sum += test_value


print(sum)