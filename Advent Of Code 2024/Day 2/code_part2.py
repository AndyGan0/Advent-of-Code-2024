import numpy as np


safety_array = []


items_that_Dont_respect_accension = []
items_difference_bigger_than_3 = []

# Open the file and read the lines
with open('Day 2\input.txt', 'r') as file:
    for line in file:
        # Split each line by spaces and append to the respective list
        values = [int(num) for num in line.split()]

        most_common_0 = 0
        if (values[0] > values[1]):
            most_common_0 = -1
        elif (values[0] < values[1]):
            most_common_0 = 1
        else:
            most_common_0 = 0

        most_common_1 = 0
        if (values[1] > values[2]):
            most_common_1 = -1
        elif (values[1] < values[2]):
            most_common_1 = 1
        else:
            most_common_1 = 0

        most_common_2 = 0
        if (values[2] > values[3]):
            most_common_2 = -1
        elif (values[2] < values[3]):
            most_common_2 = 1
        else:
            most_common_2 = 0

        if (most_common_0 == most_common_1):
            most_common = most_common_0
        elif (most_common_1 == most_common_2):
            most_common = most_common_1
        else:
            continue

        if (most_common == 0):
            continue



        items_that_Dont_respect_accension.clear()
        for index in range(len(values)-1):
            if (values[index] > values[index+1]):
                if (most_common == 1):
                    items_that_Dont_respect_accension.append(index)
            elif (values[index] < values[index+1]):
                if (most_common == -1):
                    items_that_Dont_respect_accension.append(index)
            else:                
                items_that_Dont_respect_accension.append(index)
        
        if (len(items_that_Dont_respect_accension) >= 2):
            continue


        items_difference_bigger_than_3.clear()
        for index in range(len(values)-1):
            if ( abs(values[index] - values[index+1]) > 3):
                    items_difference_bigger_than_3.append(index)


        if (len(items_difference_bigger_than_3) == 0 and len(items_that_Dont_respect_accension) == 1):
            safety_array.append(1)
        elif (len(items_difference_bigger_than_3) == 1 and len(items_that_Dont_respect_accension) == 0):
            safety_array.append(1)
        elif (len(items_difference_bigger_than_3) == 1 and len(items_that_Dont_respect_accension) == 1):
            if (items_difference_bigger_than_3[0] == items_that_Dont_respect_accension[0]):
                safety_array.append(1)
        elif (len(items_difference_bigger_than_3) == 0 and len(items_that_Dont_respect_accension) == 0):
            safety_array.append(1)
        
                
        
            
sum = np.sum(safety_array)
print(sum)



