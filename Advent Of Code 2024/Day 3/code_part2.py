import numpy as np


mulEnabled = True
numbers = []


file = ""


with open("Day 3\input.txt", 'r', encoding='utf-8') as file:
    file = file.read()




while (len(file) > 0):
    pointer = 0

    if (file[pointer] == 'm'):
        pointer += 1    

        if (file[pointer] == 'u'):
            pointer += 1
        else:
            file = file[pointer+1:]
            continue

        if (file[pointer] == 'l'):
            pointer += 1
        else:
            file = file[pointer+1:]
            continue

        if (file[pointer] == '('):
            pointer += 1
        else:
            file = file[pointer+1:]
            continue 

        #   first number
        first_number = ""
        while (file[pointer].isdigit()):
            first_number += file[pointer]
            pointer += 1
        
        if (len(first_number) >= 1 and len(first_number)<=3):
            first_number = int(first_number)
        else:
            file = file[pointer:]
            continue 

        if (file[pointer] == ','):
            pointer += 1
        else:
            file = file[pointer+1:]
            continue 

        
        #   second number
        second_number = ""
        while (file[pointer].isdigit()):
            second_number += file[pointer]
            pointer += 1
        
        if (len(second_number) >= 1 and len(second_number)<=3):
            second_number = int(second_number)
        else:
            file = file[pointer:]
            continue 

        if (file[pointer] == ')'):
            pointer += 1
        else:
            file = file[pointer+1:]
            continue 

        file = file[pointer:]
        if (mulEnabled):
            numbers.append(first_number * second_number)

    elif (file[pointer] == 'd'):
        pointer += 1

        if (file[pointer] == 'o'):
            pointer += 1
        else:
            file = file[pointer:]
            continue 

        
        isDo = True

        if (file[pointer] == 'n'):
            pointer += 1
            if (file[pointer] == "'"):
                pointer += 1
            else:
                file = file[pointer:]
                continue 

            if (file[pointer] == "t"):
                pointer += 1
            else:
                file = file[pointer:]
                continue 

            isDo = False


        if (file[pointer] == '('):
            pointer += 1
        else:
            file = file[pointer:]
            continue

        if (file[pointer] == ')'):
            pointer += 1
        else:
            file = file[pointer:]
            continue

        file = file[pointer:]
        if (isDo == True):
            mulEnabled = True
        else:
            mulEnabled = False







    else:
        file = file[pointer+1:]
        continue


sum = np.sum(numbers)
print(sum)


    


